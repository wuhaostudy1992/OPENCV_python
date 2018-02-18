import numpy as np
import cv2

img = cv2.imread('9.jpg', 0)
ret, thresh = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
img, contours, hierarchy = cv2.findContours(thresh, 1, 2)
cv2.imshow('image1', img)
cv2.waitKey(0)
cv2.imwrite('9.jpg', img)
