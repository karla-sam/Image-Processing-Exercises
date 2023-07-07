import numpy as np
import cv2 as cv

img = np.zeros((512,512,3), dtype='uint8')


img[:, 0:img.shape[1]//3] = 0,255,0
img[:, img.shape[1]//3:img.shape[1]//3*2] = 255,255,255
img[:, img.shape[1]//3*2:img.shape[1]] = 0,0,255

cv.imshow('Italy', img)
cv.waitKey(0)
cv.destroyAllWindows