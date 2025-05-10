# app.py
from flask import Flask, render_template, request, jsonify, session, url_for, redirect
from park_data import PARKS_DATA, AVAILABLE_ACTIVITIES, AVAILABLE_SCENERY, AVAILABLE_REGIONS, AVAILABLE_PARK_TYPES

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_for_a_secure_session' # CHANGE THIS!

# Helper function to get park by ID
def get_park_by_id(park_id):
    for park in PARKS_DATA:
        if park["id"] == park_id:
            return park
    return None

@app.route('/')
def welcome():
    return render_template('intro.html')

@app.route('/main', methods=['GET', 'POST'])
def index():
    recommended_parks_list = []
    selected_activities = []
    selected_scenery = []
    selected_regions = []
    selected_park_types = []
    search_term = request.form.get('search_term', '').strip() if request.method == 'POST' else ''

    if request.method == 'POST':
        selected_activities = request.form.getlist('activities')
        selected_scenery = request.form.getlist('scenery')
        selected_regions = request.form.getlist('regions')
        selected_park_types = request.form.getlist('park_types')

        temp_parks_to_consider = PARKS_DATA

        # Filter by search term if provided
        if search_term:
            temp_parks_to_consider = [
                park for park in temp_parks_to_consider
                if search_term.lower() in park['name'].lower() or \
                   search_term.lower() in park['description'].lower() or \
                   search_term.lower() in park['location'].lower()
            ]

        # Filter by park types
        if selected_park_types:
            temp_parks_to_consider = [
                park for park in temp_parks_to_consider if park.get('type') in selected_park_types
            ]

        # Filter by regions
        if selected_regions:
            temp_parks_to_consider = [
                park for park in temp_parks_to_consider if park.get('region') in selected_regions
            ]
        
        # Then filter by activities and scenery if any selected
        if selected_activities or selected_scenery:
            for park_data in temp_parks_to_consider: # Changed variable name to avoid conflict
                park_copy = park_data.copy() # Avoid modifying original data
                match_score = 0
                activity_matches = 0
                scenery_matches = 0

                for activity in selected_activities:
                    if activity in park_copy.get('activities', []):
                        match_score += 2 # Weight activities slightly higher
                        activity_matches += 1
                
                for scenery_item in selected_scenery:
                    if scenery_item in park_copy.get('scenery', []):
                        match_score += 1
                        scenery_matches += 1
                
                if match_score > 0 : # Only include if there's at least one preference match
                    park_copy['match_score'] = match_score
                    park_copy['activity_matches'] = activity_matches
                    park_copy['scenery_matches'] = scenery_matches
                    recommended_parks_list.append(park_copy)
            
            recommended_parks_list.sort(key=lambda p: p['match_score'], reverse=True)
        else: # If only search term, park types or regions were used, show those results
            recommended_parks_list = temp_parks_to_consider
            # Optional: sort remaining by rating if no activity/scenery preference
            recommended_parks_list.sort(key=lambda p: p.get('rating', 0), reverse=True)


    else: # GET request (initial page load)
        recommended_parks_list = sorted(PARKS_DATA, key=lambda p: p.get('rating', 0), reverse=True)[:9]


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
def like_park(park_id):
    if 'liked_parks' not in session:
        session['liked_parks'] = []
    
    park = get_park_by_id(park_id) # Get park details to use name in message
    if not park:
        return jsonify({'status': 'error', 'message': 'Park not found.'}), 404

    if park_id not in session['liked_parks']:
        session['liked_parks'].append(park_id)
        session.modified = True 
        return jsonify({'status': 'liked', 'park_id': park_id, 'message': f'{park["name"]} added to your liked parks!'})
    else:
        session['liked_parks'].remove(park_id)
        session.modified = True
        return jsonify({'status': 'unliked', 'park_id': park_id, 'message': f'{park["name"]} removed from your liked parks.'})

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
    # Pass all parks for potential map plotting, could be refined later
    all_parks_for_map = [{"name": p["name"], "lat": p.get("latitude"), "lon": p.get("longitude"), "id": p["id"]} for p in PARKS_DATA if p.get("latitude") and p.get("longitude")]
    return render_template('map.html', parks_for_map=all_parks_for_map)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)