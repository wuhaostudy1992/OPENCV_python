import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('test.pgm',0)
laplacian = cv2.Laplacian(img,cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobelx = np.uint8(np.absolute(sobelx))

sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobely = np.uint8(np.absolute(sobely))

final1 = sobelx + sobely
final2 = np.add(sobelx, sobely)

plt.subplot(231),plt.imshow(img,cmap = 'gray'), plt.title('Original')
plt.subplot(232),plt.imshow(laplacian,cmap = 'gray'), plt.title('Laplacian')
plt.subplot(233),plt.imshow(sobelx,cmap = 'gray'),plt.title('Sobel X')
plt.subplot(234),plt.imshow(sobely,cmap = 'gray'),plt.title('Sobel Y')
plt.subplot(235),plt.imshow(final1,cmap = 'gray'),plt.title('Final 1')
plt.subplot(236),plt.imshow(final2,cmap = 'gray'),plt.title('Final 2')

plt.show()
