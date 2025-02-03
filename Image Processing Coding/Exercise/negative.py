import cv2

image=cv2.imread("Bursaspor-amblem.png")
negative=cv2.bitwise_not(image)
cv2.imshow("Original",image)
cv2.imshow("Canny",negative)
cv2.waitKey(0)