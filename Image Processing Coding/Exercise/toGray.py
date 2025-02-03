import cv2

image=cv2.imread("Bursaspor-amblem.png")
cv2.imshow("Original",image)
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray_image)
cv2.waitKey(0)