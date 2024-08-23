import numpy as np
import cv2

# This is how you get open an image.
img = cv2.imread("assets/bike.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imshow("Bike", img) # Open the image.
cv2.waitKey(0)          # Keep the window, till you press 0.
cv2.destroyAllWindows() # If you press zeros, then close all cv2 windows.