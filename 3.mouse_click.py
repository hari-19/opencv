import cv2
import numpy as np

def click_event(event, x, y, flags, param):
    if event is cv2.EVENT_FLAG_LBUTTON:
        b = img[y, x, 0]
        g = img[y, x, 1]
        r = img[y, x, 2]
        img2 = np.zeros((512, 512, 3), np.uint8)
        img2[:] = [b, g, r]
        cv2.imshow('colour', img2)



points = []

img = cv2.imread('lena.jpg', 1)
# img2 = img.copy()
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)

if cv2.waitKey(0) == ord("q"):
    cv2.destroyAllWindows()
