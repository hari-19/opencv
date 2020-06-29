import cv2
# import numpy as np


def click_event(event, x, y, flags, param):
    if event is cv2.EVENT_FLAG_LBUTTON:
        cv2.putText(img, "Mouse Clicked", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.imshow('image', img)

    if event is cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img, (x, y), 3, (255, 255, 255), -1)
        points.append((x, y))
        if len(points) >= 2 :
            cv2.line(img, points[-1], points[-2], (255, 255, 255))
        cv2.imshow('image', img)


points = []

img = cv2.imread('lena.jpg', 1)
# img2 = img.copy()
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
