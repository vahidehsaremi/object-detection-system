     from ultralytics import YOLO

     model = YOLO("yolov8n.pt")

     def run(source: str = "0") -> None:
         """Run object detection on an image, video, or webcam (default)."""
         results = model(source)

         for result in results:
             names = result.names
             boxes = result.boxes
             for box in boxes:
                 class_id = int(box.cls[0].item())
                 confidence = float(box.conf[0].item())
                 print(f"{names[class_id]:<20} {confidence:.2%}")


     if __name__ == "__main__":
         run()
