import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(1)
mp_drawing = mp.solutions.drawing_utils
mp_all=mp.solutions.holistic
with mp_all.Holistic(min_detection_confidence=0.5,min_tracking_confidence=0.5) as holistic:
    while True:
        control,image=webcam.read()
        image_rgb=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        results = holistic.process(image_rgb)
        image=cv2.cvtColor(image_rgb,cv2.COLOR_RGB2BGR)
        mp_drawing.draw_landmarks(image,results.left_hand_landmarks,mp_all.HAND_CONNECTIONS)
        mp_drawing.draw_landmarks(image,results.face_landmarks,mp_all.FACE_CONNECTIONS())
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_all.POSE_CONNECTIONS)

        if cv2.waitKey(20) == 27 :
            break

        cv2.imshow('webcam',image)
