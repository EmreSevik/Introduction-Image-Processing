import cv2

image=cv2.imread("logo.jpg")
cv2.line(image,(50,90),(14,300),(0,0,255),3)
cv2.imshow("Image",image)
cv2.waitKey(0)