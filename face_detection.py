import cv2 as cv 

# Face detection is finding that this is a face
# Face recognition is recognizing whose face is this

img = cv.imread('image.jpg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

haarCascade = cv.CascadeClassifier('haar_face.xml')

faces_ = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f"Number of faces found: {len(faces_)}")

for i in faces_: 
    cv.rectangle(img, (i[0], i[1]), (i[0] + i[2], i[1]+ i[3]), (0,255,0), thickness=2)

# harcascades are not very good at detecting faces. They are just easy to use. 

cv.imshow('Image', img)
cv.waitKey(0)