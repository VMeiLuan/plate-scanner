## Overview
A Python-based vehicle plate scanner built using OpenCV and EasyOCR. It integrates with a Laravel application via API communication, where Laravel serves as the main backend system and the Python service handles image-based plate detection and recognition in the background. The processed results are returned to Laravel for further handling and business logic processing.

## Project Structure
    plate-scanner/
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
Copy `.env.example` to `.env` and update / adjust the values.
To enable Laravel API, set `LARAVEL_ENABLED=true` and fill in the URL and token.

## Run
    python main.py

## Logs
Daily logs are saved automatically to the `logs/` folder as `YYYY-MM-DD.log`.

## Notes
The service is fully operational even without Laravel integration.
If executed standalone, the plate detection results will be printed directly in the terminal, allowing testing and validation of the recognition pipeline.