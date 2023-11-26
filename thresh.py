import cv2 as cv 

img = cv.imread('image.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Threshold Value (100): This is the pixel intensity value that will be used as a threshold. Pixels with intensity values less than this threshold will be set to the minimum value (0 in the case of cv.THRESH_BINARY), and pixels with intensity values greater than or equal to this threshold will be set to the maximum value.

# Maximum Value (255): This is the maximum pixel value that can be assigned to pixels exceeding the threshold. In your case, if a pixel's intensity is greater than or equal to the threshold (100), it will be set to this maximum value (300). This parameter is relevant when using certain thresholding types, like cv.THRESH_BINARY.

# Simple thresholding 

threshold, thresh = cv.threshold(gray, 120, 220, cv.THRESH_BINARY)

threshold, thresh_inv = cv.threshold(gray, 120, 220, cv.THRESH_BINARY_INV)

# Adaptive thresholding 

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 15, 10)

# cv.imshow('Threshold Inv', thresh_inv)
cv.imshow('Adaptive thresh', adaptive_thresh)
# cv.imshow('Threshold', thresh)
cv.imshow('People', img)

cv.waitKey(0)