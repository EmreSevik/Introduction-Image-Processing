import cv2

image=cv2.imread("logo.jpg")
cv2.rectangle(image,(12,12 ),(155,180),(0,0,255),4)
cv2.imshow("Image",image)
cv2.waitKey(0)