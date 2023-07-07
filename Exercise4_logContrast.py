import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt
import math


def resizedImage(image, scale):
  width = int(image.shape[1]*scale)
  height = int(image.shape[0]*scale)
  dim = (width, height)
  imgresized = cv.resize(img, dim, interpolation=cv.INTER_AREA)
  return imgresized

folder = 'C:/Users/Tacha/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'raw_mammogram.tif', cv.IMREAD_UNCHANGED)

if img.dtype == 'uint8':
    depth = 8
elif img.dtype == 'uint16':
    depth = 16

# Parameters
L = 2**depth 
c = (L - 1)/math.log(L)


# Logarithmic transformation
for rows in range(0, img.shape[0]):
    for cols in range(0, img.shape[1]):
       img[rows][cols] = c*math.log(img[rows][cols] + 1)

img = (L-1) - img
cv.imshow("Image", resizedImage(img, 0.4))
cv.waitKey(0)