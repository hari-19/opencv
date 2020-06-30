import cv2
from matplotlib import pyplot as plt
import numpy as np

def nothing(x) :
    pass


img = cv2.imread('resources/sudoku.png', 0)

cv2.namedWindow("Tracking")
cv2.createTrackbar("Block Size", "Tracking", 3, 100, nothing)
cv2.createTrackbar("C", "Tracking", 3, 100, nothing)

while True:
    bs = cv2.getTrackbarPos("Block Size", "Tracking")
    c = cv2.getTrackbarPos("C", "Tracking")

    if bs%2 == 0:
        bs = bs+1

    if bs <= 1:
        bs = 3

    th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, bs, c)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, bs, c)

# images = np.append(img, th1, axis=1)
# images = np.append(images, th2, axis=1)
    cv2.imshow("Image", img)
    cv2.imshow("th1", th1)
    cv2.imshow("th2", th2)

# cv2.imshow("IMG",images)
    k = cv2.waitKey(1)
    if k == ord("q"):
        cv2.destroyAllWindows()
        break
# titles = ["Image", "Mean", "Gaussian"]
# images = [img, th1, th2]
# n = len(images)
#
# if n < 3:
#     col = n
#     row = 1
# else:
#     row = n/3
#     col = 3
#
# for i in range(n):
#     plt.subplot(row, col, i+1)
#     plt.imshow(images[i], "gray")
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])

# plt.show()