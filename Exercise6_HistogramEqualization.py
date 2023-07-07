import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

folder = 'C:/Users/Tacha/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'lowcontrast.png', cv.IMREAD_GRAYSCALE)

## EQUALIZE IMAGE
equalized = cv.equalizeHist(img)

## GET HISTOGRAMS
hist = cv.calcHist([img], [0], None, [256], [0,256])
histEq = cv.calcHist([equalized], [0], None, [256], [0,256])

## PLOT HISTOGRAMS OF ORIGINAL AND EQUALIZED IMAGE
plt.subplot(1,2,1)
plt.plot(hist)
plt.xlim([0,256])
plt.subplot(1,2,2)
plt.plot(histEq)
plt.xlim([0,256])
plt.show()

cv.imshow('Original Image', img)
cv.imshow('Equalized Image', equalized)
cv.waitKey(0)