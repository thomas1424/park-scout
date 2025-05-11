# app.py
from flask import Flask, render_template, request, jsonify, session, url_for, redirect, flash, current_app
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
import werkzeug
from werkzeug.security import check_password_hash
import werkzeug
print(f"Werkzeug version: {werkzeug.__version__}")
try:
    from werkzeug.urls import url_parse
    print(f"Contents of werkzeug.urls: {dir(werkzeug.urls)}")
except AttributeError as e:
    print("werkzeug.urls module not found.")
    # Fallback to basic URL validation
    def url_parse(url):
        return type('ParseResult', (), {'netloc': lambda: None})()

from werkzeug.utils import secure_filename
from models import db, User
from forms import LoginForm, RegistrationForm, ProfileForm
import os
from park_data import PARKS_DATA, AVAILABLE_ACTIVITIES, AVAILABLE_SCENERY, AVAILABLE_REGIONS, AVAILABLE_PARK_TYPES
from PIL import Image
import uuid
from datetime import datetime

import random

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_profile_image(file):
    if not file:
        return None
        
    try:
        filename = secure_filename(str(uuid.uuid4()) + os.path.splitext(file.filename)[1])
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Save and optimize image
        image = Image.open(file)
        image.thumbnail((500, 500))
        image.save(filepath, optimize=True, quality=85)
        
        return filename
    except Exception as e:
        current_app.logger.error(f"Error saving profile image: {e}")
        return None

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev_key_change_in_production')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///parkscout.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = os.path.join(app.root_path, 'static/uploads')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Create necessary directories
os.makedirs(os.path.join(app.root_path, 'static/uploads'), exist_ok=True)
os.makedirs(os.path.join(app.root_path, 'static/img'), exist_ok=True)

# Copy default images if they don't exist
default_images = {
    'default-profile.jpg': 'https://via.placeholder.com/500x500.jpg?text=Profile',
    'default-park.jpg': 'https://via.placeholder.com/800x400.jpg?text=Park'
}

for img_name, placeholder_url in default_images.items():
    img_path = os.path.join(app.root_path, 'static/img', img_name)
    if not os.path.exists(img_path):
        try:
            import requests
            response = requests.get(placeholder_url)
            with open(img_path, 'wb') as f:
                f.write(response.content)
        except Exception as e:
            current_app.logger.error(f"Error creating default image {img_name}: {e}")

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

# Create all tables
with app.app_context():
    if not os.path.exists('parkscout.db'):
        db.create_all()

# Helper function to get park by ID
def get_park_by_id(park_id):
    try:
        return next((park for park in PARKS_DATA if park['id'] == park_id), None)
    except Exception:
        current_app.logger.error(f"Error fetching park with ID: {park_id}")
        return None

@app.context_processor
def utility_processor():
    return dict(get_park_by_id=get_park_by_id)

@app.before_request
def before_request():
    if current_user.is_authenticated and not hasattr(current_user, 'liked_parks'):
        current_user.liked_parks = []
        db.session.commit()

@app.route('/')
def welcome():
    return render_template('intro.html')

@app.route('/main', methods=['GET', 'POST'])
def index():
    recommended_parks_list = []
    selected_activities = request.form.getlist('activities') if request.method == 'POST' else []
    selected_scenery = request.form.getlist('scenery') if request.method == 'POST' else []
    selected_regions = request.form.getlist('regions') if request.method == 'POST' else []
    selected_park_types = request.form.getlist('park_types') if request.method == 'POST' else []
    search_term = request.form.get('search_term', '').strip() if request.method == 'POST' else ''

    # Start with all parks and filter down
    filtered_parks = list(PARKS_DATA) # Make a copy to filter

    if search_term:
        filtered_parks = [
            park for park in filtered_parks
            if search_term.lower() in park['name'].lower() or \
               search_term.lower() in park['description'].lower() or \
               search_term.lower() in park['location'].lower()
        ]

    if selected_park_types:
        filtered_parks = [
            park for park in filtered_parks if park.get('type') in selected_park_types
        ]

    if selected_regions:
        filtered_parks = [
            park for park in filtered_parks if park.get('region') in selected_regions
        ]
    
    if selected_activities or selected_scenery:
        temp_recommended_list = []
        for park_data in filtered_parks:
            park_copy = park_data.copy()
            match_score = 0
            activity_matches = 0
            scenery_matches = 0

            for activity in selected_activities:
                if activity in park_copy.get('activities', []):
                    match_score += 2 
                    activity_matches += 1
            
            for scenery_item in selected_scenery:
                if scenery_item in park_copy.get('scenery', []):
                    match_score += 1
                    scenery_matches += 1
            
            if match_score > 0:
                park_copy['match_score'] = match_score
                park_copy['activity_matches'] = activity_matches
                park_copy['scenery_matches'] = scenery_matches
                temp_recommended_list.append(park_copy)
        
        recommended_parks_list = sorted(temp_recommended_list, key=lambda p: p['match_score'], reverse=True)
    else: # If no activity/scenery filters, use the parks filtered by search/type/region
        recommended_parks_list = sorted(filtered_parks, key=lambda p: p.get('rating', 0), reverse=True)


    # If it's a GET request and no filters were applied (initial load or cleared filters)
    # show a default list (e.g., top-rated or a diverse selection)
    if request.method == 'GET' and not (selected_activities or selected_scenery or selected_regions or selected_park_types or search_term):
        recommended_parks_list = sorted(PARKS_DATA, key=lambda p: p.get('rating', 0), reverse=True)[:9]
    elif not recommended_parks_list and request.method == 'POST': # If POST but no matches
        pass # recommended_parks_list will be empty, template handles this

    if 'liked_parks' not in session:
        session['liked_parks'] = []

    return render_template('index.html', 
                           parks_to_display=recommended_parks_list,
                           available_activities=AVAILABLE_ACTIVITIES,
                           available_scenery=AVAILABLE_SCENERY,
                           available_regions=AVAILABLE_REGIONS,
                           available_park_types=AVAILABLE_PARK_TYPES,
                           selected_activities=selected_activities,
                           selected_scenery=selected_scenery,
                           selected_regions=selected_regions,
                           selected_park_types=selected_park_types,
                           search_term_value=search_term,
                           liked_park_ids=session.get('liked_parks', []))

