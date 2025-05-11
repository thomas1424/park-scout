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

def get_fallback_image_url(park_name: str, retries=3) -> str:
    """Get a fallback image URL with multiple sources and retries."""
    sources = [
        f"https://source.unsplash.com/1200x800/?{park_name},national-park",
        f"https://api.pexels.com/v1/search?query={park_name}+landscape&per_page=1",
        f"https://api.flickr.com/services/rest/?method=flickr.photos.search&text={park_name}+landscape"
    ]
    
    for _ in range(retries):
        for source in sources:
            try:
                if validate_image_url(source):
                    return source
                time.sleep(0.1)  # Rate limiting
            except Exception as e:
                logger.error(f"Error getting fallback image from {source}: {e}")
                continue
    
    return "/static/img/default-park.jpg"
