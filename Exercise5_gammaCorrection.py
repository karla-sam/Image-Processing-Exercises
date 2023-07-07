import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

folder = 'C:/Users/Tacha/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'lowcontrast.png', cv.IMREAD_UNCHANGED)

## Copy image
out = img.copy()

## TRACKBAR FUNCTION
def gammaCorrectionFunc(pos):
    gamma = pos /10.0
    c = 255**(1-gamma)
    
    for i in range (0, out.shape[0]):
        for j in range (0, out.shape[1]):
            out[i][j] = c * img[i][j] ** gamma
    
    cv.imshow(title, out)

## CREATE WINDOW
title = 'Gamma correction'
cv.namedWindow(title)

## CREATE TRACKBAR
trackbarName = 'gamma'
cv.createTrackbar(trackbarName, title, 0, 100, gammaCorrectionFunc)
gamma10 = cv.getTrackbarPos(trackbarName, title)

## CALL FUNCTION
gammaCorrectionFunc(gamma10)

cv.waitKey(0)
cv.destroyAllWindows()
