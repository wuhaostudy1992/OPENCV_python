import cv2
from matplotlib import pyplot as plt
import numpy as np

x = np.uint8([200])
y = np.uint8([100])
print(cv2.addWeighted(x, 0.8, y, 0.2, 0))
print(cv2.addWeighted(x, 0.8, y, 0.2, 100))

img1 = cv2.imread('4.jpg')
img2 = cv2.imread('5.jpg')

img3 = cv2.add(img1, img2)
img4 = img1 + img2
img5 = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)

#cv2.imshow('image', img3)
#cv2.waitKey(0)

plt.subplot(231),plt.imshow(img1[:,:,::-1]),plt.title('First')
plt.subplot(232),plt.imshow(img2[:,:,::-1]),plt.title('Second')
plt.subplot(233),plt.imshow(img3[:,:,::-1]),plt.title('cv2add(saturate)')
plt.subplot(234),plt.imshow(img4[:,:,::-1]),plt.title('modulo')
plt.subplot(235),plt.imshow(img5[:,:,::-1]),plt.title('cv2weight')

plt.show()
