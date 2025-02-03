import cv2

webcam = cv2.VideoCapture(1)
while True:
    control,image=webcam.read()

    if cv2.waitKey(20) == 27 :
        break

    cv2.imshow('webcam',image)
