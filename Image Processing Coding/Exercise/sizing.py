import cv2

image=cv2.imread("logo.jpg")
size=(800,800)
sizing_image=cv2.resize(image,size)
cv2.imshow("Sizing Image",sizing_image)
cv2.waitKey(0)