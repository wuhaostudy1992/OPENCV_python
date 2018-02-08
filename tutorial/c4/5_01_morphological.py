import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('5.jpg', 0)

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)

#erosion followed by dilation
#it is useful to remove noise
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

#Dilation followed by Erosion
#It is useful in closing small holes inside the foreground objects, or small black points on the object
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)

plt.subplot(241), plt.imshow(img, cmap='gray'), plt.title('Original')
plt.subplot(242), plt.imshow(erosion, cmap='gray'), plt.title('Erosion')
plt.subplot(243), plt.imshow(dilation, cmap='gray'), plt.title('Dilation')
plt.subplot(244), plt.imshow(opening, cmap='gray'), plt.title('Opening')
plt.subplot(245), plt.imshow(closing, cmap='gray'), plt.title('Closing')
plt.subplot(246), plt.imshow(gradient, cmap='gray'), plt.title('Gradient')
plt.subplot(247), plt.imshow(tophat, cmap='gray'), plt.title('Tophat')
plt.subplot(248), plt.imshow(blackhat, cmap='gray'), plt.title('Blackhat')
plt.show()
