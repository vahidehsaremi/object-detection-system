# Object Detection System

A Python computer vision project that detects faces in an image using OpenCV's pre-trained Haar cascade classifier. Built as part of VAYDA SYSTEM infrastructure.

## Features

- Detects faces in a still image
- Draws a bounding rectangle around each detected face
- Saves the output image as `output.jpg`
- Uses OpenCV's built-in Haar cascade classifier

## Requirements

- Python 3.10 or 3.11
- OpenCV (`opencv-python`)

## Installation

Install the required dependency:

```bash
pip install -r requirements.txt
```

## Usage

Run face detection on an image:

```bash
python main.py --image path/to/image.jpg
```

The processed image will be saved as `output.jpg` in the project root.

## Note

This application detects faces using a standard pre-trained Haar cascade. It does not include a custom-trained model or detect general categories of objects.

## Project Structure

```text
object-detection-system/
├── README.md
├── requirements.txt
└── main.py
```
```