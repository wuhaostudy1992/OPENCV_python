import cv2
import numpy as np

def nothing(x):
	pass
	
img1 = cv2.imread('4.jpg')
img2 = cv2.imread('5.jpg')
cv2.namedWindow('image')
imgadd = cv2.add(img1, img2)

cv2.createTrackbar('weight', 'image', 0, 100, nothing)

while(True):
	cv2.imshow('image', imgadd)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
		
	weight = cv2.getTrackbarPos('weight', 'image') / 100
	
	imgadd = cv2.addWeighted(img1, weight, img2, 1-weight, 0)
