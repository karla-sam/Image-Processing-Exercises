import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

folder = 'C:/Users/hoyte/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'galaxy.jpg', cv.IMREAD_UNCHANGED)

def myCountNonZero(multichanImg):
    b,g,r = cv.split(multichanImg)
    result = cv.countNonZero(b) + cv.countNonZero(g) + cv.countNonZero(r)
    return result

marker = cv.morphologyEx(img, cv.MORPH_OPEN, cv.getStructuringElement(cv.MORPH_ELLIPSE, (37,37)))

marker_cur = marker
mask = img
iter = 0

while True:
    marker_prev = marker_cur.copy()

    marker_cur = cv.dilate(marker_cur, cv.getStructuringElement(cv.MORPH_RECT, (3,3)))
    marker_cur = cv.min(marker_cur, mask)

    #print("Iteration" + str(iter) + "\n\n")
    iter += 1

    if myCountNonZero(marker_cur - marker_prev) == False:
        break

cv.imshow("Reconstructed image", marker_cur)
cv.imshow("Stars image", mask - marker_cur)
cv.waitKey(0)