import cv2

x = cv2.imread('lena.jpg', 1)
cv2.imshow('image-Lena', x)
cv2.waitKey(500)
#print(x)