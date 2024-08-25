import cv2 as cv

img = cv.imread('D:\OpenCV\Photos\cats.jpg')
cv.imshow('Cats', img)

# Averaging 
average = cv.blur(img, (7,7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gaussian = cv.GaussianBlur(img, (7,7), 0)
cv.imshow('Gaussian Blur', gaussian)

# Median Blur
median = cv.medianBlur(img, 7)
cv.imshow('Median Blur', median)

# Bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blur', bilateral)

cv.waitKey(0)