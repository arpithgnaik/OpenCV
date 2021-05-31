import cv2
import numpy as np

img=cv2.imread("Resources/Lenna.png")

imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#color image to grayscale image
imgBlur=cv2.GaussianBlur(imgGray,(7,7),0)

imgCanny=cv2.Canny(img,150,200)#Edge Detection

kernel=np.ones((5,5),np.uint8)
imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)

imgErode=cv2.erode(imgDialation,kernel,iterations=1)

cv2.imshow("Gray Image", imgGray)
cv2.imshow("Blur Image", imgBlur)
cv2.imshow("Edge Detector Image", imgCanny)
cv2.imshow("Dialated Image", imgDialation)
cv2.imshow("Eroded Image", imgErode)


cv2.waitKey(0)