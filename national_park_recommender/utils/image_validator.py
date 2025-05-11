import requests
from PIL import Image
from io import BytesIO
import logging
import os
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)

def validate_image_url(url: str) -> bool:
    """Validate if an image URL is accessible and is a valid image."""
    try:
        response = requests.head(url, timeout=5)
        if response.status_code != 200:
            return False
            
        content_type = response.headers.get('content-type', '')
        if not content_type.startswith('image/'):
            return False
            
        return True
    except Exception as e:
        logger.error(f"Error validating image URL {url}: {e}")
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

def get_fallback_image_url(park_name: str) -> str:
    """Generate a fallback image URL using park name."""
    FALLBACK_SERVICES = [
        f"https://source.unsplash.com/1200x800/?{park_name},national-park",
        f"https://images.pexels.com/photos/search/{park_name}+national+park",
        f"https://api.flickr.com/services/rest/?method=flickr.photos.search&text={park_name}+national+park"
    ]
    
    for url in FALLBACK_SERVICES:
        if validate_image_url(url):
            return url
    
    return "static/img/default-park.jpg"
