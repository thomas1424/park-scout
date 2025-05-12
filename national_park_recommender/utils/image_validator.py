import requests
from PIL import Image
from io import BytesIO
import logging
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Tuple
from functools import lru_cache
import time

logger = logging.getLogger(__name__)

@lru_cache(maxsize=1000)
def validate_image_url(url: str) -> bool:
    """Validate if an image URL is accessible and returns a valid image."""
    try:
        response = requests.head(url, timeout=5)
        if response.status_code != 200:
            return False
        content_type = response.headers.get('content-type', '')
        return content_type.startswith('image/')
    except Exception as e:
        logger.error(f"Error validating image URL {url}: {e}")
        return False

def validate_google_image(url: str) -> bool:
    """Special validation for Google image URLs."""
    try:
        if "googleusercontent.com" in url:
            response = requests.head(url, timeout=5)
            return response.status_code == 200
        return False
    except Exception as e:
        logger.error(f"Error validating Google image URL {url}: {e}")
        return False

def download_and_verify_image(url: str) -> Tuple[bool, str]:
    """Download and verify image content."""
    try:
        response = requests.get(url, timeout=10)
        img = Image.open(BytesIO(response.content))
        # Verify image dimensions and format
        if img.size[0] < 100 or img.size[1] < 100:
            return False, "Image too small"
        return True, "OK"
    except Exception as e:
        return False, str(e)

def get_fallback_image_url(park_name: str, region: str = None) -> str:
    """Enhanced fallback system with region-specific searches."""
    search_query = f"{park_name} {region if region else ''} landscape mountain"
    
    # Try Unsplash first
    unsplash_url = f"https://source.unsplash.com/1600x900/?{search_query.replace(' ', ',')}"
    if validate_image_url(unsplash_url):
        return unsplash_url
        
    # Then try alternative sources
    return "/static/img/default-park.jpg"
