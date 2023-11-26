import cv2 as cv 
import numpy as np 

img = cv.imread('sample.jpg')

blank = np.zeros((600, 600, 3), dtype=np.uint8)

blank[0:200, 0:200] = np.random.randint(0, 100, (200, 200, 3), dtype='uint8')
blank[200:400, 200:400] = np.random.randint(100, 200, (200, 200, 3), dtype='uint8')
blank[400:600, 400:600] = np.random.randint(0, 200, (200, 200, 3), dtype='uint8')

cv.rectangle(blank, (200, 200), (400, 400), (0,255,0), thickness=2)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), radius=80, color=(0, 0, 255), thickness=2)

cv.putText(blank, 'Random Image', (220, 300), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255, 0, 0), thickness=2)
cv.imshow('Sample', blank)

cv.waitKey(0)