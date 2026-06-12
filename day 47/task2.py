import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

video = cv2.VideoCapture(r"C:\Users\user\OneDrive\Pictures\Camera Roll\WIN_20260612_12_53_08_Pro.mp4")

while True:

    success, frame = video.read()

    if not success:
        break

    results = model(frame)

    annotated_frame = results[0].plot()

    cv2.imshow(
        "YOLO Detection",
        annotated_frame
    )

    if cv2.waitKey(1) == 27:
        break

video.release()
cv2.destroyAllWindows()