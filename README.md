# Object Detection System

A Python computer vision project that detects faces in an image using OpenCV's pre-trained Haar cascade classifier. Built as part of VAYDA SYSTEM infrastructure.

## Features

- Detects faces in a still image
- Draws a bounding rectangle around each detected face
- Saves the output result as `output.jpg`
- Uses OpenCV's built-in Haar cascade classifier

## Requirements

- Python 3.10 or 3.11
- OpenCV (`opencv-python`)

## Installation
```bash
pip install -r requirements.txt
python main.py --image path/to/image.jpg
object-detection-system/
├── README.md
├── requirements.txt
└── main.py
