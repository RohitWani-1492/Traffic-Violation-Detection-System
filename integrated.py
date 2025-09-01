import cv2
from ultralytics import YOLO
from anpr2 import perform_ocr_on_image

# Load YOLO models
motorcycle_model = YOLO('weights/motorcycle.pt')  # Detects two-wheeler and triple-seat
helmet_model = YOLO('weights/helmet.pt')  # Helmet detection model
plate_model = YOLO('weights/best.pt')  # Number plate detection model

CONFIDENCE_THRESHOLD = 0.5  # Confidence threshold for helmet detection

violation_type_global=None

def detect_violations(frame):
    """
    Detects motorcycles, helmets, and number plates in a frame.
    Returns the modified frame with annotations.
    """
    motorcycle_results = motorcycle_model(frame)
    violation_detected = False
    detected_plate = None
    violation_type = "None"  # ✅ Initialize to avoid UnboundLocalError

    for result in motorcycle_results:
        boxes = result.boxes.xyxy
        classes = result.boxes.cls

        for box, cls in zip(boxes, classes):
            x1, y1, x2, y2 = map(int, box)
            label = "Two-Wheeler" if int(cls) == 0 else "Triple-Seat"
            color = (255, 165, 0) if int(cls) == 0 else (0, 0, 255)

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)

            motorcycle_region = frame[y1:y2, x1:x2]
            helmet_results = helmet_model(motorcycle_region)

            helmet_detected = False
            no_helmet_detected = False
            triple_riding_detected = int(cls) == 1  # ✅ Detect triple-seat

            # ✅ Draw helmet detection results
            for helmet_result in helmet_results:
                for helmet_box, helmet_class, confidence in zip(helmet_result.boxes.xyxy, helmet_result.boxes.cls, helmet_result.boxes.conf):
                    if confidence < CONFIDENCE_THRESHOLD:
                        continue

                    hx1, hy1, hx2, hy2 = map(int, helmet_box)
                    helmet_label = "Helmet" if int(helmet_class) == 0 else "No Helmet"
                    helmet_color = (0, 255, 0) if int(helmet_class) == 0 else (0, 0, 255)

                    cv2.rectangle(frame, (x1 + hx1, y1 + hy1), (x1 + hx2, y1 + hy2), helmet_color, 2)
                    cv2.putText(frame, helmet_label, (x1 + hx1, y1 + hy1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, helmet_color, 2)

                    if int(helmet_class) == 0:
                        helmet_detected = True
                    else:
                        no_helmet_detected = True

            # ✅ If no helmet OR triple riding, detect number plate
            if no_helmet_detected or triple_riding_detected:
                violation_detected = True
                plate_results = plate_model(motorcycle_region)
                violation_type = "No Helmet" if no_helmet_detected else "Triple Seat"
                global violation_type_global
                violation_type_global=violation_type

                for plate_result in plate_results:
                    for plate_box in plate_result.boxes.xyxy:
                        px1, py1, px2, py2 = map(int, plate_box)
                        detected_plate = frame[py1:py2, px1:px2]  # Extract number plate image region

                        cv2.rectangle(frame, (x1 + px1, y1 + py1), (x1 + px2, y1 + py2), (0, 255, 255), 2)

                        # ✅ Perform OCR and store violation
                        text_ocr = perform_ocr_on_image(frame, (x1 + px1, y1 + py1, x1 + px2, y1 + py2))
                        bg_x1, bg_y1 = x1 + px1, y1 + py1 - 35
                        bg_x2, bg_y2 = x1 + px1 + 200, y1 + py1
                        cv2.rectangle(frame, (bg_x1, bg_y1), (bg_x2, bg_y2), (0, 0, 0), -1)  # Black background for text

                        # ✅ Put white text on black background
                        cv2.putText(frame, text_ocr, (x1 + px1 + 5, y1 + py1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    return frame, violation_detected, detected_plate, violation_type

