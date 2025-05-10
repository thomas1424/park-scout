# app.py
from flask import Flask, render_template, request, jsonify, session, url_for
from park_data import PARKS_DATA, AVAILABLE_ACTIVITIES, AVAILABLE_SCENERY # Import from park_data.py

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_for_a_secure_session' # CHANGE THIS!

# Helper function to get park by ID
def get_park_by_id(park_id):
    for park in PARKS_DATA:
        if park["id"] == park_id:
            return park
    return None

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_parks_list = []
    selected_activities = []
    selected_scenery = []
    search_term = request.form.get('search_term', '').strip() if request.method == 'POST' else ''

    if request.method == 'POST':
        selected_activities = request.form.getlist('activities')
        selected_scenery = request.form.getlist('scenery')

        temp_parks_to_consider = PARKS_DATA

        # Filter by search term first if provided
        if search_term:
            temp_parks_to_consider = [
                park for park in temp_parks_to_consider 
                if search_term.lower() in park['name'].lower() or \
                   search_term.lower() in park['description'].lower() or \
                   search_term.lower() in park['location'].lower()
            ]
        
        # Then filter by preferences if any selected
        if selected_activities or selected_scenery:
            for park in temp_parks_to_consider:
                park_copy = park.copy() # Avoid modifying original data
                match_score = 0
                activity_matches = 0
                scenery_matches = 0

                for activity in selected_activities:
                    if activity in park_copy['activities']:
                        match_score += 2 # Weight activities slightly higher
                        activity_matches += 1
                
                for scenery_item in selected_scenery:
                    if scenery_item in park_copy['scenery']:
                        match_score += 1
                        scenery_matches += 1
                
                if match_score > 0 : # Only include if there's at least one preference match
                    park_copy['match_score'] = match_score
                    park_copy['activity_matches'] = activity_matches
                    park_copy['scenery_matches'] = scenery_matches
                    recommended_parks_list.append(park_copy)
            
            # Sort by score, descending
            recommended_parks_list.sort(key=lambda p: p['match_score'], reverse=True)
        elif search_term: # If only search term was used, show those results
            recommended_parks_list = temp_parks_to_consider
        else: # No preferences and no search, show all initially or a curated list
            recommended_parks_list = PARKS_DATA[:6] # Show some parks by default if no filter

    else: # GET request (initial page load)
         # Show all parks or a selection, perhaps shuffled or popular
        recommended_parks_list = sorted(PARKS_DATA, key=lambda p: p.get('rating', 0), reverse=True)[:6]


    # Ensure liked_parks is initialized in session
    if 'liked_parks' not in session:
        session['liked_parks'] = []

    return render_template('index.html', 
                           parks_to_display=recommended_parks_list,
                           available_activities=AVAILABLE_ACTIVITIES,
                           available_scenery=AVAILABLE_SCENERY,
                           selected_activities=selected_activities,
                           selected_scenery=selected_scenery,
                           search_term_value=search_term,
                           liked_park_ids=session.get('liked_parks', []))

@app.route('/like_park/<park_id>', methods=['POST'])
def like_park(park_id):
    if 'liked_parks' not in session:
        session['liked_parks'] = []
    
    if park_id not in session['liked_parks']:
        session['liked_parks'].append(park_id)
        session.modified = True 
        return jsonify({'status': 'liked', 'park_id': park_id, 'message': f'{get_park_by_id(park_id)["name"]} added to your liked parks!'})
    else:
        session['liked_parks'].remove(park_id)
        session.modified = True
        return jsonify({'status': 'unliked', 'park_id': park_id, 'message': f'{get_park_by_id(park_id)["name"]} removed from your liked parks.'})

@app.route('/liked')
def liked_parks_page():
    liked_park_ids = session.get('liked_parks', [])
    display_liked_parks = [park for park in PARKS_DATA if park['id'] in liked_park_ids]
    return render_template('liked_parks.html', 
                           liked_parks=display_liked_parks, 
                           liked_park_ids=liked_park_ids) # Pass liked_park_ids for consistency in like button state

@app.route('/park/<park_id>')
def park_detail_page(park_id): # Renamed to avoid conflict with variable name
    park = get_park_by_id(park_id)
    if park:
        # Ensure liked_parks is initialized in session for the detail page
        if 'liked_parks' not in session:
            session['liked_parks'] = []
        return render_template('park_detail.html', park=park, liked_park_ids=session.get('liked_parks', []))
    return render_template('404.html'), 404 # Optional 404 page

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001) # Using port 5001 to avoid common conflicts