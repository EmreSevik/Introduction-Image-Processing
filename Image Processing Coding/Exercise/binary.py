import cv2

image=cv2.imread("Bursaspor-amblem.png")
control,binary=cv2.threshold(image,127,255,cv2.THRESH_BINARY)
control,binary2=cv2.threshold(image,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow("1",binary)
cv2.imshow("2",binary2)
cv2.waitKey(0)