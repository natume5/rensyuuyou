# 行列A、Bの要素が同じかどうか比較する
import numpy as np


A = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
B = np.array([1, 2, 9, 4, 8, 6]).reshape(2, 3)    # 2行3列の配列を作る
print(A)
print(B)
C = (A == B)     # AとBを比較した結果の配列Cを作る
print(C)
