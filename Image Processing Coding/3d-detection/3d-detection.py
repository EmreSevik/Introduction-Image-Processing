import cv2
import mediapipe as mp

mp_3d = mp.solutions.objectron
mp_3d_draw = mp.solutions.drawing_utils

image = cv2.imread('cup.jpg')
image = cv2.resize(image, (500, 500))

with mp_3d.Objectron(static_image_mode=True,
                     max_num_objects=1,
                     min_detection_confidence=0.3,
                     min_tracking_confidence=0.3,
                     model_name="Cup") as objects_3d:
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    last = objects_3d.process(rgb)

    if last.detected_objects:
        for detect in last.detected_objects:
            mp_3d_draw.draw_landmarks(
                image, detect.landmarks_2d, mp_3d.BOX_CONNECTIONS,
                mp_3d_draw.DrawingSpec(color=(255, 0, 0), thickness=2, circle_radius=2),
                mp_3d_draw.DrawingSpec(color=(0, 0, 255), thickness=2, circle_radius=2)
            )

    cv2.imshow("3D", image)
    cv2.waitKey(0)
 
