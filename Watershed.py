import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


folder = 'C:/Users/Tacha/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'coins1.jpg', cv.IMREAD_GRAYSCALE)
img_color = cv.imread(folder + 'coins1.jpg')

ret, thresh = cv.threshold(img, 0, 255, cv.THRESH_BINARY_INV+cv.THRESH_OTSU)

## Noise removal
kernel = np.ones((3,3), np.uint8)
opening = cv.morphologyEx(thresh, cv.MORPH_OPEN, kernel, iterations=2)

## Sure foregroung with Distance transform
sure_fg = cv.distanceTransform(opening, cv.DIST_L2, 5)
normalized = cv.normalize(sure_fg, sure_fg, 0, 255, cv.NORM_MINMAX)
sure_fg = np.uint8(sure_fg)
ret, sure_fg = cv.threshold(sure_fg, 0.6*255, 255, cv.THRESH_BINARY)


################################ TUTORIAL
## Sure background 
# sure_bg = cv.dilate(opening, kernel, iterations=3)

# ## Unknown region
# unknown = cv.subtract(sure_bg,sure_fg)

# ## Marker labelling
# ret, markers = cv.connectedComponents(sure_fg)
# markers = markers+1
# markers[unknown == 255] = 0

# ## WATERSHED
# markers = cv.watershed(img_color, markers)
# img_color[markers == -1] = [0,0,255]

# ## SHOW RESULTS
# plt.figure()
# plt.imshow(markers)
# plt.show()
# cv.imshow('Original Image', img_color)
# cv.waitKey(0)

################################ BRIA'S
# ## Internal markers
markers = np.full_like(img, 0)
objects, hierarchy = cv.findContours(sure_fg, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

for i in range(np.shape(objects)[0]):
    cv.drawContours(markers, objects, i, i+1, cv.FILLED)

## External markers
external_marker_mask = cv.erode(~opening, cv.getStructuringElement(cv.MORPH_RECT, (3,3)))
markers[external_marker_mask.astype(bool)] = np.shape(objects)[0] + 1

## WATERSHED
markers = cv.watershed(img_color, markers.astype(np.int32))

# ## FOR VISUALIZATION
img_color[markers == -1] = [0,0,255]

# ## SHOW RESULTS
cv.imshow("Image",img_color)
cv.waitKey(0)
