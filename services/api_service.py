import requests
from config.settings import LARAVEL_API_URL, LARAVEL_API_TOKEN, LARAVEL_ENABLED
from utils.logger import logger

def send_to_laravel(plate_number):
    headers = {}
    if not LARAVEL_ENABLED:
        logger.info(f"Laravel disabled. Skipping API call for: {plate_number}")
        return None

    try:
        response = requests.post(
            LARAVEL_API_URL,
            json={"plate_number": plate_number},
            headers={"Authorization": f"Bearer {LARAVEL_API_TOKEN}"},
            timeout=5
        )
        
        result = response.json()
        logger.info(f"Laravel response: {result}")
        return result

    except Exception as e:
        logger.error(f"Laravel API error: {e}")
        return None