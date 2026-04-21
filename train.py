from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="dataset_helmet_vest/data.yaml",
    epochs=20,
    imgsz=640,
    batch=8
)