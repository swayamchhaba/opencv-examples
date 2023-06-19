# Create a program using opencv to read a video file in mp4 format (you can record YOUR OWN SELF using 
# any video recorder like media player) and display the frames.

import cv2 as cv

# This part of the code is for resizing the frame by default of 0.2 times
def rescaleFrame(frame, scale=0.2):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# reading an image and showing it here
# img = cv.imread('../content/cat_edited.jpg')
# frame_resized = rescaleFrame(img)
# cv.imshow("cat", frame_resized)
# cv.waitKey(0)

#reading a video and playing it here
capture = cv.VideoCapture('../content/man_with_dog.mp4')
while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)
    # cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()