## Overview
A Python-based car plate scanner using OpenCV and EasyOCR. It integrates with a Laravel application via API communication, where Laravel acts as the main backend service and Python processes image-based plate scanning in the background.

## Project Structure
    scanner/
    ├── config/         # App settings loaded from .env
    ├── services/       # Camera, OCR, and Laravel API logic
    ├── utils/          # Plate validator and logger
    ├── logs/           # Auto-generated daily log files
    ├── main.py         # Entry point
    ├── .env            # Your local environment variables (not committed)
    └── .env.example    # Template for .env

## Setup
    pip install opencv-python easyocr python-dotenv requests

## Configuration
Copy `.env.example` to `.env` and update the values.
To enable Laravel API, set `LARAVEL_ENABLED=true` and fill in the URL and token.

## Run
    python main.py

## Logs
Daily logs are saved automatically to the `logs/` folder as `YYYY-MM-DD.log`.