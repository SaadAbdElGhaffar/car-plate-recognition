"""
Application settings and configuration for Car Plate Detection System.
"""

import os

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Model paths
MODEL_PATH = os.path.join(BASE_DIR, "models", "best.pt")
YOLO_BASE_MODEL_PATH = os.path.join(BASE_DIR, "models", "yolo11n.pt")

# Configuration files
CLASS_NAMES_PATH = os.path.join(BASE_DIR, "config", "class_names.txt")

# Flask configuration
TEMPLATE_FOLDER = os.path.join(BASE_DIR, "frontend", "templates")
STATIC_FOLDER = os.path.join(BASE_DIR, "frontend", "static")

# Database configuration
DB_CONFIG = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "",
    "database": "numberplate",
    "port": 3306
}

# OCR configuration
OCR_CONFIDENCE_THRESHOLD = 0.5

# Video processing configuration
VIDEO_RESIZE_WIDTH = 1020
VIDEO_RESIZE_HEIGHT = 500
DETECTION_AREA = [(5, 180), (3, 249), (984, 237), (950, 168)]

# Data paths
DATA_DIR = os.path.join(BASE_DIR, "data")
VIDEOS_DIR = os.path.join(DATA_DIR, "videos")
TEST_VIDEO_PATH = os.path.join(VIDEOS_DIR, "tc.mp4")