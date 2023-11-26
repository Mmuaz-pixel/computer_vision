import cv2 as cv 
import matplotlib.pyplot as plt 
import numpy as np 

img = cv.imread('image.jpg')
gray = cv.cvtColor(img , cv.COLOR_BGR2GRAY)
blank = np.zeros(img.shape[:2], dtype=np.uint8)
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, (255,255,255), -1)

masked = cv.bitwise_and(gray, mask)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

print(gray_hist) # this is a array of number of pixels at each intensity value 
print(gray_hist.shape)

plt.figure()
plt.title("Histogram")
plt.xlabel("Bins")
plt.ylabel("Number of pixels")
plt.xlim([0,256])
plt.plot(gray_hist) # assumes x-axis as the indexes of the array 
plt.figure()
plt.hist(gray.flatten(), bins=50)

cv.imshow('Masked', masked)

plt.show()
cv.waitKey(0)