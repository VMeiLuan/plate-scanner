import cv2
import json
import time
from config.settings import FRAME_SKIP, BUFFER_SIZE, NO_PLATE_TIMEOUT
from services.camera_service import open_camera, draw_header, draw_footer, draw_plate_box
from services.ocr_service import read_plates
from services.api_service import send_to_laravel
from utils.logger import logger

def main():
    # step 1: after get info from the QR code open check on the car number plate 


    # step 2: checking car number plate to make sure its align with the QR code
    cap = open_camera()
    if cap is None:
        return

    frame_count       = 0
    last_detected_plate = ""
    detected_plates   = []
    last_scan_time    = None
    candidate_buffer  = []

    logger.info("Camera started. Press 'Q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            logger.error("Failed to grab frame.")
            break

        frame_count += 1

        # ── Timeout check ─────────────────────────────────────
        no_plate_timeout = False
        if last_scan_time is not None:
            if (time.time() - last_scan_time) > NO_PLATE_TIMEOUT:
                no_plate_timeout = True

        draw_header(frame)

        # ── OCR every Nth frame ───────────────────────────────
        if frame_count % FRAME_SKIP == 0:
            height = frame.shape[0]
            cropped = frame[50:height - 50]

            valid_plates = read_plates(cropped)

            for (bbox, cleaned, confidence) in valid_plates:
                last_scan_time = time.time()

                draw_plate_box(frame, bbox, f"{cleaned} ({confidence:.0%})")

                candidate_buffer.append(cleaned)

                if len(candidate_buffer) >= BUFFER_SIZE:
                    best_plate = max(set(candidate_buffer), key=candidate_buffer.count)
                    candidate_buffer.clear()

                    last_in_list = detected_plates[-1] if detected_plates else None
                    logger.info(f"BUFFER RESULT: best='{best_plate}' | last='{last_in_list}'")

                    if best_plate != last_in_list:
                        output = {"plate_number": best_plate}
                        logger.info(json.dumps(output))
                        detected_plates.append(best_plate)
                        last_detected_plate = best_plate
                        last_scan_time = time.time()

                        # Send to Laravel (only if enabled in .env)
                        # print(f"sending to laravel...: {best_plate}")
                        send_to_laravel(best_plate)

        draw_footer(frame, last_detected_plate, no_plate_timeout)

        # ── Timeout transition ────────────────────────────────
        if no_plate_timeout and last_detected_plate:
            logger.info("No plate detected yet.")
            send_to_laravel("")
            last_detected_plate = ""
            last_scan_time = None
            detected_plates.clear()

        cv2.imshow("Plate Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            logger.info("System off.")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()