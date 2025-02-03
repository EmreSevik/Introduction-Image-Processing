import cv2
import numpy as np

img = cv2.imread('live.jpg')

kernel = np.ones((5,5), np.uint8)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
canny = cv2.Canny(img, 50, 150)
dilation = cv2.dilate(canny, None, iterations=2)

img2 = np.zeros((512, 512, 3), np.uint8)

cv2.line(img2, (0, 0), (511, 511), (0, 0, 255), 3)

cv2.rectangle(img2, (100, 100), (400, 400), (0, 0, 255), 3)
cv2.putText(img2,"OPENCV",(40,40),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)

h, w, _ = img.shape
img2_resized = cv2.resize(img2, (w, h))
canny_resized = cv2.resize(canny, (w, h))
dilation_resized = cv2.resize(dilation, (w, h))
blur_resized = cv2.resize(blur, (w, h))
gray_resized = cv2.resize(gray, (w, h))

horizontal = np.hstack((img, img2_resized, cv2.cvtColor(canny_resized, cv2.COLOR_GRAY2BGR),
                        cv2.cvtColor(dilation_resized, cv2.COLOR_GRAY2BGR),
                        cv2.cvtColor(blur_resized, cv2.COLOR_GRAY2BGR),
                        cv2.cvtColor(gray_resized, cv2.COLOR_GRAY2BGR)))
cv2.imshow('horizontal',horizontal)
cv2.waitKey(0)
cv2.destroyAllWindows()
