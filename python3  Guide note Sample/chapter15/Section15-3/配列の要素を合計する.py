# 配列の要素を合計する
import numpy as np


A = np.array([56, 45, 83, 67, 59, 41]).reshape(2, 3)
print(A)
print(A.sum())    # 全体の合計
print(A.sum(0))    # 各列の合計
print(A.sum(1))    # 各行の合計
