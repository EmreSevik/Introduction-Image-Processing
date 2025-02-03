import numpy as np
import cv2
import pytesseract
import imutils

img = cv2.imread('plaka.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filter=cv2.bilateralFilter(gray,9,100,100)
corner=cv2.Canny(filter,100,200)

contour,a=cv2.findContours(corner,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt=imutils.grab_contours((contour,a))
cnt=sorted(cnt,key=cv2.contourArea,reverse=True)[:10]

ekran=0
for i in cnt:
    eps=0.018*cv2.arcLength(i,True)
    approx=cv2.approxPolyDP(i,0.018*cv2.arcLength(i,True),True)
    if len(approx)==4:
        ekran=approx
        break

mask=np.zeros(gray.shape,np.uint8)
new_mask=cv2.drawContours(mask,[ekran],0,255,-1)

writing=cv2.bitwise_and(img,img,mask=new_mask)

(x,y)=np.where(new_mask==255)
(highx,highy)=(np.min(x),np.min(y))
(lowx,lowy)=(np.max(x),np.max(y))
cut=gray[highx:lowx-1,highy:lowy+1]

text=pytesseract.image_to_string(cut,lang='eng')
print(text)


cv2.imshow('filter', filter)
cv2.imshow('gray', gray)
cv2.imshow('newmask', new_mask)
cv2.imshow('writing', writing)
cv2.imshow('cut', cut)

cv2.waitKey(0)
cv2.destroyAllWindows()


