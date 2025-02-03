import cv2

image=cv2.imread("logo.jpg")
crop=image[20:190,30:170]
cv2.imshow("Image",image)
cv2.imshow("Last",crop)
cv2.waitKey(0)
