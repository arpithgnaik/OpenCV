import cv2

cap=cv2.VideoCapture(0)
cap.set(3,640)#width=640
cap.set(4,480)#height=480
cap.set(10,100)#brightness=100

while True:
    success, vid=cap.read()
    cv2.imshow("Webcam",vid)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break