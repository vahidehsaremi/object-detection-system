import argparse
from pathlib import Path

import cv2


def detect_faces(image_path: Path) -> None:
    if not image_path.is_file():
        raise FileNotFoundError(f"Image not found: {image_path}")

    image = cv2.imread(str(image_path))
    if image is None:
        raise ValueError(f"Could not read image: {image_path}")

    cascade_path = (
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )
    face_detector = cv2.CascadeClassifier(cascade_path)

    if face_detector.empty():
        raise RuntimeError("Could not load the Haar cascade classifier.")

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(
        gray_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )

    for (x, y, width, height) in faces:
        cv2.rectangle(
            image,
            (x, y),
            (x + width, y + height),
            (0, 255, 0),
            2,
        )

    output_path = Path("output.jpg")
    if not cv2.imwrite(str(output_path), image):
        raise RuntimeError(f"Could not save the output image: {output_path}")

    print(f"Faces detected: {len(faces)}")
    print(f"Output saved to: {output_path.resolve()}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Detect faces in an image using OpenCV."
    )
    parser.add_argument(
        "--image",
        required=True,
        help="Path to the input image.",
    )
    args = parser.parse_args()

    detect_faces(Path(args.image))


if __name__ == "__main__":
    main()