@app.route('/like_park/<park_id>', methods=['POST'])
@login_required
def like_park(park_id):
    try:
        if not current_user.liked_parks:
            current_user.liked_parks = []
        
        park = get_park_by_id(park_id)
        if not park:
            return jsonify({'status': 'error', 'message': 'Park not found'}), 404

        if park_id not in current_user.liked_parks:
            current_user.liked_parks.append(park_id)
        else:
            current_user.liked_parks.remove(park_id)
        
        db.session.commit()
        return jsonify({
            'status': 'liked' if park_id in current_user.liked_parks else 'unliked',
            'message': f"Park {'added to' if park_id in current_user.liked_parks else 'removed from'} favorites!"
        })
    except Exception as e:
        db.session.rollback()
        current_app.logger.error(f"Error in like_park: {e}")
        return jsonify({'status': 'error', 'message': 'An error occurred'}), 500

@app.route('/liked')
def liked_parks_page():
    liked_park_ids = session.get('liked_parks', [])
    display_liked_parks = [park for park in PARKS_DATA if park['id'] in liked_park_ids]
    return render_template('liked_parks.html', 
                           liked_parks=display_liked_parks, 
                           liked_park_ids=liked_park_ids)

@app.route('/park/<park_id>')
def park_detail_page(park_id):
    park = get_park_by_id(park_id)
    if park:
        if 'liked_parks' not in session:
            session['liked_parks'] = []
        return render_template('park_detail.html', park=park, liked_park_ids=session.get('liked_parks', []))
    return render_template('404.html'), 404

@app.route('/map')
def map_page():
    # Pass relevant park data for map plotting
    all_parks_for_map = [
        {
            "name": p["name"], 
            "lat": p.get("latitude"), 
            "lon": p.get("longitude"), 
            "id": p["id"],
            "type": p.get("type", "Unknown Type"),
            "image_url": p.get("image_url") # For richer popups, if desired
        } 
        for p in PARKS_DATA if p.get("latitude") and p.get("longitude")
    ]
    return render_template('map.html', parks_for_map=all_parks_for_map)

@app.route('/parks')
def parks():
    q = request.args.get('q', '').strip().lower()
    region = request.args.get('region', '')
    type_ = request.args.get('type', '')
    parks_filtered = PARKS_DATA
    if q:
        parks_filtered = [p for p in parks_filtered if q in p['name'].lower() or q in p['location'].lower() or q in p['description'].lower()]
    if region:
        parks_filtered = [p for p in parks_filtered if p['region'] == region]
    if type_:
        parks_filtered = [p for p in parks_filtered if p['type'] == type_]
    # If no filters, show all parks
    if not q and not region and not type_:
        parks_filtered = PARKS_DATA
    parks_sorted = sorted(parks_filtered, key=lambda p: p['name'])
    liked_park_ids = session.get('liked_parks', [])
    return render_template('all_parks.html', parks=parks_sorted, liked_park_ids=liked_park_ids)

@app.route('/gallery')
def gallery():
    parks_sorted = sorted(PARKS_DATA, key=lambda p: p['name'])
    return render_template('gallery.html', parks=parks_sorted)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/random_park')
def random_park():
    park = random.choice(PARKS_DATA)
    return redirect(url_for('park_detail_page', park_id=park['id']))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password', 'error')
            return redirect(url_for('login'))
        login_user(user)
        next_page = request.args.get('next')
        try:
            # Add error handling for URL parsing
            if not next_page or url_parse(next_page).netloc:
                next_page = url_for('index')
        except Exception as e:
            current_app.logger.error(f"Error parsing next URL: {e}")
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Register', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if not hasattr(current_user, 'liked_parks') or current_user.liked_parks is None:
        current_user.liked_parks = []
        db.session.commit()

    form = ProfileForm()
    if form.validate_on_submit():
        try:
            if form.profile_image.data:
                filename = save_profile_image(form.profile_image.data)
                if filename:
                    if current_user.profile_image:
                        try:
                            old_file = os.path.join(current_app.config['UPLOAD_FOLDER'], current_user.profile_image)
                            if os.path.exists(old_file):
                                os.remove(old_file)
                        except Exception as e:
                            current_app.logger.error(f"Error removing old profile image: {e}")
                    current_user.profile_image = filename

            current_user.bio = form.bio.data
            current_user.location = form.location.data
            current_user.updated_at = datetime.utcnow()
            db.session.commit()
            flash('Profile updated successfully!', 'success')
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(f"Error updating profile: {e}")
            flash('An error occurred while updating your profile.', 'error')
        return redirect(url_for('profile'))

    elif request.method == 'GET':
        form.bio.data = current_user.bio
        form.location.data = current_user.location

    return render_template(
        'auth/profile.html', 
        form=form,
        created_at=current_user.created_at.strftime('%B %Y') if current_user.created_at else 'Unknown'
    )

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)