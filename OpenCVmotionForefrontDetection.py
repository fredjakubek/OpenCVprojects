""" Description: Uses OpenCV to visually eliminate non-moving objects contained
within the video file, displaying moving items within the video-file in a vivid
white color for better recognition.
Enables better video-analysis for applications such as object-detection in
moving images. 
"""
import cv2
import numpy as np

cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
	ret, frame = cap.read()
	fgmask= fgbg.apply(frame)

	cv2.imshow('original', frame)
	cv2.imshow('fg', fgmask)

	k= cv2.waitKey(30) & 0xff
	if k==27:
		break

cap.release()
cv2.destroyAllWindows()
