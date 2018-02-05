import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]
img1 = cv2.imread('3.jpg')
replicate = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,30,30,30,30,cv2.BORDER_CONSTANT,value=BLUE)


plt.subplot(231),plt.imshow(img1[:,:,::-1],'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate[:,:,::-1],'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect[:,:,::-1],'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101[:,:,::-1],'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap[:,:,::-1],'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant[:,:,::-1],'gray'),plt.title('CONSTANT')
plt.show()
