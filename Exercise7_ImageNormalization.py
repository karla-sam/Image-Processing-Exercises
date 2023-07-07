import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

folder = 'C:/Users/hoyte/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'lowcontrast.png', cv.IMREAD_UNCHANGED)

## IMAGE NORMALIZATION
imgNorm = np.full_like(img, 0)
cv.normalize(img, imgNorm, 0, 255, cv.NORM_MINMAX)

## HISTOGRAM PLOTTING
hist = cv.calcHist(img, [0], None, [256], [0,256])
histNorm = cv.calcHist(imgNorm, [0], None, [256], [0,256])

plt.subplot(1,2,1)
plt.plot(hist)
plt.xlim([0,256])
plt.subplot(1,2,2)
plt.plot(histNorm)
plt.xlim([0,256])
plt.show()

## SHOW IMAGES
cv.imshow('Image Normalized', img)
cv.imshow('Original Image', imgNorm)
cv.waitKey(0)
