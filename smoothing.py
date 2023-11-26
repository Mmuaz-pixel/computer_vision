import cv2 as cv 
import numpy as np 

img = cv.imread('sample.jpg')
# img = cv.resize(img, (700, 500), interpolation=cv.INTER_CUBIC) 

## Blurring techniques 

# 1) Average blur (takes the average of pixel intensity of surrounding kernel window and apply that)

average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

# 2) Gaussian blur (apply weights to the windows and then take avg) - More weight to the closer ones and less weight to far ones.- More natural  

gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian', gauss)

# 3) Median blur (takes the median of the intensies) - Reduces more noise and make more smooth 

median = cv.medianBlur(img, 3, 0)
cv.imshow('Median Blur', median)

# 4) Bilateral blurring - Used in advanced projects and it retains the edges while applying the blur

bilateral = cv.bilateralFilter(img, 5, 40, 35)
cv.imshow('Bilateral', bilateral)

cv.imshow('sample', img)
cv.waitKey(0)