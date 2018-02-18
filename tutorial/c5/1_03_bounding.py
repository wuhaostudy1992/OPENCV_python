import numpy as np
import cv2

img = cv2.imread('9.jpg', 0)
#ret, thresh = cv2.threshold(img, 240, 255, cv2.THRESH_BINARY)
x,y,w,h = cv2.boundingRect(img)
img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
cv2.imshow('image1', img)
cv2.waitKey(0)

img = cv2.imread('9.jpg', 0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
rect = cv2.minAreaRect(cnt)
box = cv2.boxPoints(rect)
box = np.int0(box)
img = cv2.drawContours(img,[box],0,(255,255,255),2)
cv2.imshow('image2', img)
cv2.waitKey(0)
