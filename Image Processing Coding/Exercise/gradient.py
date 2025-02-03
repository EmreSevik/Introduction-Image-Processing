import cv2
import numpy as np

kernel=np.ones((5,5),np.uint8)
image=cv2.imread("j.png",0)
gradient=cv2.morphologyEx(image,cv2.MORPH_GRADIENT,kernel)
cv2.imshow("gradient",gradient)
cv2.imshow("image",image)
cv2.waitKey(0)