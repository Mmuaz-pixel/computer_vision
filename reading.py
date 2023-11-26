import cv2 as cv 

# img = cv.imread('sample.jpg')
# print(img.shape) # height, width, channel (3: colored, 1: grayscale)

# cv.imshow('Sample',img)

video = cv.VideoCapture('sample.mp4')  # argument 0 is used for web cam 
while True: 

    success, frame = video.read()
    cv.imshow('Video', frame)

    if cv.waitKey(1) & 0xFF == ord('d'): # d is pressed then break 
        break

video.release()
cv.destroyAllWindows()

# cv.waitKey(0)