import cv2

image=cv2.imread("Bursaspor-amblem.png")
gauss=cv2.GaussianBlur(image,(7,7),0)
cv2.imshow("Original",image)
cv2.imshow("Gauss",gauss)
cv2.waitKey(0)