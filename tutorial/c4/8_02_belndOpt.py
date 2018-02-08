import cv2
import numpy as np,sys
from matplotlib import pyplot as plt

A = cv2.imread('4.jpg')
B = cv2.imread('5.jpg')

# generate Gaussian pyramid for A and B
GA, GB = A.copy(), B.copy()
gpA, gpB = [GA], [GB]
for i in range(6):
	GA = cv2.pyrDown(GA)
	GB = cv2.pyrDown(GB)
	gpA.append(GA)
	gpB.append(GB)
	
# generate Laplacian Pyramid for A and B
lpA, lpB = [gpA[5]], [gpB[5]]
for i in range(5,0,-1):
	GEA = cv2.pyrUp(gpA[i])
	GEB = cv2.pyrUp(gpB[i])
	LA = cv2.subtract(gpA[i-1],GEA)
	LB = cv2.subtract(gpB[i-1],GEB)
	lpA.append(LA)
	lpB.append(LB)
	
# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
	rows,cols,dpt = la.shape
	ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))
	LS.append(ls)
	
# now reconstruct
ls_ = LS[0]
for i in range(1,6):
	ls_ = cv2.pyrUp(ls_)
	ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))

plt.subplot(121), plt.imshow(ls_[:,:,::-1]), plt.title('Pyramid_blending2')
plt.subplot(122), plt.imshow(real[:,:,::-1]), plt.title('Direct_blending')

plt.show()
