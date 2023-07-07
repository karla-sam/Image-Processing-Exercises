from cv2 import CV_8U
import numpy as np
import cv2 as cv

folder = 'C:/Users/hoyte/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'eye.blurry.png', cv.IMREAD_UNCHANGED)

## COPY IMAGE
img_sharpened = img.copy()

## CALLBACK FUNCTION
def sharpenLaplacian(k10):
    k = k10 /10.0
    kernel = np.array([[-k, -k, -k], [-k, 1+8*k, -k], [-k, -k, -k]])
    img_sharpened = cv.filter2D(img, CV_8U, kernel)
    cv.imshow(title, img_sharpened)

## CREATE WINDOW
title = 'Sharpening'
cv.namedWindow(title)

## CREATE TRACKBAR
trackbarName = 'k'
cv.createTrackbar(trackbarName, title, 0, 100, sharpenLaplacian)
k10 = cv.getTrackbarPos(trackbarName, title)

sharpenLaplacian(k10)

cv.waitKey(0)
cv.destroyAllWindows()