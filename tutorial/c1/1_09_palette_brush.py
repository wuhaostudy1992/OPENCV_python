import cv2
import numpy as np

draw = False
ix = iy = -1


def nothing(x):
	pass

def drawLine(event, x, y, flags, param):
	global ix, iy, draw
	if event == cv2.EVENT_LBUTTONDOWN:
		draw = True
		ix, iy = x, y
	elif event == cv2.EVENT_MOUSEMOVE:
		if draw:
			cv2.line(img, (ix, iy), (x, y), (b,g,r), radius)
			ix, iy = x, y
	elif event == cv2.EVENT_LBUTTONUP:
		draw = False
	
img = np.zeros((300, 512, 3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image', drawLine)

cv2.createTrackbar('R', 'image', 0, 255, nothing)
cv2.createTrackbar('G', 'image', 0, 255, nothing)
cv2.createTrackbar('B', 'image', 0, 255, nothing)

#switch = '0: OFF \n1: ON'
#cv2.createTrackbar(switch, 'image', 0, 1, nothing)
brushRadius = 'Radius'
cv2.createTrackbar(brushRadius, 'image', 1, 20, nothing)

while(1):
	cv2.imshow('image', img)
	k = cv2.waitKey(1) & 0xFF
	if k == 27:
		break
	
	r = cv2.getTrackbarPos('R', 'image')
	g = cv2.getTrackbarPos('G', 'image')
	b = cv2.getTrackbarPos('B', 'image')
	#s = cv2.getTrackbarPos(switch, 'image')
	radius = cv2.getTrackbarPos(brushRadius, 'image')
