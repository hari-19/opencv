import cv2
from matplotlib import pyplot as plt
import math


img = cv2.imread('resources/gradient.png', 1)

_,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
_,th2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
_,th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
_,th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
_,th5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ["Image", "Binary", "Binary Inverse", "Trunc", "To Zero", "To Zero inv"]
images = [img, th1, th2, th3, th4, th5 ]
n = len(images)

if n < 3:
    col = n
    row = 1
else:
    row = math.ceil(n/3)
    col = 3

for i in range(n):
    plt.subplot(row, col, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()