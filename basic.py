import cv2 as cv 

img = cv.imread('sample.jpg')

# converting to grey 
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

#blurring 

blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)

# edge cascade (finding edges)

# canny = cv.Canny(img, 125, 175)
canny = cv.Canny(blur, 125, 175)# more prominent edges

# Dilating the image 

dilated = cv.dilate(canny, (3,3), iterations=1) # used for increasing the size of borders 

# eroding the image 

eroded = cv.erode(dilated, (3,3), iterations=2)
# used for opposite of dilation. hiding small details and making the image compact 

# cropping the image 

croped = img[0:200, 200:400]

# cv.imshow('Canny', canny) 
# cv.imshow('cropped', croped)
# cv.imshow('Eroded', eroded)
# cv.imshow('Dilated', dilated)
cv.imshow('Image', img)
cv.waitKey(0)