import numpy as np
import cv2 as cv

folder = 'C:/Users/hoyte/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'noisyimage1.png', cv.IMREAD_GRAYSCALE)

## COPY IMAGE
img_restored = img.copy()

## CALLBACK FUNCTION
def saltPepperDenoise(size):
    if size % 2 == 1:
        img_restored = cv.medianBlur(img, size)
        cv.imshow(title, img_restored)


## CREATE WINDOW
title = 'Salt and pepper correction'
cv.namedWindow(title)

## CREATE TRACKBAR
trackbarName = 'kernel size'
cv.createTrackbar(trackbarName, title, 0, 30, saltPepperDenoise)
size = cv.getTrackbarPos(trackbarName, title)

saltPepperDenoise(size)

cv.waitKey(0)
cv.destroyAllWindows()

