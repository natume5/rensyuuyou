# 多次元配列から5より大きな値を抽出する
import numpy as np


a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
b = a.reshape(4, 4)    # 4x4の配列にする
print(b)
print(b[b>5])    # 4x4の配列から5より大きな値を抽出する
