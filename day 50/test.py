from ultralytics import YOLO

model = YOLO(
    "runs/detect/train/weights/best.pt"
)

results = model("test/images/helmetimage-208-_jpg.rf.8d795f2306aa50895aa6f721f20ec2bd.jpg")

results[0].show()