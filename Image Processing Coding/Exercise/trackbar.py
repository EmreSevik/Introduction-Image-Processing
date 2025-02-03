import cv2
import numpy as np

cv2.namedWindow("Image")
image=np.zeros((450,495,3),np.uint8)

def func(value):
    print(value)

cv2.createTrackbar("Blue","Image",0,255,func)
cv2.createTrackbar("Green","Image",0,255,func)
cv2.createTrackbar("Red","Image",0,255,func)

while True:
    cv2.imshow("Image",image)
    blue=cv2.getTrackbarPos("Blue","Image")
    green=cv2.getTrackbarPos("Green","Image")
    red=cv2.getTrackbarPos("Red","Image")
    image[:]=[blue,green,red]

    cv2.waitKey(1)
