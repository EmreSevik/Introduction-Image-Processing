import cv2

video=cv2.VideoCapture("video.mp4")
while True:
    control,catch=video.read()
    if not control:
        print("video capture error")
    cv2.imshow('video',catch)
    if cv2.waitKey(20) & 0xFF == ord('p'):
        break
