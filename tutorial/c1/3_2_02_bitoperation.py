import cv2
import numpy as np

img1 = cv2.imread('4.jpg')
img2 = cv2.imread('5.jpg')

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# Now create a mask of logo and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 5, 255, cv2.THRESH_BINARY)
#print(mask[0])
mask_inv = cv2.bitwise_not(mask)
#print(mask_inv[0])

# Now black-out the area of logo in ROI
#print("image 1")
#print(img1[0])
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
#print("image 1 bg")
#print(img1_bg[0])

# Take only region of logo from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put logo in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst
cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
