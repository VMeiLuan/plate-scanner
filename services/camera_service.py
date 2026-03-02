import cv2
from config.settings import CAMERA_INDEX
from utils.logger import logger

def open_camera():
    cap = cv2.VideoCapture(CAMERA_INDEX)
    if not cap.isOpened():
        logger.error("Cannot open camera. Check your camera index.")
        return None
    logger.info("Camera opened successfully.")
    return cap

# interface header
def draw_header(frame):
    cv2.rectangle(frame, (0, 0), (frame.shape[1], 50), (0, 0, 0), -1)
    cv2.putText(frame, "PLATE SCANNER", (10, 33),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, "Press 'Q' to quit", (frame.shape[1] - 210, 33),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)

# interface footer
def draw_footer(frame, last_detected_plate, no_plate_timeout):
    footer_y = frame.shape[0] - 50
    cv2.rectangle(frame, (0, footer_y), (frame.shape[1], frame.shape[0]), (0, 0, 0), -1)

    if no_plate_timeout or not last_detected_plate:
        cv2.putText(frame, "No plate detected yet.", (10, footer_y + 33),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 165, 255), 2)
    else:
        cv2.putText(frame, f"{last_detected_plate}", (10, footer_y + 33),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

# scanner draw box
def draw_plate_box(frame, bbox, label):
    if bbox is not None:
        (tl, tr, br, bl) = bbox
        tl = (int(tl[0]), int(tl[1]) + 50)
        br = (int(br[0]), int(br[1]) + 50)
        cv2.rectangle(frame, tl, br, (0, 255, 0), 2)
        cv2.putText(frame, label, (tl[0], tl[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)