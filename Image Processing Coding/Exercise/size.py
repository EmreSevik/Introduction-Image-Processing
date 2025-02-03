import cv2

read=cv2.imread("logo.jpg")
(height,width,deep)=read.shape
print("Height: {} Width: {} Deep: {}".format(height,width,deep))
cv2.imshow("Image",read)
cv2.waitKey(0)
