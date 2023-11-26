import cv2 as cv 

# Face detection is finding that this is a face
# Face recognition is recognizing whose face is this

img = cv.imread('image.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cv.waitKey(0)