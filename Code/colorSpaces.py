import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('D:\OpenCV\Photos\park.jpg')
cv.imshow('Park', img)

# plt.imshow(img)
# plt.show()

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('GRAY', gray)

# BGR to HSV (Hue Space Value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (L*a*b*) color space
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)

# HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV -> BGR', hsv_bgr)

plt.imshow(rgb)
plt.show()

cv.waitKey(0)