import cv2 as cv 
import numpy as np 

img = cv.imread('image.jpg')

blank = np.zeros(img.shape[:2], dtype=np.uint8)
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, (255,255,255), -1) 

masked = cv.bitwise_and(img, img, mask=mask)

cv.imshow('Image', img)
cv.imshow('Masked', masked)

np.where()
cv.waitKey(0)