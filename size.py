import cv2

img=cv2.imread("Resources/Lenna.png")
print(img.shape)    #prints (height,width,channels)
imgResize=cv2.resize(img,(300,300))
print(imgResize.shape)    #prints (height,width,channels)

imgCropped=img[0:200,200:500]

cv2.imshow("Original Image",img)
cv2.imshow("Resized Image",imgResize)
cv2.imshow("Cropped Image",imgCropped)
cv2.waitKey(0)