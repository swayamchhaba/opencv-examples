import cv2 as cv

def rescaleFrame(frame, scale=0.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('../content/man_with_phone.jpeg')
frame_resized = rescaleFrame(img)
cv.imshow('Man with phone', frame_resized)

# BGR to Grayscale
gray = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
cv.imshow('Man with phone gray', gray)

# BFR to HSV
hsv = cv.cvtColor(frame_resized, cv.COLOR_BGR2HSV)
cv.imshow('Man with phone HSV', hsv)

# BGR to L*a*b
lab = cv.cvtColor(frame_resized, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

cv.waitKey(0)