"""
Core plate detection logic for Car Plate Detection System.
Handles real-time license plate detection and OCR recognition.
"""

import cv2
from ultralytics import YOLO
from paddleocr import PaddleOCR
import numpy as np
import cvzone
import os
import sys

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.database_manager import manage_numberplate_db
from config.settings import (
    MODEL_PATH, CLASS_NAMES_PATH, TEST_VIDEO_PATH,
    VIDEO_RESIZE_WIDTH, VIDEO_RESIZE_HEIGHT, DETECTION_AREA,
    OCR_CONFIDENCE_THRESHOLD
)

os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'

class PlateDetector:
    """Main class for license plate detection and recognition."""
    
    def __init__(self):
        """Initialize the plate detector with OCR and YOLO model."""
        self.ocr = PaddleOCR()
        self.model = YOLO(MODEL_PATH)
        
        with open(CLASS_NAMES_PATH, "r") as f:
            self.class_names = f.read().splitlines()
    
    def perform_ocr(self, image_array):
        """
        Perform OCR on an image array to extract text and confidence.
        
        Args:
            image_array: Input image as numpy array
            
        Returns:
            tuple: (detected_text, confidence) or (None, 0) if no text found
        """
        if image_array is None:
            raise ValueError("Image is None")
        
        results = self.ocr.ocr(image_array, rec=True)
        detected_text = []
        confidence = 0
        
        if results[0] is not None:
            for result in results[0]:
                text = result[1][0]  # The detected text
                conf = result[1][1]  # The confidence score
                detected_text.append(text)
                confidence = conf
            
            return ''.join(detected_text), confidence
        return None, 0
    
    def detect_from_video(self, video_path=None):
        """
        Detect license plates from video file.
        
        Args:
            video_path: Path to video file (uses default test video if None)
        """
        if video_path is None:
            video_path = TEST_VIDEO_PATH
        
        cap = cv2.VideoCapture(video_path)
        counter = []
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame or end of video")
                break
            
            frame = cv2.resize(frame, (VIDEO_RESIZE_WIDTH, VIDEO_RESIZE_HEIGHT))
            results = self.model.track(frame, persist=True, imgsz=240)

            # Check if there are any boxes in the results
            if results[0].boxes is not None and results[0].boxes.id is not None:
                boxes = results[0].boxes.xyxy.int().cpu().tolist()  # Bounding boxes
                class_ids = results[0].boxes.cls.int().cpu().tolist()  # Class IDs
                track_ids = results[0].boxes.id.int().cpu().tolist()  # Track IDs
                confidences = results[0].boxes.conf.cpu().tolist()  # Confidence score

                for box, class_id, track_id, conf in zip(boxes, class_ids, track_ids, confidences):
                    c = self.class_names[class_id]
                    x1, y1, x2, y2 = box
                    cx = int(x1 + x2) // 2
                    cy = int(y1 + y2) // 2
                    
                    result = cv2.pointPolygonTest(np.array(DETECTION_AREA, np.int32), ((cx, cy)), False)
                    if result >= 0:
                        if track_id not in counter:
                            counter.append(track_id)  # Only add if it's a new track ID
                
                            crop = frame[y1:y2, x1:x2]
                            crop = cv2.resize(crop, (160, 50))
                            
                            text, ocr_conf = self.perform_ocr(crop)
                            
                            if text and ocr_conf > OCR_CONFIDENCE_THRESHOLD:
                                # Create a semi-transparent background for text
                                overlay = frame.copy()
                                cv2.rectangle(overlay, (x1, y1-60), (x2, y1), (0, 0, 0), -1)
                                cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
                                
                                # Display text and confidence
                                text_str = f"Plate: {text}"
                                conf_str = f"Conf: {ocr_conf:.2f}"
                                
                                cv2.putText(frame, text_str, (x1, y1-35), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                                cv2.putText(frame, conf_str, (x1, y1-15), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
                                
                                # Display the cropped plate
                                cv2.imshow("License Plate", crop)
                                
                                # Clean up text for database storage
                                text = text.replace('(', '').replace(')', '').replace(',', '').replace(']', '').replace('-', ' ')
                                
                                # Store in database
                                manage_numberplate_db(text)
            
            mycounter = len(counter)               
            cvzone.putTextRect(frame, f'{mycounter}', (50, 60), 1, 1)
            cv2.polylines(frame, [np.array(DETECTION_AREA, np.int32)], True, (255, 0, 0), 2)
            cv2.imshow("RGB", frame)
            
            if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
                break

        # Close video capture
        cap.release()
        cv2.destroyAllWindows()

def main():
    """Main function to run plate detection."""
    detector = PlateDetector()
    print("Starting license plate detection...")
    print("Press 'Esc' to exit")
    detector.detect_from_video()

if __name__ == "__main__":
    main()