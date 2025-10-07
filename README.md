# Car Plate Detection System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0.1-000000.svg)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.5.3-5C3EE8.svg)](https://opencv.org/)
[![YOLO](https://img.shields.io/badge/YOLO-8.0.196-00FFFF.svg)](https://github.com/ultralytics/ultralytics)
[![PaddleOCR](https://img.shields.io/badge/PaddleOCR-2.6.1-FF6B35.svg)](https://github.com/PaddlePaddle/PaddleOCR)

An intelligent computer vision system that automatically detects and extracts license plate information from video streams in real-time. Built with cutting-edge AI technologies including YOLOv11 for precise plate detection and PaddleOCR for accurate text recognition, this system provides a complete solution for automated vehicle identification with a user-friendly web interface and MySQL database integration for persistent storage and historical tracking of detected license plates.

## Features

- **Real-time Detection** - Live video processing with instant plate recognition
- **High Accuracy** - YOLOv11 model trained specifically for license plate detection
- **OCR Integration** - PaddleOCR for accurate text extraction
- **Web Interface** - User-friendly Flask web application
- **Database Storage** - MySQL integration for detected plate records

## Technology Stack

- **Python 3.8+** - Main programming language
- **Flask** - Web framework
- **OpenCV** - Computer vision processing
- **YOLOv11** - Object detection model
- **PaddleOCR** - Text recognition
- **MySQL** - Database storage
- **NumPy** - Numerical operations
- **Jupyter** - Model training and analysis

## Demo

![Car Plate Detection Demo](video/video.gif)

## Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/CarPlate.git
cd CarPlate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py

# Open browser to http://localhost:5000
```

## Project Structure

```
CarPlate/
├── main.py                    # Main entry point
├── requirements.txt           # Dependencies
├── api/
│   └── app.py                # Flask web application
├── frontend/
│   ├── static/css/style.css  # Styling
│   └── templates/index.html  # HTML template
├── config/
│   ├── settings.py           # Configuration
│   └── class_names.txt       # YOLO classes
├── models/
│   ├── best.pt               # Trained model
│   └── yolo11n.pt           # Base model
├── src/
│   └── plate_detector.py     # Detection logic
├── utils/
│   └── database_manager.py   # Database operations
├── data/videos/              # Test videos
└── notebooks/
    └── CarPlate.ipynb        # Training notebook
```

## Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/CarPlate.git
cd CarPlate
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure database (optional)**
   - Install MySQL server
   - Update `config/settings.py` with your database credentials

## Usage

### Web Application
```bash
python main.py
# Access at http://localhost:5000
```

### Direct Detection
```bash
python src/plate_detector.py
```

## Dataset

**Source**: [License Plate Recognition Dataset](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e) from Roboflow Universe

### Training Your Own Model

```python
# Download dataset
from roboflow import Roboflow
rf = Roboflow(api_key="your_api_key")
project = rf.workspace("roboflow-universe-projects").project("license-plate-recognition-rxg4e")
version = project.version(11)
dataset = version.download("yolov11")

# Train model
!yolo task=detect mode=train model=yolo11n.pt data={dataset.location}/data.yaml epochs=50 imgsz=640
```

## Configuration

Edit `config/settings.py` to modify:
- Model paths
- Database settings  
- OCR confidence thresholds
- Video processing parameters

## Dependencies

```
flask==2.0.1
opencv-python==4.5.3.56
ultralytics==8.0.196
paddleocr==2.6.1.3
numpy==1.21.2
cvzone==1.5.6
mysql-connector-python==8.1.0
pandas>=1.3.0
matplotlib>=3.4.0
jupyter>=1.0.0
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Roboflow Universe](https://universe.roboflow.com/roboflow-universe-projects/license-plate-recognition-rxg4e) - Dataset
- [Ultralytics](https://github.com/ultralytics/ultralytics) - YOLOv11
- [PaddlePaddle](https://github.com/PaddlePaddle/PaddleOCR) - OCR
- [Flask](https://flask.palletsprojects.com/) - Web framework

