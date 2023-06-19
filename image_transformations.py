import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# translation
def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# Rotation
def rotate(img, angle, rotPoint = None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


img = cv.imread('../content/cat_edited.jpg')
frame_resized = rescaleFrame(img)
cv.imshow('Cat', frame_resized)

translated = translate(frame_resized, 100, 100)
# cv.imshow('translated', translated)

rotated = rotate(frame_resized, 45)
# cv.imshow('Rotated', rotated)

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
# cv.imshow('Resized', resized)

flip = cv.flip(frame_resized, 1)
# cv.imshow('Flip', flip)

cropped = frame_resized[200:400, 300:400]
cv.imshow('cropped', cropped)

cv.waitKey(0)