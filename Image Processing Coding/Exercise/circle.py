import cv2

image=cv2.imread("logo.jpg")
cv2.circle(image,(100,100),100,(0,255,0),3)
cv2.imshow("Image",image)
cv2.waitKey(0)