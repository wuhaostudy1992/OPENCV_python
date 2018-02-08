import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('6.jpg')
rows, cols, ch = img.shape

#pts1 and pts2 represent three points in the input and outout pitcure
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
pts3 = np.float32([[10,10],[200,50],[50,100]])

M1 = cv2.getAffineTransform(pts1, pts2)
M2 = cv2.getAffineTransform(pts1, pts3)

dst1 = cv2.warpAffine(img, M1, (cols, rows))
dst2 = cv2.warpAffine(img, M2, (cols, rows))

plt.subplot(131), plt.imshow(img), plt.title('Original')
plt.subplot(132), plt.imshow(dst1), plt.title('Transform1')
plt.subplot(133), plt.imshow(dst2), plt.title('Transform2')
plt.show()
