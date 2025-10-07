"""
Main entry point for the Car Plate Detection System.
This file starts the Flask web application.
"""

import os
import sys

# Add current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from api.app import app

if __name__ == '__main__':
    print("Starting Car Plate Detection System...")
    print("Access the application at: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)