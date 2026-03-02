import re
from config.settings import PLATE_MIN_LENGTH, PLATE_MAX_LENGTH, PLATE_SPECIAL_MIN

def clean_plate(text):
    cleaned = re.sub(r'[^A-Z0-9 ]', '', text.upper())
    return cleaned.strip()

def is_valid_malaysian_plate(plate):
    plate_no_space = plate.replace(" ", "")

    if len(plate_no_space) < PLATE_MIN_LENGTH or len(plate_no_space) > PLATE_MAX_LENGTH:
        return False

    has_letters = any(c.isalpha() for c in plate_no_space)
    has_numbers = any(c.isdigit() for c in plate_no_space)

    # Normal plate — must have both letters and numbers
    if has_letters and has_numbers:
        return True

    # Special plate e.g. MADANI — letters only but long enough
    if has_letters and len(plate_no_space) >= PLATE_SPECIAL_MIN:
        return True

    return False