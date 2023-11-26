import cv2 as cv 
import numpy as np 

img = cv.imread('bird.jpg')
img = cv.resize(img, (700, 500), interpolation=cv.INTER_CUBIC) 

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)
# canny = cv.Canny(blur, 0, 300)

# we can also use this method for same purpose

ret, thresh = cv.threshold(gray, 100, 150, cv.THRESH_BINARY)

contours, hierarchies = cv.findContours(thresh, mode = cv.RETR_LIST, method=cv.CHAIN_APPROX_SIMPLE) # use mode = cv.RETR_EXTERNAL to get only outer contours, cv.RETR_TREE returns hierarchial contours..... method = cv.CHAIN_APPROX_NONE gets us all the contours and cv.CHAIN_APPROX_SIMPLE gets us only the contours that make most sense 

print(len(contours)) # number of contours 

blank = np.zeros(img.shape, dtype=np.uint8)
cv.drawContours(blank, contours=contours, contourIdx=-1, color=(0,255,0), thickness=1) # contouridx = -1 means all of them 

cv.imshow('contours', blank)
cv.imshow('bird', img)
cv.imshow('Thresh', thresh)
cv.waitKey(0)