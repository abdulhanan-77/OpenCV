import cv2 as cv

img = cv.imread('D:\OpenCV\Photos\park.jpg')
cv.imshow('Cat', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)

# Dialating the image
dilated = cv.dilate(canny, (5, 5), iterations=2)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (5,5), iterations=2)
cv.imshow('Eroded', eroded)

# Resize
resized = cv.resize(img, (500, 500), interpolation = cv.INTER_AREA)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)