from ultralytics import YOLO

model = YOLO(
    "runs/detect/train/weights/best.pt"
)

results = model("test/images/suggested-g8COnTAMPzAhtjRT3SWj_jpg.rf.9d676383b3ea42affe1bf8eca8761342.jpg")

results[0].show()