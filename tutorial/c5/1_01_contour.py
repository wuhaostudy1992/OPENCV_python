import numpy as np
import cv2
from matplotlib import pyplot as plt

im = cv2.imread('3.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
i = imgray[:]
ret,thresh = cv2.threshold(imgray,127,255,0)

image10, contours1, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
img11 = cv2.drawContours(imgray, contours1, -1, (0,255,0), 3)
img12 = cv2.drawContours(imgray, contours1, 3, (0,255,0), 3)

imgray = i[:]

image20, contours2, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
img21 = cv2.drawContours(imgray, contours2, -1, (0,255,0), 3)
img22 = cv2.drawContours(imgray, contours2, 3, (0,255,0), 3)

#cnt = contours[4]
#img23 = cv2.drawContours(imgray, [cnt], 0, (0,255,0), 3)


images = [image10, img11, img12, image20, img21, img22]
titles = ['None', '-1', '3', 'SIMPLE', '-1', '3']

for i in range(6):
	plt.subplot(2, 3, i+1), plt.imshow(images[i], cmap = 'gray'), plt.title(titles[i])
	
plt.show()
