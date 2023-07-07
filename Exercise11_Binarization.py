import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

folder = 'C:/Users/hoyte/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'tools.png', cv.IMREAD_GRAYSCALE)

## CALCULATE AND SHOW HISTOGRAM
hist = cv.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.xlim([0,256])
plt.ylim([0, max(hist)+1])
plt.show()

## OTSU: not a good choice since histogram is not bimodal
ret, imgOtsu = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

## TRIANGLE: Better choice since dark background is dominant
ret2, imgTri = cv.threshold(img, 0, 255, cv.THRESH_BINARY+cv.THRESH_TRIANGLE)

cv.imshow('Original Image', img)
cv.imshow('Image with Otsu', imgOtsu)
cv.imshow('Image with Triangle', imgTri)
cv.waitKey(0)
