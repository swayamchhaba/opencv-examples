import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow('Blank', blank)

#paint the image in a certain colour
# blank[:] = 0, 255, 0
# cv.imshow('Green', blank)

#draw a rectangle
cv.rectangle(blank, (0, 0), (250, 250,), (0, 255, 0), thickness=2)

#draw a circle
cv.circle(blank, (250, 250), 40, (0, 0, 255), thickness = -1)

#draw a line
cv.line(blank, (0, 0), (45, 45), (255, 0, 0), thickness = 2)

#write text on image
cv.putText(blank, 'Hello World', (255, 255), cv.FONT_HERSHEY_COMPLEX, 1.0, (255, 255, 255), 2)

cv.imshow('circle', blank)

cv.waitKey(0)