import cv2 as cv 
import numpy as np 

img = cv.imread('bird.jpg')
img = cv.resize(img, (600, 500), interpolation=cv.INTER_CUBIC)

b, g, r = cv.split(img)

# cv.imshow('Blue', b)
# cv.imshow('Green', g)
# cv.imshow('Red', r)
cv.imshow('Birdi', img)

print(b.shape) # (500, 600) from (500, 600, 3)

# creating an image that actually shows the blue color according to intensity instead of just the gray scale 

blue = np.zeros((500, 600, 3), dtype=np.uint8)
blue[:, :, 0] = b

cv.imshow('Blues', blue)

red = np.zeros((500, 600, 3), dtype=np.uint8)
red[:, :, 2] = r

cv.imshow('Red', red)

# merging 

merged = cv.merge([b, g, r])

cv.waitKey(0)