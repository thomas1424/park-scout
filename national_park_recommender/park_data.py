# park_data.py

PARKS_DATA = [
    {
        "id": "acadia",
        "name": "Acadia National Park",
        "location": "Maine",
        "description": "Features a stunning rocky coastline, granite peaks, and historic carriage roads. Ideal for coastal hikes and scenic drives.",
        "activities": ["hiking", "biking", "boating", "wildlife watching", "stargazing", "photography", "scenic driving"],
        "scenery": ["mountains", "forests", "coasts", "lakes", "islands"],
        "image_url": "https://images.unsplash.com/photo-1693307481261-1725dbe5a61f?q=80&w=1373&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
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
        "image_url": "https://images.unsplash.com/photo-1443632864897-14973fa006cf?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "rating": 4.9
    },
    {
        "id": "yellowstone",
        "name": "Yellowstone National Park",
        "location": "Wyoming, Montana, Idaho",
        "description": "Home to geysers like Old Faithful, hot springs, and diverse wildlife including bison, elk, and bears. A geothermal wonderland.",
        "activities": ["hiking", "wildlife watching", "geothermal viewing", "camping", "fishing", "photography", "boating"],
        "scenery": ["geysers", "hot springs", "mountains", "forests", "lakes", "wildlife", "caldera"],
        "image_url": "https://images.unsplash.com/photo-1529439322271-42931c09bce1?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8eWVsbG93c3RvbmUlMjBuYXRpb25hbCUyMHBhcmt8ZW58MHx8MHx8fDA%3D",
        "rating": 4.7
    },
    {
        "id": "grand_canyon",
        "name": "Grand Canyon National Park",
        "location": "Arizona",
        "description": "A mile-deep canyon carved by the Colorado River, offering breathtaking views, challenging hikes, and mule rides.",
        "activities": ["hiking", "mule rides", "rafting", "photography", "stargazing", "helicopter tours"],
        "scenery": ["canyons", "rivers", "deserts", "geological formations", "sunrise/sunset views"],
        "image_url": "https://images.unsplash.com/photo-1456425712190-0dd8c2b00156?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8Z3JhbmQlMjBjYW55b24lMjBuYXRpb25hbCUyMHBhcmt8ZW58MHx8MHx8fDA%3D",
        "rating": 4.9
    },
    {
        "id": "everglades",
        "name": "Everglades National Park",
        "location": "Florida",
        "description": "A vast wetland ecosystem known for its unique wildlife, including alligators, manatees, and wading birds. Best explored by airboat or kayak.",
        "activities": ["boating", "kayaking", "wildlife watching", "fishing", "hiking", "bird watching", "airboat tours"],
        "scenery": ["wetlands", "mangroves", "wildlife", "sawgrass prairies"],
        "image_url": "https://images.unsplash.com/photo-1638552903242-4e3103f8ef69?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "rating": 4.5
    },
    {
        "id": "rocky_mountain",
        "name": "Rocky Mountain National Park",
        "location": "Colorado",
        "description": "Features majestic mountain views, diverse wildlife, and Trail Ridge Road, the highest continuous paved road in North America.",
        "activities": ["hiking", "wildlife watching", "scenic driving", "fishing", "camping", "mountaineering", "snowshoeing"],
        "scenery": ["mountains", "alpine tundra", "forests", "lakes", "wildlife"],
        "image_url": "https://images.unsplash.com/photo-1600542158543-1faed2d1c05d?q=80&w=1631&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
        "rating": 4.8
    }
]

AVAILABLE_ACTIVITIES = sorted(list(set(activity for park in PARKS_DATA for activity in park["activities"])))
AVAILABLE_SCENERY = sorted(list(set(scenery_type for park in PARKS_DATA for scenery_type in park["scenery"])))