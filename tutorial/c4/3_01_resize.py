import cv2
import numpy as np

img = cv2.imread('test.pgm')
res = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('image', res)

print(img.shape)
print(img.shape[:2])
height, width = img.shape[:2]
res = cv2.resize(img, (width//2, height//2), interpolation=cv2.INTER_CUBIC)
cv2.imshow('image2', res)

cv2.imwrite('8.jpg', res)

while True:
	k = cv2.waitKey(30) & 0xFF
	if k == 27:
		break
