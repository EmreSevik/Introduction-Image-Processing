import cv2

image=cv2.imread("Bursaspor-amblem.png")
width=500
height=500
center=(width/2,height/2)
d=cv2.getRotationMatrix2D(center,-30,1)
rotating=cv2.warpAffine(image,d,(width,height))
cv2.imshow("rotating",rotating)
cv2.imshow("Original",image)
cv2.waitKey(0)