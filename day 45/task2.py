from ultralytics import YOLO

import os

print(os.getcwd())
print(os.listdir())

model = YOLO("yolov8n.pt")

results = model([
    "../image2.jpg",
    "../image3.jpg"
], save=True)
results[0].show()