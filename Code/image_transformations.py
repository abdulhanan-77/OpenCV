import cv2 as cv
import numpy as np

img = cv.imread('D:\OpenCV\Photos\group 1.jpg')

cv.imshow('Group', img)

# Translation
def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x -> Left
# -y -> Up
# x -> Right
# y -> Down
translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

# Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width // 2, height // 2)
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)
    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated', rotated_rotated)

# Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 1)
cv.imshow('Flipped', flip)

# Croping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

# Scaling
def scale(img, scaleFactor):
    dimensions = (int(img.shape[1] * scaleFactor), int(img.shape[0] * scaleFactor))
    return cv.resize(img, dimensions, interpolation=cv.INTER_AREA)

scaled = scale(img, 0.5)
cv.imshow('Scaled', scaled)

cv.waitKey(0)

