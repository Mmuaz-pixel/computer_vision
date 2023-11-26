import cv2 as cv 
import numpy as np 
img = cv.imread('image.jpg')

# cv.imshow('Peeps', img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

## Laplace method 

lap = cv.Laplacian(gray, cv.CV_64F) 
lap = np.uint8(np.absolute(lap))

## Subel method 

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
sobel_combined = cv.bitwise_or(sobelx, sobely)

canny = cv.Canny(gray, 100, 255)

# cv.imshow('Sobelx', sobelx)
# cv.imshow('Sobely', sobely)
cv.imshow('Canny', canny) # The most cleanest 
cv.imshow('Sobel', sobel_combined)
cv.imshow('Laplacian', lap)
cv.waitKey(0)