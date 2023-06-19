import cv2 as cv

def rescaleFrame(frame, scale=0.1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('../content/man_with_phone.jpeg')
frame_resized = rescaleFrame(img)
# cv.imshow('Man with phone', frame_resized)

gray = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(frame_resized, 125, 125)
cv.imshow('Canny Edges', canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

cv.waitKey(0)