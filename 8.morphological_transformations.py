import cv2
from matplotlib import pyplot as plt
import numpy as np
import math


img = cv2.imread('resources/j.png', 0)
kernel = np.ones((5, 5), np.uint8)

erosion = cv2.erode(img, kernel, iterations=1)
dilation = cv2.dilate(img, kernel, iterations=1)
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)


titles = ["Image", "Erosion", "Dilation", "Opening", "Closing", "Gradient", "Top Hat", "Black Hat"]
images = [img, erosion, dilation, opening, closing, gradient, tophat, blackhat]
n = len(images)

if n < 3:
    col = n
    row = 1
else:
    row = math.ceil(n/3)
    col = 3

for i in range(n):
    plt.subplot(row, col, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()