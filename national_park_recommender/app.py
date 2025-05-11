# app.py
from flask import Flask, render_template, request, jsonify, session, url_for, redirect, flash
from park_data import PARKS_DATA, AVAILABLE_ACTIVITIES, AVAILABLE_SCENERY, AVAILABLE_REGIONS, AVAILABLE_PARK_TYPES

import math

# Simple static ZIP to lat/lon mapping for demo (expand as needed)
ZIP_LATLON = {
    "10001": (40.7506, -73.9972),  # New York, NY
    "94103": (37.7739, -122.4312), # San Francisco, CA
    "60601": (41.8853, -87.6229),  # Chicago, IL
    "90001": (33.9731, -118.2479), # Los Angeles, CA
    "30301": (33.7490, -84.3880),  # Atlanta, GA
    "33101": (25.7751, -80.2105),  # Miami, FL
    "80202": (39.7525, -104.9995), # Denver, CO
    "73301": (30.2672, -97.7431),  # Austin, TX
    "02101": (42.3601, -71.0589),  # Boston, MA
    "98101": (47.6101, -122.3365), # Seattle, WA
}

def haversine(lat1, lon1, lat2, lon2):
    # Calculate the great-circle distance between two points
    R = 6371  # Earth radius in km
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

app = Flask(__name__)
app.secret_key = 'your_very_secret_key_for_a_secure_session_b1x9d' # CHANGE THIS!

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
def like_park(park_id):
    if 'liked_parks' not in session:
        session['liked_parks'] = []
    
    park = get_park_by_id(park_id) 
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

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/find_closest', methods=['GET', 'POST'])
def find_closest():
    user_zip = None
    user_lat = None
    user_lon = None
    parks_with_distance = []
    error = None
    if request.method == 'POST':
        user_zip = request.form.get('zip_code', '').strip()
        coords = ZIP_LATLON.get(user_zip)
        if not coords:
            error = "Sorry, we couldn't find that ZIP code. Try a major US city ZIP."
        else:
            user_lat, user_lon = coords
            for park in PARKS_DATA:
                if park.get('latitude') and park.get('longitude'):
                    dist = haversine(user_lat, user_lon, park['latitude'], park['longitude'])
                    park_copy = park.copy()
                    park_copy['distance_km'] = round(dist, 1)
                    parks_with_distance.append(park_copy)
            parks_with_distance.sort(key=lambda p: p['distance_km'])
    return render_template('find_closest.html', user_zip=user_zip, user_lat=user_lat, user_lon=user_lon, parks=parks_with_distance, error=error)

@app.route('/api/nearby_parks')
def api_nearby_parks():
    # AJAX endpoint for map
    lat = request.args.get('lat', type=float)
    lon = request.args.get('lon', type=float)
    if lat is None or lon is None:
        return jsonify({"error": "Missing lat/lon"}), 400
    parks = []
    for park in PARKS_DATA:
        if park.get('latitude') and park.get('longitude'):
            dist = haversine(lat, lon, park['latitude'], park['longitude'])
            parks.append({
                "id": park['id'],
                "name": park['name'],
                "lat": park['latitude'],
                "lon": park['longitude'],
                "distance_km": round(dist, 1),
                "address": park.get('address', ''),
                "location": park.get('location', ''),
                "type": park.get('type', ''),
            })
    parks.sort(key=lambda p: p['distance_km'])
    return jsonify({"parks": parks[:20]})

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)