import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('7.jpg')
lower_reso = cv2.pyrDown(img)

cv2.imshow('image1', img)
cv2.imshow('image', lower_reso)

higher_reso = cv2.pyrUp(lower_reso)
cv2.imshow('image', higher_reso)
cv2.waitKey(0)
