import cv2
import numpy as np
from matplotlib import pyplot as ply

img = cv2.imread('8.pgm', 0)
cv2.namedWindow('image')

def nothing(x):
	pass

low, high = 0, 255
cv2.createTrackbar('Low', 'image', low, 255, nothing)
cv2.createTrackbar('High', 'image', high, 255, nothing)
cv2.imshow('image', img)

res = cv2.Canny(img, low, high)

while 1:
	cv2.imshow('image', res)
	if (cv2.waitKey(30) & 0xFF) == 27:
		break
	low = cv2.getTrackbarPos('Low', 'image')# if low < high else high
	high = cv2.getTrackbarPos('High', 'image')# if high > low else low
	
	res = cv2.Canny(img, low, high)
