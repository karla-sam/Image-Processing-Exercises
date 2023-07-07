import numpy as np
import cv2 as cv

folder = 'C:/Users/hoyte/Documents/MAIA/SECOND SEMESTER/Advanced Image Analysis/Exercises/Images/'
img = cv.imread(folder + 'tools.bmp', cv.IMREAD_UNCHANGED)
imgCopy = img.copy()

## CONVERT TO GRAYSCALE
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

## CLICK FUNCTION
def objPicking(event, x, y, int, userdata):
    if (event == cv.EVENT_LBUTTONDOWN):
        for i in range (0, len(filteredObjects)):
            if cv.pointPolygonTest(filteredObjects[i], (x, y), False) > 0:
                cv.drawContours(imgCopy, filteredObjects, i, (0,255,0), cv.FILLED, cv.LINE_AA)
    cv.imshow(winName, imgCopy)

## THRESHOLDING WITH TRIANGLE METHOD
ret, imgTri = cv.threshold(imgGray, 0, 255, cv.THRESH_BINARY+cv.THRESH_TRIANGLE)

## FIND CONTOURS
objects, hierarchy = cv.findContours(imgTri, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)


## FILTERING OBJECTS
filteredObjects = []
for i in range (0, len(objects)):
    area = cv.contourArea(objects[i])
    if area > 100:
        filteredObjects.append(objects[i])
print(filteredObjects)
## CREATE WINDOW AND CALL FUNCTION
winName = 'Contoured Img'
cv.namedWindow(winName)
cv.setMouseCallback(winName, objPicking)
objPicking(0,0,0,0,0)

cv.waitKey(0)
