import cv2
import numpy as np
import time
from matplotlib import pyplot as plt

print(cv2.useOptimized())
cv2.setUseOptimized(False)
img = cv2.imread('3.jpg')

e1 = cv2.getTickCount()
plt.subplot(131), plt.imshow(cv2.medianBlur(img, 1)[:,:,::-1]), plt.title('1')
plt.subplot(132), plt.imshow(cv2.medianBlur(img, 11)[:,:,::-1]), plt.title('2')
plt.subplot(133), plt.imshow(cv2.medianBlur(img, 99)[:,:,::-1]), plt.title('3')

e2 = cv2.getTickCount()

time = (e2-e1) / cv2.getTickFrequency()
print(time)
cv2.setUseOptimized(True)
plt.show()
