# park_data.py

PARKS_DATA = [
    {
        "id": "acadia",
        "name": "Acadia National Park",
        "location": "Maine",
        "description": "Features a stunning rocky coastline, granite peaks, and historic carriage roads. Ideal for coastal hikes and scenic drives.",
        "activities": ["hiking", "biking", "boating", "wildlife watching", "stargazing", "photography", "scenic driving"],
        "scenery": ["mountains", "forests", "coasts", "lakes", "islands"],
        "image_url": "https://images.unsplash.com/photo-1553949090-4487DCA1735A?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YWNhZGlhJTIwbmF0aW9uYWwlMjBwYXJrfGVufDB8fDB8fHww&auto=format&fit=crop&w=500&q=60",
        "rating": 4.8
    },
    {
        "id": "yosemite",
        "name": "Yosemite National Park",
        "location": "California",
        "description": "Famous for its giant sequoia trees, iconic granite cliffs like El Capitan and Half Dome, and stunning waterfalls.",
        "activities": ["hiking", "rock climbing", "photography", "wildlife watching", "camping", "waterfalls", "backpacking"],
        "scenery": ["mountains", "forests", "waterfalls", "valleys", "granite cliffs", "giant sequoias"],
        "image_url": "https://images.unsplash.com/photo-1518623380242-d992d3c57b37?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8eW9zZW1pdGUlMjBuYXRpb25hbCUyMHBhcmt8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "rating": 4.9
    },
    {
        "id": "zion",
        "name": "Zion National Park",
        "location": "Utah",
        "description": "Known for its massive sandstone cliffs of cream, pink, and red that soar into a brilliant blue sky. Offers challenging hikes like The Narrows.",
        "activities": ["hiking", "canyoning", "photography", "stargazing", "rock climbing", "backpacking"],
        "scenery": ["canyons", "rivers", "cliffs", "deserts", "slot canyons"],
        "image_url": "https://images.unsplash.com/photo-1536942459870-838f6f288081?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8emlvbiUyMG5hdGlvbmFsJTIwcGFya3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "rating": 4.9
    },
    {
        "id": "yellowstone",
        "name": "Yellowstone National Park",
        "location": "Wyoming, Montana, Idaho",
        "description": "Home to geysers like Old Faithful, hot springs, and diverse wildlife including bison, elk, and bears. A geothermal wonderland.",
        "activities": ["hiking", "wildlife watching", "geothermal viewing", "camping", "fishing", "photography", "boating"],
        "scenery": ["geysers", "hot springs", "mountains", "forests", "lakes", "wildlife", "caldera"],
        "image_url": "https://images.unsplash.com/photo-1588422439500-976f05971936?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8eWVsbG93c3RvbmUlMjBuYXRpb25hbCUyMHBhcmt8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "rating": 4.7
    },
    {
        "id": "grand_canyon",
        "name": "Grand Canyon National Park",
        "location": "Arizona",
        "description": "A mile-deep canyon carved by the Colorado River, offering breathtaking views, challenging hikes, and mule rides.",
        "activities": ["hiking", "mule rides", "rafting", "photography", "stargazing", "helicopter tours"],
        "scenery": ["canyons", "rivers", "deserts", "geological formations", "sunrise/sunset views"],
        "image_url": "https://images.unsplash.com/photo-1515887406896-8a49056d51c8?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8Z3JhbmQlMjBjYW55b24lMjBuYXRpb25hbCUyMHBhcmt8ZW58MHx8MHx8fDA%3D&auto=format&fit=crop&w=500&q=60",
        "rating": 4.9
    },
    {
        "id": "everglades",
        "name": "Everglades National Park",
        "location": "Florida",
        "description": "A vast wetland ecosystem known for its unique wildlife, including alligators, manatees, and wading birds. Best explored by airboat or kayak.",
        "activities": ["boating", "kayaking", "wildlife watching", "fishing", "hiking", "bird watching", "airboat tours"],
        "scenery": ["wetlands", "mangroves", "wildlife", "sawgrass prairies"],
        "image_url": "https://images.unsplash.com/photo-1600903578939-7421573f5a40?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8ZXZlcmdsYWRlcyUyMG5hdGlvbmFsJTIwcGFya3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "rating": 4.5
    },
    {
        "id": "rocky_mountain",
        "name": "Rocky Mountain National Park",
        "location": "Colorado",
        "description": "Features majestic mountain views, diverse wildlife, and Trail Ridge Road, the highest continuous paved road in North America.",
        "activities": ["hiking", "wildlife watching", "scenic driving", "fishing", "camping", "mountaineering", "snowshoeing"],
        "scenery": ["mountains", "alpine tundra", "forests", "lakes", "wildlife"],
        "image_url": "https://images.unsplash.com/photo-1572064504051-18fe397b0996?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8cm9ja3klMjBtb3VudGFpbiUyMG5hdGlvbmFsJTIwcGFya3xlbnwwfHwwfHx8MA%3D%3D&auto=format&fit=crop&w=500&q=60",
        "rating": 4.8
    }
]

AVAILABLE_ACTIVITIES = sorted(list(set(activity for park in PARKS_DATA for activity in park["activities"])))
AVAILABLE_SCENERY = sorted(list(set(scenery_type for park in PARKS_DATA for scenery_type in park["scenery"])))