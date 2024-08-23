import numpy as np
import cv2

# Open stream for video capture.
stream = cv2.VideoCapture(1)

# Check if stream is open, if not close it.
if not stream.isOpened():
    print("No stream opened :(")
    exit()

# Those we do to save the video.
fps = stream.get(cv2.CAP_PROP_FPS) # 30.0 fps for my MSI webcam.
width = int(stream.get(3))
height = int(stream.get(4))
output = cv2.VideoWriter("assets/4_stream.mp4",
                         cv2.VideoWriter_fourcc('m','p','4','v'),
                         fps=fps, frameSize=(width,height))

while True:
    # Here read from your strea.
    ret, frame = stream.read()
    # If all is good, ret is true and you have a frame.
    if not ret:
        print("No more stream:(")
        break

    frame = cv2.resize(frame, (width,height))
    output.write(frame)
    # Now display the frame.
    cv2.imshow("MyWebcam!",frame)
    # We always want a way to escape from all this.
    if cv2.waitKey(1) == ord('q'):
        break

# Release the stream and destroy windows.
stream.release()
cv2.destroyAllWindows()