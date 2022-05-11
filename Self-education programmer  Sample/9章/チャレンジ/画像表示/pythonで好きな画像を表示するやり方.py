# -*- coding:utf-8 -*-
import cv2
import numpy as np

# 画像を入力
img = cv2.imread('画像をを入力してください: ')
# 画像の読み込み
gazou = cv2.imread(img)

cv2.namedWindow("img", cv2.WINDOW_KEEPRATIO | cv2.WINDOW_NORMAL)
# 画像の表示
cv2.imshow("img", gazou)
cv2.waitKey()
