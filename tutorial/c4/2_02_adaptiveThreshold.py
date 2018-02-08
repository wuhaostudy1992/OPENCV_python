import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('3.jpg', 0)
img = cv2.medianBlur(img, 5)

ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
thresh2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
thresh3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

images = [img, thresh1, thresh2, thresh3]
titles = ['Original', 'binary', 'mean', 'Gaussian']

for i in range(4):
	plt.subplot(2, 2, i+1), plt.imshow(images[i]), plt.title(titles[i])
	
plt.show()
