# 列数が足りない配列を足す
import numpy as np


A = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(A)    # 配列Aは2行3列
B = np.array([10, 20]).reshape(2, 1)
print(B)    # 配列Bは2行1列
C = A + B    # 列数が足りない配列を足す
print(C)    # Bの足りない列を補って計算する
