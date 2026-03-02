import re
import easyocr
from config.settings import CONFIDENCE_MIN
from utils.plate_validator import clean_plate, is_valid_malaysian_plate
from utils.logger import logger

reader = easyocr.Reader(['en'])

def read_plates(cropped_frame):
    results = reader.readtext(cropped_frame)

    # Combine all high confidence detections
    combined = ""
    for (_, text, conf) in results:
        if conf > CONFIDENCE_MIN:
            part = re.sub(r'[^A-Z0-9 ]', '', text.upper()).strip()
            combined += " " + part if combined else part

    combined = combined.strip()
    logger.info(f"COMBINED: '{combined}'")

    # Append combined as extra result
    if combined and results:
        results.append((results[0][0], combined, 0.9))

    valid_plates = []
    for (bbox, text, confidence) in results:
        # logger.info(f"RAW: '{text}' | confidence: {confidence:.2f}")
        if confidence > CONFIDENCE_MIN:
            cleaned = clean_plate(text)
            if is_valid_malaysian_plate(cleaned):
                valid_plates.append((bbox, cleaned, confidence))

    return valid_plates