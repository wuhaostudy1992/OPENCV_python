import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('5.jpg',0)
edges1 = cv2.Canny(img,100,200)
edges2 = cv2.Canny(img,100,200,True)


plt.subplot(221),plt.imshow(img,cmap = 'gray'),plt.title('Original Image')
plt.subplot(222),plt.imshow(edges1,cmap = 'gray'),plt.title('Edge Image')
plt.subplot(223),plt.imshow(edges2,cmap = 'gray'),plt.title('Edge Image')

plt.show()
