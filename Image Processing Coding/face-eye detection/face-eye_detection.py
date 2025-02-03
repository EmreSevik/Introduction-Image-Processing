import cv2

face_detection=cv2.CascadeClassifier('yuz_tanima.xml')
eye_detection=cv2.CascadeClassifier('goz.xml')

if face_detection.empty():
    print('No face detected')

face=cv2.imread('yuz_resmi.jpg')
gray=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

facelast=face_detection.detectMultiScale(gray,1.3,5)

for (x,y,w,h) in facelast:
    cv2.rectangle(face,(x,y),(x+w,y+h),(0,255,0),2)
    eyelast=eye_detection.detectMultiScale(gray,1.2,5)
    for (ex,ey,ew,eh) in eyelast:
        cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,0,255),5)
cv2.imshow('face',face)
cv2.waitKey(0)