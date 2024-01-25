import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('camera window', grey)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imshow('camera window', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break
    
    

cap.release()
cv2.destroyAllWindows()