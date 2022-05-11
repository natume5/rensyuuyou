# -*- coding: utf-8 -*-
import cv2
# 画像を読み込む
img = cv2.imread("img.jpg")
# ウィンドウの名前を設定
cv2.namedWindow('gui', cv2.WINDOW_NORMAL)
# ウィンドウの名前を選択して画像を表示
cv2.imshow('gui', img)
# 入力待ち
cv2.waitKey(0)
