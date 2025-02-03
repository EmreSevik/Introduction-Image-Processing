import cv2
import numpy as np

img = np.zeros((300, 300, 1), np.uint8)
cv2.namedWindow('Trackbar')

def func(value):
    print(value)

cv2.createTrackbar('LowB', 'Trackbar', 0, 255, func)
cv2.createTrackbar('HighB', 'Trackbar', 0, 255, func)
cv2.createTrackbar('LowG', 'Trackbar', 0, 255, func)
cv2.createTrackbar('HighG', 'Trackbar', 0, 255, func)
cv2.createTrackbar('LowR', 'Trackbar', 0, 255, func)
cv2.createTrackbar('HighR', 'Trackbar', 0, 255, func)

tracking = cv2.VideoCapture("takip.mp4")

if not tracking.isOpened():
    print("Video cannot be opened!")
    exit()

while True:

    control, catch = tracking.read()
    if not control:
        print("Video don't read.")
        break

    catch_resized = cv2.resize(catch, (400, 400), interpolation=cv2.INTER_AREA)

    LowB = cv2.getTrackbarPos('LowB', 'Trackbar')
    HighB = cv2.getTrackbarPos('HighB', 'Trackbar')
    LowG = cv2.getTrackbarPos('LowG', 'Trackbar')
    HighG = cv2.getTrackbarPos('HighG', 'Trackbar')
    LowR = cv2.getTrackbarPos('LowR', 'Trackbar')
    HighR = cv2.getTrackbarPos('HighR', 'Trackbar')
    low = np.array([LowB, LowG, LowR])
    high = np.array([HighB, HighG, HighR])
    goal = cv2.inRange(catch_resized, low, high)
    last = cv2.bitwise_and(catch_resized, catch_resized, mask=goal)
    combined = np.hstack((catch_resized, cv2.cvtColor(goal, cv2.COLOR_GRAY2BGR), last))
    cv2.imshow('Trackbar', img)
    cv2.imshow('Videos', combined)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

tracking.release()
cv2.destroyAllWindows()
