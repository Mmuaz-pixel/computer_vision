import cv2 as cv 
import numpy as np 

img = cv.imread('sample.jpg')

# Translation 

def translate(img, x, y): 
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)


# Rotation 

def rotate(img, angle, rotpoint=None): 
    height, width = img.shape[:2]

    if rotpoint is None: 
        rotpoint = (width//2, height//2)
    
    rotMat = cv.getRotationMatrix2D(rotpoint, angle, 1.0)

    dimension = (width, height)

    return cv.warpAffine(img, rotMat, dimension)


# Flipping the image 

flip = cv.flip(img, -1) # 0: Vertical flip , 1: Horizontal Flip, -1: Both 

# translatedImg = translate(img, 100, 100)
# cv.imshow('Translated', translatedImg)

# rotatedImg = rotate(img, -30)
# cv.imshow('Rotated', rotatedImg)

cv.imshow('Flipped', flip)
cv.waitKey(0)
cv.destroyAllWindows()