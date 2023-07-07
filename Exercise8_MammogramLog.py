import numpy as np
import cv2 as cv
import math

folder = 'C:/Users/hoyte/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'raw_mammogram.tif', cv.IMREAD_GRAYSCALE)

## RESIZE IMAGE
width = int(img.shape[1]*0.4)
height = int(img.shape[0]*0.4)
dim = (width, height)
img = cv.resize(img, dim)

## DETERMINE BIT DEPTH
if img.dtype == 'uint8':
    depth = 8
elif img.dtype == 'uint16':
    depth = 16
else:
    print('Error, bit depth is different than 8 or 16')

## ESTABLISH L AND C
L = 2**depth
c = (L-1)/math.log(L)

# LOG TRANSFORMATION
for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        img[i][j] = c * math.log(1 + img[i][j])

img = (L-1) - img

## SHOW THE IMAGE
cv.imshow('Image', img)
cv.waitKey(0)