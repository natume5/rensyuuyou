# 要素の型を指定して配列を作る
import numpy as np

a = np.array([1, 1.5, 2], dtype=int)    # 整数型で作る
print(a)

b = np.array([1, 2, 3], dtype=float)    # 浮動小数点数で作る
print(b)

c = np.array([1, 1.5, 2], dtype=complex)    # 複素数型で作る
print(c)