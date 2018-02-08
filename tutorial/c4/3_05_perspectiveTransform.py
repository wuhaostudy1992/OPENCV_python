import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('6.jpg')
rows, cols, *_ = img.shape

pts1 = np.float32([[56,65], [368,52], [28,387], [389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
pts3 = np.float32([[0,0],[300,30],[50,200],[300,300]])

M1 = cv2.getPerspectiveTransform(pts1, pts2)
M2 = cv2.getPerspectiveTransform(pts1, pts3)

dst1 = cv2.warpPerspective(img, M1, (300, 300))
dst2 = cv2.warpPerspective(img, M2, (300, 300))

plt.subplot(131), plt.imshow(img), plt.title('Original')
plt.subplot(132), plt.imshow(dst1), plt.title('Transform1')
plt.subplot(133), plt.imshow(dst2), plt.title('Transform2')
plt.show()
