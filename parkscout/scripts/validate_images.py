import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils import image_validator
from park_data import PARKS_DATA
import json
from concurrent.futures import ThreadPoolExecutor
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def validate_park_images():
    results = {'valid': [], 'invalid': []}
    
    def check_park(park):
        if 'image_url' not in park or not park['image_url']:
            logger.warning(f"No image URL for park: {park['name']}")
            return (park['id'], False)
            
        is_valid = image_validator.validate_image_url(park['image_url'])
        if not is_valid:
            logger.error(f"Invalid image for park: {park['name']}")
            # Try to get a fallback image
            fallback_url = image_validator.get_fallback_image_url(park['name'])
            if fallback_url != "static/img/default-park.jpg":
                park['image_url'] = fallback_url
                return (park['id'], True)
        return (park['id'], is_valid)

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(check_park, park) for park in PARKS_DATA]
        for future in futures:
            park_id, is_valid = future.result()
            if is_valid:
                results['valid'].append(park_id)
            else:
                results['invalid'].append(park_id)
    
    return results

if __name__ == '__main__':
    logger.info("Starting image validation...")
    results = validate_park_images()
    logger.info(f"Validation complete. Valid: {len(results['valid'])}, Invalid: {len(results['invalid'])}")
    
    with open('image_validation_results.json', 'w') as f:
        json.dump(results, f, indent=2)
