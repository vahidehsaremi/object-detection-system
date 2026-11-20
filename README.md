# Object Detection SystemA Python computer vision project that detects faces in an image using OpenCV's pre-trained Haar cascade classifier. Built as part of VAYDA SYSTEM infrastructure.

## Features- Detects faces in a still image- Draws a bounding rectangle around each detected face- Saves the output image as `output.jpg`
- Uses OpenCV's built-in Haar cascade classifier## Requirements- Python3.10 or3.11- OpenCV (`opencv-python`)

## InstallationInstall the required dependency:

 pip install -r requirements.txt## UsageRun face detection on an image:

 python main.py --image path/to/image.jpgThe processed image will be saved as `output.jpg` in the project root.

## NoteThis application detects faces using a standard pre-trained Haar cascade. It does not include a custom-trained model or detect general categories of objects.

## Project Structure object-detection-system/
 ├── README.md ├── requirements.txt └── main.py
