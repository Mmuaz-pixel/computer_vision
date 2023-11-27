import numpy as np 
import cv2 as cv 

haarCascade = cv.CascadeClassifier('haar_face.xml')
features = np.load('features.npy', allow_pickle=True)
labels = np.load('labels.npy', allow_pickle=True)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained_model.yml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

img = cv.imread(r'D:\Tours\Naran Tour 2022\IMG_20220909_115446_871.jpg')

img = cv.resize(img, (400, 400))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces_rects = haarCascade.detectMultiScale(gray, 1.1, 4)

for (x,y,w,h) in faces_rects:
    face_region = gray[y:y+h, x:x+w]
    label, confidence = face_recognizer.predict(face_region)

    print(f'Label = {people[label]} with confidence {confidence}')

    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)
    cv.putText(img, f"{people[label]} {confidence:.2f}%", (20,20), cv.FONT_HERSHEY_COMPLEX, 0.7, (0,255,0), thickness=2)

cv.imshow("Image", img)
cv.waitKey(0)