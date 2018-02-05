import cv2
import numpy as np

img = cv2.imread('1.jpg')

"""Numpy is a optimized library for fast array calculations. So simply accessing each and every pixel
values and modifying it will be very slow and it is discouraged."""

#to access the red value
value = img.item(10, 10, 2)
print(value)

img.itemset((10, 10, 2), 100)
value = img.item(10, 10, 2)
print(value)

print(img.shape)
print(img.size)
print(img.dtype)

'''cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)'''
#cv2.destoryAllWindows()

region = img[0:300, 0:300]
img[500:800, 500:800] = region

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image', img)
cv2.waitKey(0)
