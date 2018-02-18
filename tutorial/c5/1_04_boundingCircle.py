import cv2

img = cv2.imread('9.jpg', 0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]


(x,y),radius = cv2.minEnclosingCircle(cnt)
center = (int(x),int(y))
radius = int(radius)
img1 = cv2.circle(img,center,radius,(255,255,255),2)
cv2.imshow('image', img1)
cv2.waitKey(0)

img = cv2.imread('9.jpg', 0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]

ellipse = cv2.fitEllipse(cnt)
img2 = cv2.ellipse(img,ellipse,(255,255,255),2)
cv2.imshow('image2', img2)
cv2.waitKey(0)
