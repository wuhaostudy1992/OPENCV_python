import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('6.jpg')

kernel1 = np.ones((5, 5), np.float32)/25
dst1 = cv2.filter2D(img, -1, kernel1)

dst2 = cv2.blur(img, (5,5))
dst3 = cv2.GaussianBlur(img, (5,5), 0)
dst4 = cv2.medianBlur(img, 5)
dst5 = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(231), plt.imshow(img[:,:,::-1]), plt.title('Original')
plt.subplot(232), plt.imshow(dst1[:,:,::-1]), plt.title('Transform1')
plt.subplot(233), plt.imshow(dst2[:,:,::-1]), plt.title('Transform2')
plt.subplot(234), plt.imshow(dst3[:,:,::-1]), plt.title('Transform3')
plt.subplot(235), plt.imshow(dst4[:,:,::-1]), plt.title('Transform4')
plt.subplot(236), plt.imshow(dst5[:,:,::-1]), plt.title('Transform5')
plt.show()
