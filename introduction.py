import numpy as np
import cv2


img = cv2.imread("assets/bike.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Bike", img)
cv2.waitKey(0)
cv2.destroyAllWindows()  