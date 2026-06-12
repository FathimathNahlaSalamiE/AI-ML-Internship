from ultralytics import YOLO
import os

print(os.getcwd())
print(os.listdir())

model = YOLO("yolov8n.pt")
results = model(r"C:\Users\user\Downloads\dogs-and-cats-live-together-ai-generative-free-photo.jpg",save=True)
results[0].show()