import cv2

cap = cv2.VideoCapture(0)

cap.set(4, 1080)
cap.set(3, 1080)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while(True):
    ret, frame = cap.read()
    k = cv2.waitKey(1)
    frame = cv2.line(frame, (0, 0), (255, 255), (255, 255, 255), 5)
    frame = cv2.rectangle(frame, (255, 255), (500,500), (255, 11, 123), -1)
    cv2.imshow('video', frame)
    if k == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
