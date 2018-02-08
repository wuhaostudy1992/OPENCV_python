import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('6.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst1 = cv2.warpAffine(img, M, (cols, rows))
M = np.float32([[1, 0, 10], [0, 1, 50]])
dst2 = cv2.warpAffine(img, M, (cols*2, rows*2))

plt.subplot(121), plt.imshow(dst1), plt.title('Example 1')
plt.subplot(122), plt.imshow(dst2), plt.title('Example 2')
plt.show()

#cv2.imshow('img', dst)
#cv2.waitKey(0)
