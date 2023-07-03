import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture("myvdeo.mp4")
det=HandDetector(detectionCon=0.5,maxHands=4)

while True:
    success, img = cap.read()
    if not success:
        break
    
    hands,img=det.findHands(img)
    cv2.imshow("video Capture",img)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyWindows()
