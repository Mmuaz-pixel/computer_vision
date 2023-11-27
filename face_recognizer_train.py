import cv2 as cv 
import os 
import numpy as np 

# We will build a face recognizer using built in face recognizer of python 

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']

haarCascade = cv.CascadeClassifier('haar_face.xml')

DIR = r"D:\Codeplayground\Artificial Intelligence\Computer Vision\Faces\train"

features = []
labels = []

def create_train(): 
    for per in people: 
        path = os.path.join(DIR, per)
        label = people.index(per)

        for img in os.listdir(path): 
            img_path = os.path.join(path, img)
            img = cv.imread(img_path)
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            faces_rectangle = haarCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

            for x,y,w,h in faces_rectangle: 
                faces_region = gray[y:y+h, x:x+w]
                features.append(faces_region)
                labels.append(label)

create_train()

print(f'length of features: {len(features)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.train(features, labels)

face_recognizer.save('face_trained_model.yml') # saving model 

np.save('features.npy', features) # we have saved the features in this numpy file 
np.save('labels.npy', labels) # same as above 