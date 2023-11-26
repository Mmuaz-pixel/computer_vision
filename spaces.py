import cv2 as cv 

# color spaces are different ways to color the image e.g BGR, gray etc 

img = cv.imread('bird.jpg')
img = cv.resize(img, (700, 500), cv.INTER_CUBIC)
cv.imshow('Birdi', img)

# Gray 
gray = cv.cvtColor(img, code = cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV 
hsv = cv.cvtColor(img, code= cv.COLOR_BGR2HSV_FULL)
# cv.imshow('HSV', hsv)

# BGR to l a b 
lab = cv.cvtColor(img, cv.COLOR_BGR2Lab)
# cv.imshow('LAB', lab)

# BGR to RGB 
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb', rgb)

# gray to BGR 

bgr = cv.cvtColor(gray, cv.COLOR_GRAY2BGR)
cv.imshow('BGR', bgr)
cv.waitKey(0)