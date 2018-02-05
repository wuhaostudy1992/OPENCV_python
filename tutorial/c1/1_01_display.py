import numpy as np
import cv2

img = cv2.imread('1.jpg')
cv2.namedWindow('Image', cv2.WINDOW_AUTOSIZE)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()