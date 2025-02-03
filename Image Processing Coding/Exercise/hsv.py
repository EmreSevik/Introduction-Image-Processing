import cv2

image=cv2.imread("Bursaspor-amblem.png")
cv2.imshow("Original",image)
Hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",Hsv)
cv2.waitKey(0)