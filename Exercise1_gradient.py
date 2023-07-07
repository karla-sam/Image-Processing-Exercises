import numpy as np
import cv2 as cv
import time

start = time.time()
blank = np.zeros((400,600), np.uint8)


for rows in range(0, blank.shape[0]):
    for cols in range(0, blank.shape[1]):
        blank[rows][cols] = rows/blank.shape[0]*255

cv.imshow("Image", blank)

end = time.time()
print(end-start)

cv.waitKey(0)

