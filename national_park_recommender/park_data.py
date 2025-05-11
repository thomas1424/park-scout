# park_data.py

PARKS_DATA = [
    # Existing US Parks (addresses and details reviewed, some image URLs might be updated for variety)
    {
        "id": "acadia", "name": "Acadia National Park", "type": "National Park", "location": "Maine, USA",
        "address": "25 Visitor Center Rd, Bar Harbor, ME 04609", "latitude": 44.3386, "longitude": -68.2733, "region": "North America",
        "description": "Features a stunning rocky coastline, granite peaks, and historic carriage roads.",
        "activities": ["hiking", "biking", "boating", "wildlife watching", "stargazing", "photography", "scenic driving"],
        "scenery": ["mountains", "forests", "coasts", "lakes", "islands"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Ocean views", "Granite peaks", "Carriage roads"]
    },
    {
        "id": "yosemite", "name": "Yosemite National Park", "type": "National Park", "location": "California, USA",
        "address": "9035 Village Dr, Yosemite Valley, CA 95389", "latitude": 37.8651, "longitude": -119.5383, "region": "North America",
        "description": "Giant sequoia trees, El Capitan & Half Dome granite cliffs, stunning waterfalls.",
        "activities": ["hiking", "rock climbing", "photography", "wildlife watching", "camping", "waterfalls", "backpacking"],
        "scenery": ["mountains", "forests", "waterfalls", "valleys", "granite cliffs", "giant sequoias"],
        "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80",
        "rating": 4.9,
        "features": ["El Capitan", "Half Dome", "Yosemite Falls"]
    },
    {
        "id": "zion", "name": "Zion National Park", "type": "National Park", "location": "Utah, USA",
        "address": "1 Zion Park Blvd, Springdale, UT 84767", "latitude": 37.2982, "longitude": -113.0263, "region": "North America",
        "description": "Massive sandstone cliffs of cream, pink, and red. Challenging hikes like The Narrows.",
        "activities": ["hiking", "canyoning", "photography", "stargazing", "rock climbing", "backpacking"],
        "scenery": ["canyons", "rivers", "cliffs", "deserts", "slot canyons"],
        "image_url": "https://images.unsplash.com/photo-1500534314209-a25ddb2bd429?auto=format&fit=crop&w=800&q=80",
        "rating": 4.9,
        "features": ["The Narrows", "Angels Landing", "Sandstone cliffs"]
    },
    {
        "id": "yellowstone", "name": "Yellowstone National Park", "type": "National Park", "location": "Wyoming, USA", # Primary state
        "address": "2 Officers Row, Yellowstone National Park, WY 82190", "latitude": 44.4280, "longitude": -110.5885, "region": "North America",
        "description": "Geysers like Old Faithful, hot springs, diverse wildlife. A geothermal wonderland.",
        "activities": ["hiking", "wildlife watching", "geothermal viewing", "camping", "fishing", "photography"],
        "scenery": ["geysers", "hot springs", "mountains", "forests", "lakes", "wildlife", "caldera"],
        "image_url": "https://images.unsplash.com/photo-1502086223501-7ea6ecd79368?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Old Faithful", "Grand Prismatic Spring", "Wildlife"]
    },
    {
        "id": "grand_canyon", "name": "Grand Canyon National Park", "type": "National Park", "location": "Arizona, USA",
        "address": "S Entrance Rd, Grand Canyon Village, AZ 86023", "latitude": 36.0597, "longitude": -112.1119, "region": "North America",
        "description": "Mile-deep canyon carved by the Colorado River. Breathtaking views, challenging hikes.",
        "activities": ["hiking", "mule rides", "rafting", "photography", "stargazing", "helicopter tours"],
        "scenery": ["canyons", "rivers", "deserts", "geological formations", "sunrise/sunset views"],
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=800&q=80",
        "rating": 4.9,
        "features": ["South Rim", "Colorado River", "Sunset views"]
    },
    {
        "id": "everglades", "name": "Everglades National Park", "type": "National Park", "location": "Florida, USA",
        "address": "40001 State Road 9336, Homestead, FL 33034", "latitude": 25.2866, "longitude": -80.8987, "region": "North America",
        "description": "Vast wetland ecosystem with unique wildlife like alligators and manatees.",
        "activities": ["boating", "kayaking", "wildlife watching", "fishing", "hiking", "bird watching", "airboat tours"],
        "scenery": ["wetlands", "mangroves", "wildlife", "sawgrass prairies"],
        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "rating": 4.5,
        "features": ["Alligators", "Mangroves", "Airboat tours"]
    },
    {
        "id": "rocky_mountain", "name": "Rocky Mountain National Park", "type": "National Park", "location": "Colorado, USA",
        "address": "1000 US Hwy 36, Estes Park, CO 80517", "latitude": 40.3428, "longitude": -105.6836, "region": "North America",
        "description": "Majestic mountain views, diverse wildlife, Trail Ridge Road.",
        "activities": ["hiking", "wildlife watching", "scenic driving", "fishing", "camping", "mountaineering", "snowshoeing"],
        "scenery": ["mountains", "alpine tundra", "forests", "lakes", "wildlife"],
        "image_url": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Trail Ridge Road", "Alpine lakes", "Wildlife"]
    },
    {
        "id": "lincoln_memorial", "name": "Lincoln Memorial", "type": "National Memorial", "location": "Washington D.C., USA",
        "address": "2 Lincoln Memorial Cir NW, Washington, DC 20037", "latitude": 38.8893, "longitude": -77.0502, "region": "North America",
        "description": "Iconic American monument honoring Abraham Lincoln.",
        "activities": ["sightseeing", "photography", "history learning"],
        "scenery": ["monuments", "city views", "reflecting pool"],
        "image_url": "https://upload.wikimedia.org/wikipedia/commons/6/6e/Lincoln_Memorial_%28Lincoln_Memorial_Reflecting_Pool%29.jpg",
        "rating": 4.7,
        "features": ["Reflecting Pool", "Statue of Lincoln", "Historic speeches"]
    },
    {
        "id": "mount_rushmore", "name": "Mount Rushmore National Memorial", "type": "National Memorial", "location": "South Dakota, USA",
        "address": "13000 SD-244, Keystone, SD 57751", "latitude": 43.8791, "longitude": -103.4591, "region": "North America",
        "description": "Colossal sculptures of four U.S. presidents.",
        "activities": ["sightseeing", "photography", "history learning", "hiking"],
        "scenery": ["mountains", "sculptures", "forests"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.6,
        "features": ["Presidential carvings", "Visitor center", "Scenic views"]
    },

    # New International and Diverse Landmarks
    {
        "id": "plitvice_lakes", "name": "Plitvice Lakes National Park", "type": "National Park", "location": "Croatia",
        "address": "Plitvička Jezera, Croatia", "latitude": 44.8653, "longitude": 15.5820, "region": "Europe",
        "description": "Chain of 16 terraced lakes joined by waterfalls in a limestone canyon.",
        "activities": ["hiking", "photography", "boating", "waterfalls viewing"],
        "scenery": ["lakes", "waterfalls", "forests", "canyons"],
        "image_url": "https://images.unsplash.com/photo-1570395198008-050700a8f894?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Terraced lakes", "Waterfalls", "Limestone canyon"]
    },
    {
        "id": "uluru_kata_tjuta", "name": "Uluru-Kata Tjuta National Park", "type": "National Park", "location": "Northern Territory, Australia",
        "address": "Uluru Rd, Uluru NT 0872, Australia", "latitude": -25.3444, "longitude": 131.0369, "region": "Australia/Oceania",
        "description": "Home to Uluru (Ayers Rock) and Kata Tjuta (The Olgas). Sacred to Indigenous Australians.",
        "activities": ["cultural tours", "hiking", "stargazing", "sunrise/sunset views", "photography"],
        "scenery": ["deserts", "rock formations", "cultural sites"],
        "image_url": "https://images.unsplash.com/photo-1547309984-09e7128f03ca?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Uluru", "Kata Tjuta", "Cultural significance"]
    },
    {
        "id": "banff", "name": "Banff National Park", "type": "National Park", "location": "Alberta, Canada",
        "address": "Banff, AB T1L 1K2, Canada", "latitude": 51.4968, "longitude": -115.9281, "region": "North America",
        "description": "Canada's oldest national park, with Rocky Mountain peaks, turquoise glacial lakes, and abundant wildlife.",
        "activities": ["hiking", "skiing", "canoeing", "wildlife watching", "scenic driving", "photography"],
        "scenery": ["mountains", "glaciers", "lakes", "forests", "hot springs"],
        "image_url": "https://images.unsplash.com/photo-1503614472-8c93d56e92ce?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Rocky Mountain peaks", "Glacial lakes", "Wildlife"]
    },
    {
        "id": "machu_picchu", "name": "Machu Picchu", "type": "UNESCO World Heritage Site", "location": "Cusco Region, Peru",
        "address": "Machu Picchu, Peru", "latitude": -13.1631, "longitude": -72.5450, "region": "South America",
        "description": "Ancient Inca city set high in the Andes Mountains. Renowned for its sophisticated dry-stone walls.",
        "activities": ["archaeology", "hiking", "history learning", "photography", "spiritual exploration"],
        "scenery": ["mountains", "ruins", "cloud forests", "valleys"],
        "image_url": "https://images.unsplash.com/photo-1526745925052-dd824d27b9ab?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Inca ruins", "Andes Mountains", "Dry-stone walls"]
    },
    {
        "id": "serengeti", "name": "Serengeti National Park", "type": "National Park", "location": "Tanzania",
        "address": "Serengeti, Tanzania", "latitude": -2.3333, "longitude": 34.8333, "region": "Africa",
        "description": "Famous for its annual wildebeest migration, vast plains, and high concentration of predators.",
        "activities": ["safari", "wildlife watching", "photography", "hot air ballooning", "cultural visits"],
        "scenery": ["savannah", "wildlife", "acacia trees", "riverine forests"],
        "image_url": "https://images.unsplash.com/photo-1534001803993-75071f110f85?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Wildebeest migration", "Vast plains", "Predators"]
    },
    {
        "id": "great_barrier_reef", "name": "Great Barrier Reef", "type": "UNESCO World Heritage Site", "location": "Queensland, Australia",
        "address": "Off the coast of Queensland, Australia", "latitude": -18.2871, "longitude": 147.6992, "region": "Australia/Oceania",
        "description": "World's largest coral reef system, composed of over 2,900 individual reefs and 900 islands.",
        "activities": ["snorkeling", "diving", "boating", "marine biology", "scenic flights"],
        "scenery": ["coral reefs", "marine life", "islands", "ocean"],
        "image_url": "https://images.unsplash.com/photo-1610632897825-1eb11b43911c?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.7,
        "features": ["Coral reefs", "Marine life", "Scenic flights"]
    },
    {
        "id": "eiffel_tower", "name": "Eiffel Tower", "type": "Historic Landmark", "location": "Paris, France",
        "address": "Champ de Mars, 5 Av. Anatole France, 75007 Paris, France", "latitude": 48.8584, "longitude": 2.2945, "region": "Europe",
        "description": "Iconic wrought-iron lattice tower on the Champ de Mars in Paris.",
        "activities": ["sightseeing", "photography", "city views", "dining"],
        "scenery": ["cityscape", "architecture", "river seine"],
        "image_url": "https://images.unsplash.com/photo-1500217053999-aa7570a6d352?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Iconic structure", "City views", "Dining"]
    },
    {
        "id": "colosseum", "name": "Colosseum", "type": "Historic Landmark", "location": "Rome, Italy",
        "address": "Piazza del Colosseo, 1, 00184 Roma RM, Italy", "latitude": 41.8902, "longitude": 12.4922, "region": "Europe",
        "description": "Ancient Roman amphitheater, an iconic symbol of Imperial Rome.",
        "activities": ["history learning", "archaeology", "sightseeing", "photography"],
        "scenery": ["ruins", "historic architecture", "roman forum"],
        "image_url": "https://images.unsplash.com/photo-1552832230-c0197dd311b5?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.7,
        "features": ["Roman architecture", "Amphitheater", "Historic significance"]
    },
    {
        "id": "taj_mahal", "name": "Taj Mahal", "type": "UNESCO World Heritage Site", "location": "Agra, India",
        "address": "Dharmapuri, Forest Colony, Tajganj, Agra, Uttar Pradesh 282001, India", "latitude": 27.1751, "longitude": 78.0421, "region": "Asia",
        "description": "Ivory-white marble mausoleum on the south bank of the Yamuna river. A monument of love.",
        "activities": ["sightseeing", "history learning", "architecture appreciation", "photography"],
        "scenery": ["mausoleum", "gardens", "mughal architecture", "reflection pool"],
        "image_url": "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Marble mausoleum", "Gardens", "Reflection pool"]
    },
    {
        "id": "great_wall_china", "name": "Great Wall of China", "type": "UNESCO World Heritage Site", "location": "China",
        "address": "Various sections, e.g., Badaling, Mutianyu near Beijing", "latitude": 40.4319, "longitude": 116.5704, "region": "Asia", # Coordinates for Mutianyu section
        "description": "Series of fortifications made of stone, brick, tamped earth, wood, and other materials.",
        "activities": ["hiking", "history learning", "photography", "scenic views"],
        "scenery": ["mountains", "fortifications", "historic architecture", "countryside"],
        "image_url": "https://images.unsplash.com/photo-1507799018044-3c7c9c9f0bcd?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.7,
        "features": ["Historic fortifications", "Scenic views", "Cultural significance"]
    },
    {
        "id": "pyramids_giza", "name": "Pyramids of Giza", "type": "UNESCO World Heritage Site", "location": "Giza, Egypt",
        "address": "Al Haram, Giza Governorate, Egypt", "latitude": 29.9792, "longitude": 31.1342, "region": "Africa",
        "description": "The Giza pyramid complex, includes the Great Pyramid, Pyramid of Khafre, and Pyramid of Menkaure, along with the Great Sphinx.",
        "activities": ["archaeology", "history learning", "sightseeing", "camel riding", "photography"],
        "scenery": ["pyramids", "sphinx", "desert", "ancient civilization"],
        "image_url": "https://images.unsplash.com/photo-1572094304400-b9c170344692?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Great Pyramid", "Sphinx", "Ancient civilization"]
    },
    {
        "id": "petra", "name": "Petra", "type": "UNESCO World Heritage Site", "location": "Jordan",
        "address": "Petra, Jordan", "latitude": 30.3285, "longitude": 35.4444, "region": "Asia", # Middle East is part of Asia
        "description": "Ancient Nabatean city carved into rose-red sandstone cliffs. Famous for Al-Khazneh (The Treasury).",
        "activities": ["archaeology", "hiking", "history learning", "photography", "horseback riding"],
        "scenery": ["canyons", "rock-cut architecture", "desert", "ruins"],
        "image_url": "https://images.unsplash.com/photo-1580030569959-526959c99585?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Al-Khazneh", "Rock-cut architecture", "Desert canyons"]
    },
    {
        "id": "angkor_wat", "name": "Angkor Wat", "type": "UNESCO World Heritage Site", "location": "Siem Reap, Cambodia",
        "address": "Krong Siem Reap, Cambodia", "latitude": 13.4125, "longitude": 103.8660, "region": "Asia",
        "description": "Largest religious monument in the world, originally a Hindu temple dedicated to Vishnu, gradually transformed into a Buddhist temple.",
        "activities": ["archaeology", "history learning", "temple exploration", "photography", "sunrise views"],
        "scenery": ["temples", "ruins", "bas-reliefs", "moats", "forests"],
        "image_url": "https://images.unsplash.com/photo-1528181304800-259b08848526?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Temples", "Bas-reliefs", "Moats"]
    },
    {
        "id": "stonehenge", "name": "Stonehenge", "type": "UNESCO World Heritage Site", "location": "Wiltshire, England",
        "address": "Salisbury SP4 7DE, United Kingdom", "latitude": 51.1789, "longitude": -1.8262, "region": "Europe",
        "description": "Prehistoric monument featuring a ring of standing stones, set within earthworks.",
        "activities": ["archaeology", "history learning", "mysticism", "photography"],
        "scenery": ["megalithic structures", "plains", "ancient mystery"],
        "image_url": "https://images.unsplash.com/photo-1548303549-37e17a1b0d52?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.5,
        "features": ["Standing stones", "Ancient mystery", "Plains"]
    },
    {
        "id": "galapagos", "name": "Galápagos Islands", "type": "National Park & UNESCO Site", "location": "Ecuador",
        "address": "Galápagos Islands, Ecuador", "latitude": -0.9538, "longitude": -90.9656, "region": "South America",
        "description": "Volcanic archipelago renowned for its unique fearless wildlife, studied by Charles Darwin.",
        "activities": ["wildlife watching", "snorkeling", "diving", "boating", "evolutionary studies"],
        "scenery": ["islands", "volcanic landscapes", "unique fauna", "marine life", "beaches"],
        "image_url": "https://images.unsplash.com/photo-1531890412038-6c40e059079f?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Unique wildlife", "Volcanic landscapes", "Marine life"]
    },
    {
        "id": "mount_fuji", "name": "Mount Fuji", "type": "UNESCO World Heritage Site", "location": "Honshu, Japan",
        "address": "Kitayama, Fujinomiya, Shizuoka 418-0112, Japan", "latitude": 35.3606, "longitude": 138.7274, "region": "Asia",
        "description": "Japan's tallest peak, an active stratovolcano and iconic symbol of the country.",
        "activities": ["hiking", "mountaineering", "photography", "cultural significance", "scenic views"],
        "scenery": ["volcano", "mountains", "lakes", "snow-capped peak", "forests"],
        "image_url": "https://images.unsplash.com/photo-1578271887552-5ac3a72752bc?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Stratovolcano", "Snow-capped peak", "Cultural significance"]
    },
    {
        "id": "victoria_falls", "name": "Victoria Falls", "type": "UNESCO World Heritage Site", "location": "Zambia/Zimbabwe Border",
        "address": "Mosi-o-Tunya Road, Livingstone, Zambia", "latitude": -17.9243, "longitude": 25.8572, "region": "Africa",
        "description": "One of the world's largest waterfalls, known locally as 'The Smoke that Thunders'.",
        "activities": ["sightseeing", "rafting", "bungee jumping", "wildlife viewing", "photography"],
        "scenery": ["waterfalls", "gorges", "rainforest", "mist", "river"],
        "image_url": "https://images.unsplash.com/photo-1581701778934-2b991658a79b?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Waterfalls", "Gorges", "Rainforest"]
    },
    {
        "id": "ha_long_bay", "name": "Hạ Long Bay", "type": "UNESCO World Heritage Site", "location": "Quảng Ninh Province, Vietnam",
        "address": "Hạ Long Bay, Vietnam", "latitude": 20.9101, "longitude": 107.1839, "region": "Asia",
        "description": "Thousands of limestone karsts and isles in various shapes and sizes. Emerald waters and stunning caves.",
        "activities": ["boating", "kayaking", "cave exploration", "swimming", "photography"],
        "scenery": ["karst islands", "emerald waters", "caves", "floating villages"],
        "image_url": "https://images.unsplash.com/photo-1548032885-b5e38734688a?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.7,
        "features": ["Limestone karsts", "Emerald waters", "Caves"]
    },
    {
        "id": "kilimanjaro", "name": "Mount Kilimanjaro", "type": "National Park & UNESCO Site", "location": "Tanzania",
        "address": "Mount Kilimanjaro National Park, Tanzania", "latitude": -3.0674, "longitude": 37.3556, "region": "Africa",
        "description": "Africa's highest peak and the world's tallest free-standing mountain. A dormant volcano.",
        "activities": ["mountaineering", "hiking", "trekking", "cultural experiences"],
        "scenery": ["mountains", "glaciers", "alpine desert", "rainforest", "summit views"],
        "image_url": "https://images.unsplash.com/photo-1589391879625-b7349700b926?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Highest peak in Africa", "Glaciers", "Summit views"]
    },
    {
        "id": "chichen_itza", "name": "Chichen Itza", "type": "UNESCO World Heritage Site", "location": "Yucatán Peninsula, Mexico",
        "address": "Chichen Itza, Yucatan, Mexico", "latitude": 20.6843, "longitude": -88.5678, "region": "North America",
        "description": "Large pre-Columbian city built by the Maya people. Features El Castillo pyramid.",
        "activities": ["archaeology", "history learning", "Mayan culture", "photography"],
        "scenery": ["pyramids", "temples", "ruins", "cenotes (nearby)"],
        "image_url": "https://images.unsplash.com/photo-1511910293148-3706f2729753?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.7,
        "features": ["El Castillo pyramid", "Mayan ruins", "Cenotes"]
    },
    {
        "id": "santorini", "name": "Santorini", "type": "Island Destination", "location": "Cyclades, Greece",
        "address": "Santorini, Greece", "latitude": 36.3932, "longitude": 25.4615, "region": "Europe",
        "description": "Volcanic island known for its dramatic views, stunning sunsets from Oia town, and white-washed houses.",
        "activities": ["sightseeing", "sunsets", "boating", "wine tasting", "beach relaxation", "photography"],
        "scenery": ["caldera", "volcanic islands", "white villages", "blue-domed churches", "aegean sea"],
        "image_url": "https://images.unsplash.com/photo-1573096101305-79701b74a6f0?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Dramatic views", "Sunsets", "White-washed houses"]
    },
    {
        "id": "bora_bora", "name": "Bora Bora", "type": "Island Destination", "location": "French Polynesia",
        "address": "Bora Bora, French Polynesia", "latitude": -16.5004, "longitude": -151.7415, "region": "Australia/Oceania",
        "description": "South Pacific island known for its turquoise lagoon, luxury resorts, and overwater bungalows.",
        "activities": ["snorkeling", "diving", "luxury travel", "boating", "beach relaxation", "watersports"],
        "scenery": ["lagoon", "coral reefs", "volcanic peaks", "overwater bungalows", "tropical paradise"],
        "image_url": "https://images.unsplash.com/photo-1506953823076-075a7c0339a1?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Turquoise lagoon", "Luxury resorts", "Overwater bungalows"]
    },
    {
        "id": "death_valley", "name": "Death Valley National Park", "type": "National Park", "location": "California/Nevada, USA",
        "address": "Death Valley, CA 92328", "latitude": 36.5054, "longitude": -117.0794, "region": "North America",
        "description": "Hottest, driest, and lowest national park. A land of extremes with stunning desert landscapes.",
        "activities": ["hiking", "stargazing", "photography", "geology", "scenic driving"],
        "scenery": ["deserts", "badlands", "salt flats", "canyons", "sand dunes", "mountains"],
        "image_url": "https://images.unsplash.com/photo-1541700345680-c2e0f1f392c3?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.6,
        "features": ["Desert landscapes", "Badlands", "Salt flats"]
    },
    {
        "id": "statue_of_liberty", "name": "Statue of Liberty National Monument", "type": "National Monument", "location": "New York Harbor, USA",
        "address": "New York, NY 10004", "latitude": 40.6892, "longitude": -74.0445, "region": "North America",
        "description": "Colossal neoclassical sculpture on Liberty Island. A symbol of freedom and democracy.",
        "activities": ["sightseeing", "history learning", "ferry ride", "museum visit", "photography"],
        "scenery": ["statue", "skyline views", "harbor", "island"],
        "image_url": "https://images.unsplash.com/photo-1544017109-28d089900c84?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.7,
        "features": ["Symbol of freedom", "Skyline views", "Museum"]
    },
    {
        "id": "neuschwanstein_castle", "name": "Neuschwanstein Castle", "type": "Historic Landmark", "location": "Bavaria, Germany",
        "address": "Neuschwansteinstraße 20, 87645 Schwangau, Germany", "latitude": 47.5576, "longitude": 10.7498, "region": "Europe",
        "description": "Nineteenth-century Romanesque Revival palace on a rugged hill. The inspiration for Disney's Sleeping Beauty Castle.",
        "activities": ["castle tour", "history learning", "photography", "hiking (around)"],
        "scenery": ["castle", "mountains", "forests", "lakes (nearby)", "fairytale architecture"],
        "image_url": "https://images.unsplash.com/photo-1567596683154-591dc5176027?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Fairytale architecture", "Mountain views", "Historic significance"]
    },
    {
        "id": "sydney_opera_house", "name": "Sydney Opera House", "type": "UNESCO World Heritage Site", "location": "Sydney, Australia",
        "address": "Bennelong Point, Sydney NSW 2000, Australia", "latitude": -33.8568, "longitude": 151.2153, "region": "Australia/Oceania",
        "description": "Multi-venue performing arts centre. One of the 20th century's most famous and distinctive buildings.",
        "activities": ["performance attendance", "architecture tour", "photography", "dining", "harbour views"],
        "scenery": ["architecture", "harbour", "cityscape", "sydney harbour bridge"],
        "image_url": "https://images.unsplash.com/photo-1523059623039-a6ed04734213?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Iconic architecture", "Performing arts", "Harbour views"]
    },
    {
        "id": "torres_del_paine", "name": "Torres del Paine National Park", "type": "National Park", "location": "Patagonia, Chile",
        "address": "Torres del Paine, Magallanes Region, Chile", "latitude": -50.9425, "longitude": -72.9739, "region": "South America",
        "description": "Known for its soaring mountains, bright blue icebergs, and grasslands that shelter rare wildlife like guanacos.",
        "activities": ["hiking", "trekking", "mountaineering", "wildlife watching", "photography", "glacier viewing"],
        "scenery": ["mountains", "granite peaks", "glaciers", "lakes", "rivers", "pampas"],
        "image_url": "https://images.unsplash.com/photo-1564020429170-551900160975?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Granite peaks", "Glaciers", "Wildlife"]
    },
    {
        "id": "fiordland", "name": "Fiordland National Park", "type": "National Park", "location": "South Island, New Zealand",
        "address": "Fiordland National Park, Southland, New Zealand", "latitude": -45.4164, "longitude": 167.7160, "region": "Australia/Oceania",
        "description": "Known for the glacier-carved fiords of Milford and Doubtful Sounds. Rainforests, mountains, and waterfalls.",
        "activities": ["hiking", "boating", "kayaking", "wildlife watching", "scenic flights", "photography"],
        "scenery": ["fiords", "mountains", "rainforests", "waterfalls", "lakes", "marine life"],
        "image_url": "https://images.unsplash.com/photo-1591207960001-ba1a793108a9?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Glacier-carved fiords", "Rainforests", "Waterfalls"]
    },
    {
        "id": "iguazu_falls", "name": "Iguazu Falls", "type": "UNESCO World Heritage Site", "location": "Argentina/Brazil Border",
        "address": "Puerto Iguazú, Misiones Province, Argentina", "latitude": -25.6953, "longitude": -54.4367, "region": "South America",
        "description": "System of hundreds of waterfalls stretching for 2.7 km. Taller than Niagara Falls, twice as wide.",
        "activities": ["sightseeing", "boating (under falls)", "hiking", "wildlife viewing", "photography"],
        "scenery": ["waterfalls", "rainforest", "river", "wildlife", "mist"],
        "image_url": "https://images.unsplash.com/photo-1592920053728-91749a4a3c4c?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Hundreds of waterfalls", "Rainforest", "Wildlife"]
    },
    {
        "id": "arches", "name": "Arches National Park", "type": "National Park", "location": "Utah, USA",
        "address": "Arches National Park, Moab, UT 84532", "latitude": 38.7331, "longitude": -109.5925, "region": "North America",
        "description": "Over 2,000 natural stone arch formations in the high desert of Utah. Address: Arches National Park, Moab, UT 84532.",
        "activities": ["hiking", "photography", "stargazing", "rock climbing"],
        "scenery": ["arches", "desert", "rock formations"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Delicate Arch", "Balanced Rock", "Fiery Furnace"]
    },
    {
        "id": "kruger", "name": "Kruger National Park", "type": "National Park", "location": "South Africa",
        "address": "Kruger National Park, South Africa", "latitude": -23.9884, "longitude": 31.5547, "region": "Africa",
        "description": "One of Africa's largest game reserves. Address: Kruger National Park, South Africa.",
        "activities": ["safari", "wildlife watching", "photography", "bird watching"],
        "scenery": ["savannah", "rivers", "bushveld"],
        "image_url": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=800&q=80",
        "rating": 4.9,
        "features": ["Big Five", "Game drives", "Birdlife"]
    },
    {
        "id": "table_mountain", "name": "Table Mountain National Park", "type": "National Park", "location": "Cape Town, South Africa",
        "address": "Table Mountain, Cape Town, South Africa", "latitude": -33.9628, "longitude": 18.4098, "region": "Africa",
        "description": "Iconic flat-topped mountain overlooking Cape Town. Address: Table Mountain, Cape Town, South Africa.",
        "activities": ["hiking", "cable car", "photography", "rock climbing"],
        "scenery": ["mountains", "city views", "ocean"],
        "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Tabletop summit", "Cableway", "Panoramic views"]
    },
    {
        "id": "cinque_terre", "name": "Cinque Terre National Park", "type": "National Park", "location": "Liguria, Italy",
        "address": "Cinque Terre, Liguria, Italy", "latitude": 44.1277, "longitude": 9.7096, "region": "Europe",
        "description": "Five colorful seaside villages on the rugged Italian Riviera. Address: Cinque Terre, Liguria, Italy.",
        "activities": ["hiking", "swimming", "photography", "boating"],
        "scenery": ["cliffs", "villages", "sea"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Colorful villages", "Coastal trails", "Sea views"]
    },
    {
        "id": "toronto_islands", "name": "Toronto Islands Park", "type": "Urban Park", "location": "Toronto, Canada",
        "address": "Toronto Islands, Toronto, ON, Canada", "latitude": 43.6205, "longitude": -79.3781, "region": "North America",
        "description": "A chain of small islands in Lake Ontario, just offshore from Toronto. Address: Toronto Islands, Toronto, ON, Canada.",
        "activities": ["biking", "beach", "kayaking", "picnicking"],
        "scenery": ["islands", "city views", "beaches"],
        "image_url": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
        "rating": 4.6,
        "features": ["Beaches", "Bike paths", "Toronto skyline"]
    },
    {
        "id": "keukenhof", "name": "Keukenhof Gardens", "type": "Botanical Garden", "location": "Lisse, Netherlands",
        "address": "Stationsweg 166A, 2161 AM Lisse, Netherlands", "latitude": 52.2711, "longitude": 4.5461, "region": "Europe",
        "description": "World-famous tulip gardens open in spring. Address: Stationsweg 166A, 2161 AM Lisse, Netherlands.",
        "activities": ["walking", "photography", "flower viewing"],
        "scenery": ["gardens", "flowers", "lakes"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Tulip fields", "Spring blooms", "Windmills"]
    },
    {
        "id": "bryce_canyon", "name": "Bryce Canyon National Park", "type": "National Park", "location": "Utah, USA",
        "address": "Bryce Canyon National Park, UT 84764", "latitude": 37.5930, "longitude": -112.1871, "region": "North America",
        "description": "Known for its crimson-colored hoodoos, spire-shaped rock formations. Address: Bryce Canyon National Park, UT 84764.",
        "activities": ["hiking", "photography", "stargazing"],
        "scenery": ["hoodoos", "canyons", "forests"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Hoodoos", "Bryce Amphitheater", "Night skies"]
    },
    {
        "id": "sagarmatha", "name": "Sagarmatha National Park", "type": "National Park", "location": "Nepal",
        "address": "Sagarmatha National Park, Khumjung 56000, Nepal", "latitude": 27.9333, "longitude": 86.7167, "region": "Asia",
        "description": "Home to Mount Everest and Sherpa culture. Address: Sagarmatha National Park, Khumjung 56000, Nepal.",
        "activities": ["trekking", "mountaineering", "wildlife watching"],
        "scenery": ["mountains", "glaciers", "forests"],
        "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80",
        "rating": 4.9,
        "features": ["Mount Everest", "Sherpa villages", "Himalayan wildlife"]
    },
    {
        "id": "central_park", "name": "Central Park", "type": "Urban Park", "location": "New York, USA",
        "address": "Central Park, New York, NY 10024", "latitude": 40.7851, "longitude": -73.9683, "region": "North America",
        "description": "Iconic urban park in Manhattan. Address: Central Park, New York, NY 10024.",
        "activities": ["walking", "biking", "boating", "picnicking"],
        "scenery": ["lawns", "lakes", "city views"],
        "image_url": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Great Lawn", "Bow Bridge", "Bethesda Fountain"]
    },
    {
        "id": "wilsons_prom", "name": "Wilsons Promontory National Park", "type": "National Park", "location": "Victoria, Australia",
        "address": "Wilsons Promontory Rd, Yanakie VIC 3960, Australia", "latitude": -39.0300, "longitude": 146.3200, "region": "Australia/Oceania",
        "description": "Southernmost tip of mainland Australia, known for beaches and wildlife. Address: Wilsons Promontory Rd, Yanakie VIC 3960, Australia.",
        "activities": ["hiking", "beach", "wildlife watching", "camping"],
        "scenery": ["beaches", "forests", "mountains"],
        "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Squeaky Beach", "Wildlife", "Granite mountains"]
    },
    {
        "id": "guilin", "name": "Guilin and Lijiang River National Park", "type": "National Park", "location": "Guangxi, China",
        "address": "Guilin, Guangxi, China", "latitude": 25.2736, "longitude": 110.2900, "region": "Asia",
        "description": "Famous for its dramatic karst mountain landscape and scenic river cruises. Address: Guilin, Guangxi, China.",
        "activities": ["boating", "photography", "hiking", "sightseeing"],
        "scenery": ["karst mountains", "river", "villages"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Karst peaks", "River cruises", "Scenic villages"]
    },
    {
        "id": "plaza_de_armas", "name": "Plaza de Armas", "type": "Historic Landmark", "location": "Cusco, Peru",
        "address": "Plaza de Armas, Cusco, Peru", "latitude": -13.5167, "longitude": -71.9781, "region": "South America",
        "description": "Historic city square surrounded by colonial architecture and Inca ruins. Address: Plaza de Armas, Cusco, Peru.",
        "activities": ["walking", "history learning", "photography", "cultural tours"],
        "scenery": ["plaza", "cathedrals", "mountains"],
        "image_url": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
        "rating": 4.6,
        "features": ["Colonial architecture", "Inca ruins", "Cultural events"]
    },
    {
        "id": "tikal", "name": "Tikal National Park", "type": "UNESCO World Heritage Site", "location": "Petén, Guatemala",
        "address": "Tikal, Petén, Guatemala", "latitude": 17.2220, "longitude": -89.6237, "region": "North America",
        "description": "Ancient Mayan city with towering temples in the rainforest. Address: Tikal, Petén, Guatemala.",
        "activities": ["archaeology", "hiking", "wildlife watching", "photography"],
        "scenery": ["ruins", "rainforest", "temples"],
        "image_url": "https://images.unsplash.com/photo-1511910293148-3706f2729753?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Mayan temples", "Rainforest wildlife", "Ancient city"]
    },
    {
        "id": "yala", "name": "Yala National Park", "type": "National Park", "location": "Sri Lanka",
        "address": "Yala National Park, Sri Lanka", "latitude": 6.3667, "longitude": 81.5167, "region": "Asia",
        "description": "Renowned for its leopards, elephants, and diverse birdlife. Address: Yala National Park, Sri Lanka.",
        "activities": ["safari", "wildlife watching", "photography", "bird watching"],
        "scenery": ["jungles", "lagoons", "grasslands"],
        "image_url": "https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Leopards", "Elephants", "Birdlife"]
    },
    {
        "id": "torres_stirling", "name": "Stirling Range National Park", "type": "National Park", "location": "Western Australia, Australia",
        "address": "Stirling Range National Park, WA 6338, Australia", "latitude": -34.4250, "longitude": 118.1167, "region": "Australia/Oceania",
        "description": "Mountain range known for wildflowers and hiking. Address: Stirling Range National Park, WA 6338, Australia.",
        "activities": ["hiking", "wildflower viewing", "photography", "bird watching"],
        "scenery": ["mountains", "wildflowers", "forests"],
        "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80",
        "rating": 4.6,
        "features": ["Wildflowers", "Mountain hikes", "Birdlife"]
    },
    {
        "id": "fiery_furnace", "name": "Fiery Furnace", "type": "National Park Feature", "location": "Utah, USA",
        "address": "Arches National Park, Moab, UT 84532", "latitude": 38.7486, "longitude": -109.5547, "region": "North America",
        "description": "A labyrinth of narrow sandstone canyons and passages. Address: Arches National Park, Moab, UT 84532.",
        "activities": ["hiking", "photography", "guided tours"],
        "scenery": ["sandstone", "arches", "canyons"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Maze-like canyons", "Sandstone fins", "Guided hikes"]
    },
    {
        "id": "lake_bled", "name": "Lake Bled", "type": "Lake", "location": "Slovenia",
        "address": "Lake Bled, 4260 Bled, Slovenia", "latitude": 46.3625, "longitude": 14.0936, "region": "Europe",
        "description": "Picturesque lake with an island church and medieval castle. Address: Lake Bled, 4260 Bled, Slovenia.",
        "activities": ["boating", "swimming", "photography", "hiking"],
        "scenery": ["lake", "island", "castle"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Island church", "Bled Castle", "Rowboat rides"]
    },
    {
        "id": "table_rock", "name": "Table Rock State Park", "type": "State Park", "location": "South Carolina, USA",
        "address": "158 Ellison Ln, Pickens, SC 29671", "latitude": 35.0240, "longitude": -82.7074, "region": "North America",
        "description": "Mountain park with hiking trails and a scenic lake. Address: 158 Ellison Ln, Pickens, SC 29671.",
        "activities": ["hiking", "fishing", "camping", "boating"],
        "scenery": ["mountains", "lake", "forest"],
        "image_url": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
        "rating": 4.6,
        "features": ["Table Rock Mountain", "Lake Oolenoy", "Trails"]
    },
    {
        "id": "giant_causeway", "name": "Giant's Causeway", "type": "UNESCO World Heritage Site", "location": "Northern Ireland, UK",
        "address": "44 Causeway Rd, Bushmills BT57 8SU, UK", "latitude": 55.2408, "longitude": -6.5116, "region": "Europe",
        "description": "Famous for its unique hexagonal basalt columns. Address: 44 Causeway Rd, Bushmills BT57 8SU, UK.",
        "activities": ["walking", "photography", "nature study"],
        "scenery": ["basalt columns", "coast", "cliffs"],
        "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Basalt columns", "Coastal views", "Legendary site"]
    },

    # --- New Parks ---
    {
        "id": "jiuzhaigou",
        "name": "Jiuzhaigou Valley National Park",
        "type": "National Park",
        "location": "Sichuan, China",
        "address": "Jiuzhaigou, Sichuan, China",
        "latitude": 33.2521,
        "longitude": 103.9182,
        "region": "Asia",
        "description": "Famous for multi-level waterfalls, colorful lakes, and snow-capped peaks.",
        "activities": ["hiking", "photography", "nature watching"],
        "scenery": ["lakes", "waterfalls", "mountains", "forests"],
        "image_url": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Colorful lakes", "Waterfalls", "Snow-capped peaks"]
    },
    {
        "id": "cappadocia",
        "name": "Cappadocia",
        "type": "Historic Region",
        "location": "Turkey",
        "address": "Cappadocia, Turkey",
        "latitude": 38.6431,
        "longitude": 34.8270,
        "region": "Europe",
        "description": "Known for unique rock formations, cave dwellings, and hot air balloon rides.",
        "activities": ["hot air ballooning", "hiking", "photography"],
        "scenery": ["rock formations", "valleys", "caves"],
        "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80",
        "rating": 4.9,
        "features": ["Fairy chimneys", "Cave hotels", "Balloon rides"]
    },
    {
        "id": "banff_lake_louise",
        "name": "Lake Louise",
        "type": "Lake",
        "location": "Alberta, Canada",
        "address": "Lake Louise, AB, Canada",
        "latitude": 51.4254,
        "longitude": -116.1773,
        "region": "North America",
        "description": "Turquoise glacier-fed lake surrounded by high peaks and a famous chateau.",
        "activities": ["canoeing", "hiking", "skiing", "photography"],
        "scenery": ["lake", "mountains", "glaciers"],
        "image_url": "https://images.unsplash.com/photo-1501785888041-af3ef285b470?auto=format&fit=crop&w=800&q=80",
        "rating": 4.9,
        "features": ["Turquoise lake", "Mountain views", "Chateau"]
    },
    {
        "id": "tatra_national_park",
        "name": "Tatra National Park",
        "type": "National Park",
        "location": "Poland/Slovakia",
        "address": "Tatra Mountains, Poland/Slovakia",
        "latitude": 49.2296,
        "longitude": 20.0131,
        "region": "Europe",
        "description": "Alpine peaks, glacial lakes, and diverse wildlife in the Carpathians.",
        "activities": ["hiking", "climbing", "skiing", "wildlife watching"],
        "scenery": ["mountains", "lakes", "forests"],
        "image_url": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Alpine peaks", "Glacial lakes", "Wildlife"]
    },
    {
        "id": "plivice_lakes",
        "name": "Plitvice Lakes",
        "type": "National Park",
        "location": "Croatia",
        "address": "Plitvička Jezera, Croatia",
        "latitude": 44.8653,
        "longitude": 15.5820,
        "region": "Europe",
        "description": "16 terraced lakes joined by waterfalls, set in deep woodland.",
        "activities": ["hiking", "photography", "boating"],
        "scenery": ["lakes", "waterfalls", "forests"],
        "image_url": "https://images.unsplash.com/photo-1570395198008-050700a8f894?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.9,
        "features": ["Terraced lakes", "Waterfalls", "Woodland"]
    },
    {
        "id": "fiordland_milford",
        "name": "Milford Sound",
        "type": "Fiord",
        "location": "New Zealand",
        "address": "Milford Sound, New Zealand",
        "latitude": -44.6710,
        "longitude": 167.9240,
        "region": "Australia/Oceania",
        "description": "Dramatic fiord with towering peaks and waterfalls, accessible by boat.",
        "activities": ["boating", "kayaking", "hiking", "photography"],
        "scenery": ["fiord", "waterfalls", "mountains"],
        "image_url": "https://images.unsplash.com/photo-1591207960001-ba1a793108a9?q=80&w=1920&auto=format&fit=crop",
        "rating": 4.8,
        "features": ["Towering peaks", "Waterfalls", "Boat tours"]
    },
    {
        "id": "namib_naukluft",
        "name": "Namib-Naukluft National Park",
        "type": "National Park",
        "location": "Namibia",
        "address": "Namib Desert, Namibia",
        "latitude": -24.7710,
        "longitude": 15.2920,
        "region": "Africa",
        "description": "Vast desert park with towering dunes, unique wildlife, and surreal landscapes.",
        "activities": ["dune climbing", "photography", "wildlife watching"],
        "scenery": ["desert", "dunes", "mountains"],
        "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Sand dunes", "Desert landscapes", "Wildlife"]
    },
    {
        "id": "patagonia_fitzroy",
        "name": "Mount Fitz Roy",
        "type": "Mountain",
        "location": "Patagonia, Argentina",
        "address": "El Chaltén, Santa Cruz, Argentina",
        "latitude": -49.2728,
        "longitude": -73.0456,
        "region": "South America",
        "description": "Iconic jagged peak in the Andes, popular with trekkers and climbers.",
        "activities": ["trekking", "climbing", "photography"],
        "scenery": ["mountains", "glaciers", "lakes"],
        "image_url": "https://images.unsplash.com/photo-1511910293148-3706f2729753?auto=format&fit=crop&w=800&q=80",
        "rating": 4.8,
        "features": ["Jagged peaks", "Glaciers", "Trekking routes"]
    },
    {
        "id": "wilpena_pound",
        "name": "Wilpena Pound",
        "type": "Natural Amphitheatre",
        "location": "South Australia",
        "address": "Flinders Ranges, SA, Australia",
        "latitude": -31.5775,
        "longitude": 138.5950,
        "region": "Australia/Oceania",
        "description": "Huge natural amphitheatre of mountains in the heart of Flinders Ranges.",
        "activities": ["hiking", "scenic flights", "wildlife watching"],
        "scenery": ["mountains", "valleys", "wildlife"],
        "image_url": "https://images.unsplash.com/photo-1464983953574-0892a716854b?auto=format&fit=crop&w=800&q=80",
        "rating": 4.7,
        "features": ["Natural amphitheatre", "Mountain views", "Wildlife"]
    },
    {
        "id": "sarek_national_park",
        "name": "Sarek National Park",
        "type": "National Park",
        "location": "Sweden",
        "address": "Sarek National Park, Jokkmokk, Sweden",
        "latitude": 67.1670,
        "longitude": 17.7500,
        "region": "Europe",
        "description": "Remote wilderness with glaciers, wild rivers, and high peaks. No marked trails.",
        "activities": ["trekking", "mountaineering", "wildlife watching"],
        "scenery": ["mountains", "glaciers", "rivers"],
        "image_url": "https://images.unsplash.com/photo-1465101046530-73398c7f28ca?auto=format&fit=crop&w=800&q=80",
        "rating": 4.6,
        "features": ["Wilderness", "Glaciers", "Wild rivers"]
    },
]

AVAILABLE_ACTIVITIES = sorted(list(set(activity for park in PARKS_DATA for activity in park.get("activities", []))))
AVAILABLE_SCENERY = sorted(list(set(scenery_type for park in PARKS_DATA for scenery_type in park.get("scenery", []))))
AVAILABLE_REGIONS = sorted(list(set(park.get("region", "Other") for park in PARKS_DATA)))
AVAILABLE_PARK_TYPES = sorted(list(set(park.get("type", "Other") for park in PARKS_DATA)))