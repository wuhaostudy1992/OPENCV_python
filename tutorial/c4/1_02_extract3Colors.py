import cv2
import numpy as np

img = cv2.imread('5.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130,255,255])
lower_Green = np.array([50, 110, 50])
upper_Green = np.array([255,130,255])
lower_red = np.array([50, 50, 110])
upper_red = np.array([255,255,130])


mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
mask_red = cv2.inRange(hsv, lower_red, upper_red)
mask_Green = cv2.inRange(hsv, lower_Green, upper_Green)

res_blue = cv2.bitwise_and(img, img, mask=mask_blue)
res_red = cv2.bitwise_and(img, img, mask=mask_red)
res_Green = cv2.bitwise_and(img, img, mask=mask_Green)

cv2.imshow('blue', res_blue)
cv2.imshow('red', res_red)
cv2.imshow('yellow', res_Green)

while(True):
	k = cv2.waitKey(30) & 0xFF
	if k == 27:
		break
