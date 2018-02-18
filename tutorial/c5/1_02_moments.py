import cv2
import numpy as np

img = cv2.imread('5.jpg', 0)
cv2.imshow('img', img)
cv2.waitKey(0)
ret, thresh = cv2.threshold(img, 127, 255, 0)
image, contours, hierarchy = cv2.findContours(thresh, 1, 2)
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imshow('img', img)
cv2.waitKey(0)

cnt = contours[0]
M = cv2.moments(cnt)
#print(M)

#the below is the centroid
print(M['m10']//M['m00'])
print(M['m01']//M['m00'])

#contour area
area = cv2.contourArea(cnt)
print('Area is {}'.format(area))
#contour perimeter
perimeter = cv2.arcLength(cnt, True)
print('Perimeter is {}'.format(perimeter))

epsilon = 0.1*cv2.arcLength(cnt, True)
approx = cv2.approxPolyDP(cnt, epsilon, True)
print('Approx is {}'.format(approx))
cv2.drawContours(img, approx, -1, (255,255,255), 3)
cv2.imshow('image', img)
cv2.waitKey(0)

#Convex Hull
hull = cv2.convexHull(cnt)
print('Hull is {}'.format(hull))
#print(cv2.convexHull(cnt, returnPoints = False))
cv2.drawContours(img, hull, -1, (255,255,255), 3)
cv2.imshow('image Hull', img)
cv2.waitKey(0)
