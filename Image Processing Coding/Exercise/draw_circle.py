import cv2
import numpy as np

image = cv2.imread('logo.jpg')

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.putText(image,"Draw a circle",(x-90,y-40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
        cv2.circle(image,(x,y),25,(0,255,0))

cv2.namedWindow('image', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('image',draw_circle)
while True:
    cv2.imshow('image',image)
    if cv2.waitKey(20) & 0xFF == 27:
        break

cv2.destroyAllWindows()