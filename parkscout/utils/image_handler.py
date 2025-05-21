import requests
from typing import Optional
import logging

logger = logging.getLogger(__name__)

PHOTO_APIS = [
    {
        "name": "Unsplash",
        "base_url": "https://api.unsplash.com/photos/random",
        "params": {
            "query": "{query}",
            "orientation": "landscape",
            "client_id": "YOUR_UNSPLASH_API_KEY"
        }
    },
    {
        "name": "Pexels",
        "base_url": "https://api.pexels.com/v1/search",
        "params": {
            "query": "{query}",
            "per_page": "1"
        }
    }
]

def get_fallback_image(landmark_name: str) -> Optional[str]:
    """Try multiple photo APIs to get a suitable fallback image."""
    search_query = f"{landmark_name} landmark scenic"
    
    # First try Unsplash
    try:
        response = requests.get(
            "https://source.unsplash.com/1600x900/?" + search_query.replace(" ", ",")
        )
        if response.status_code == 200:
            return response.url
    except Exception as e:
        logger.error(f"Unsplash fallback failed for {landmark_name}: {e}")

    # Then try direct image search
    try:
        response = requests.get(
            f"https://source.pexels.com/photos/search/{search_query.replace(' ', '-')}"
        )
        if response.status_code == 200:
            return response.url
    except Exception as e:
        logger.error(f"Pexels fallback failed for {landmark_name}: {e}")

    # Return None if all fallbacks fail
    return None
