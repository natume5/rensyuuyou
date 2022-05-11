# 多次元配列のスライス
import numpy as np


data = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
a = np.array(data).reshape(3, 3)
print(a)
print(a[:2,])    # 0~1行目、すべての列
print(a[:,1:])    # すべての行、1行目以降
print(a[1:,1:])    # 1行目以降、1行目以降
