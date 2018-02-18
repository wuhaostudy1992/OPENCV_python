import cv2

img = cv2.imread('9.jpg', 0)
#img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(img, 127, 255, 0)
img, contours, hierarchy = cv2.findContours(thresh, 1, 2)
cnt = contours[0]
rows,cols = img.shape[:2]


[vx,vy,x,y] = cv2.fitLine(cnt, cv2.DIST_L2,0,0.01,0.01)
lefty = int((-x*vy/vx) + y)
righty = int(((cols-x)*vy/vx)+y)
img = cv2.line(img,(cols-1,righty),(0,lefty),(255,255,255),2)
cv2.imshow('image', img)
cv2.waitKey(0)
