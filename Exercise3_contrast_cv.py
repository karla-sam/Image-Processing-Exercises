import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

folder = 'C:/Users/Tacha/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'lowcontrast.png', cv.IMREAD_UNCHANGED)

## Pre-normalization histogram
hist = cv.calcHist([img], [0], None, [256], [0,256])
plt.figure()
plt.title("Histogram before normalization")
plt.xlabel('Pixel intensity')
plt.ylabel('# of pixels')
plt.plot(hist)
plt.xlim([0,256])

cv.imshow("Image pre-normalized", img)

## Normalization using openCV
cv.normalize(img, img, 0, 255, cv.NORM_MINMAX)

## Post-normalization histogram
hist_norm = cv.calcHist([img], [0], None, [256], [0,256])
plt.figure()
plt.title("Histogram after normalization")
plt.xlabel('Pixel intensity')
plt.ylabel('# of pixels')
plt.plot(hist_norm)
plt.xlim([0,256])
plt.show()

## Show image
cv.imshow('Image post-normalized', img)
cv.waitKey(0)
cv.destroyAllWindows()