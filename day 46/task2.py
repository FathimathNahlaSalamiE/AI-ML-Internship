from ultralytics import YOLO

model = YOLO("yolov8n.pt")

results = model("../image.jpg")

results[0].show()

for result in results:

    print("Detected Objects")

    for box in result.boxes:
        print(box.conf)
        # print("Confidence:",box.conf)