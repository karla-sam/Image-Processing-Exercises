import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt

folder = 'C:/Users/Tacha/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'pills2.png', cv.IMREAD_UNCHANGED)

Z = img.reshape((-1,3))
Z = np.float32(Z)



cv.imshow('Image', img)
cv.waitKey(0)