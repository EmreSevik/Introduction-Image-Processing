import cv2

print(cv2.__version__)

image = cv2.imread('logo.jpg')
print(image)
cv2.imshow('Image', image)
cv2.waitKey(0)