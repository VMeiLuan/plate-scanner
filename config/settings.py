import os
from dotenv import load_dotenv

load_dotenv()

# Camera
CAMERA_INDEX        = int(os.getenv("CAMERA_INDEX", 0))
FRAME_SKIP          = int(os.getenv("FRAME_SKIP", 5))

# OCR
BUFFER_SIZE         = int(os.getenv("BUFFER_SIZE", 3))
CONFIDENCE_MIN      = float(os.getenv("CONFIDENCE_MIN", 0.5))

# Plate
PLATE_MIN_LENGTH    = int(os.getenv("PLATE_MIN_LENGTH", 2))
PLATE_MAX_LENGTH    = int(os.getenv("PLATE_MAX_LENGTH", 11))
PLATE_SPECIAL_MIN   = int(os.getenv("PLATE_SPECIAL_MIN", 5))

# Timeout
NO_PLATE_TIMEOUT    = int(os.getenv("NO_PLATE_TIMEOUT", 3))

# Laravel API
LARAVEL_API_URL     = os.getenv("LARAVEL_API_URL", "")
LARAVEL_API_TOKEN   = os.getenv("LARAVEL_API_TOKEN", "")
LARAVEL_ENABLED     = os.getenv("LARAVEL_ENABLED", "false").lower() == "true"