import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

folder = 'C:/Users/hoyte/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'retina.png', cv.IMREAD_UNCHANGED)

## Mean Shift Filtering
img_filtered = cv.pyrMeanShiftFiltering(img, 3, 30)

cv.imshow('Image Original', img)
cv.imshow('Image Filtered', img_filtered)
cv.waitKey(0)