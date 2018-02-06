import cv2
import numpy as np
from matplotlib import pyplot as plt

#flags = [i for i in dir(cv2) if i.startswith('COLOR')]
#print(flags)

img = cv2.imread('5.jpg')

#while(True):
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

res = cv2.bitwise_and(img, img, mask=mask)

'''plt.subplot(121), plt.imshow(img), plt.title('img')
plt.subplot(122), plt.imshow(mask), plt.title('mask')
plt.subplot(123), plt.imshow(res), plt.title('res')

plt.show()'''
cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.imshow('res', res)

while(True):
	k = cv2.waitKey(300) & 0xFF
	if k == 27:
		break

#cv2.destoryAllWindows()
