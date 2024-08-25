import numpy as np
import cv2

img = cv2.imread("assets/shapes.png")
# For corner detection it is easier to work with gray scale.
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Shi-Tomashi method
corners = cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                                  qualityLevel=0.05, minDistance=50)
corners = np.int64(corners)

for c in corners:
    x, y = c.ravel()
    img = cv2.circle(img, center=(x,y), radius=20,
                     color=(0,0,255),thickness=-1)

# Shi-Tomashi method
corners = cv2.goodFeaturesToTrack(gray_img, maxCorners=50,
                                  qualityLevel=0.01, minDistance=50,
                                  useHarrisDetector=True, k=0.1)
corners = np.int64(corners)

for c in corners:
    x, y = c.ravel()
    img = cv2.circle(img, center=(x,y), radius=5,
                     color=(0,255,0),thickness=-1)

cv2.imshow("Shape", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("assets/5_shape_w_corners.png",img)