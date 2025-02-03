import cv2


image=cv2.imread("Bursaspor-amblem.png",0)
horizontal_flip=cv2.flip(image,0)
vertical_flip=cv2.flip(image,1)
all_flip=cv2.flip(image,-1)
cv2.imshow("Horizontal_flip",horizontal_flip)
cv2.imshow("Vertical_flip",vertical_flip)
cv2.imshow("All_flip",all_flip)
cv2.imshow("Original",image)


cv2.waitKey(0) 