import cv2
import numpy as np

def mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print("Mouse left button clicked")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print("Mouse right button clicked")
    elif event == cv2.EVENT_MOUSEMOVE:
        print("Mouse movement detected")

image=np.zeros((400,400,3),np.uint8)
cv2.namedWindow('Mouse', cv2.WINDOW_AUTOSIZE)
cv2.setMouseCallback('Mouse', mouse)
cv2.imshow('Mouse', image)
cv2.waitKey(0)