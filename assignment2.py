# face detection

import cv2 as cv

def rescaleFrame(frame, scale=0.15):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('../content/man_with_multiple_men.jpeg')
frame_resized = rescaleFrame(img)
# cv.imshow('Man with phone', frame_resized)

# gray = cv.cvtColor(frame_resized, cv.COLOR_BGR2GRAY)
cv.imshow('Gray man with phone', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(frame_resized, scaleFactor = 1.1, minNeighbors = 3)
print('Number of faces found = ', {len(faces_rect)})

for (x, y, w, h) in faces_rect:
    cv.rectangle(frame_resized, (x, y), (x+w, y+h), (0, 255, 0), thickness = 1)

cv.imshow('Detected faces ', frame_resized)
cv.waitKey(0)