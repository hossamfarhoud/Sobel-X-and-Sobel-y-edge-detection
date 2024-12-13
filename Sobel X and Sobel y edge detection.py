import cv2

import numpy as np

from matplotlib import pyplot as plt



img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)

lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)

lap = np.uint8(np.absolute(lap))

sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)

sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)



sobelX = np.uint8(np.absolute(sobelX))

sobelY = np.uint8(np.absolute(sobelY))



sobelCombined = cv2.bitwise_or(sobelX, sobelY)



cv2.imshow('img', img)
cv2.imshow('laplacian image', lap)
cv2.imshow('sobel_X', sobelX)
cv2.imshow('sobel_y', sobelY)
cv2.imshow('combine_sobel_X_and_y', sobelCombined)
   
cv2.waitKey(0)
cv2.destroyAllWindows()

