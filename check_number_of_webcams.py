import cv2

def list_available_cameras(max_cameras=10):
    available_cameras = []
    for i in range(max_cameras):
        cap = cv2.VideoCapture(i)
        if cap.isOpened():
            available_cameras.append(i)
            cap.release()
    return available_cameras

available_cameras = list_available_cameras()

if available_cameras:
    print(f"Available cameras: {available_cameras}")
else:
    print("No cameras detected.")
