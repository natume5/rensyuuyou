import cv2
import numpy as np

img = cv2.imread('')   # もちろん読み取れないよ
cv2.imshow('image', img)

img = cv2.imread("index.jpg")
cv2.imshow("image", img)
cv2.waitKey()
