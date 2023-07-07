import numpy as np
import cv2 as cv

folder = 'C:/Users/Tacha/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'lena.png', cv.IMREAD_UNCHANGED)

print(img.shape)
cv.imshow('Image', img)
cv.waitKey(0)
