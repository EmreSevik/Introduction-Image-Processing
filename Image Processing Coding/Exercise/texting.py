import cv2

image=cv2.imread("logo.jpg")
image=cv2.putText(image,"EMRE",(100,100),cv2.FONT_ITALIC,1,(0,255,0),2)
cv2.imshow("Text",image)
cv2.waitKey(0)