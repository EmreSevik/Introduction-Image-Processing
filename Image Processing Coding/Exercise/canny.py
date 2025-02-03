import cv2

image=cv2.imread("Bursaspor-amblem.png",0)
edge=cv2.Canny(image,45,150)
cv2.imshow("Original",image)
cv2.imshow("Canny",edge)
cv2.waitKey(0)