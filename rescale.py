import cv2 as cv 

img = cv.imread('sample.jpg')

def rescaleFrame(frame, scale = 0.75): 
    height = int(frame.shape[0] * scale) 
    width = int(frame.shape[1] * scale)

    dimensions = (width,height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


rescaled_img = rescaleFrame(img, 0.5)
cv.imshow("Image", rescaled_img)
print(img.shape)
print(rescaled_img.shape)

cv.waitKey(0)