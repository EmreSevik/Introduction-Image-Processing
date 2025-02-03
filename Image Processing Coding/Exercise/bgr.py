import cv2

resim123=cv2.imread("logo.jpg")
(blue,green,red)=resim123[125,122]
print("Red {} Green {} Blue {}".format(red,green,blue))