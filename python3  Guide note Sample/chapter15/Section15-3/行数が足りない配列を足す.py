# 行数が足りない配列を足す
import numpy as np


A = np.array([1, 2, 3, 4]).reshape(2, 2)
print(A)    # 2行2列の配列
B = np.array([100, 200])    # 1行2列の配列
print(B)
C = A + B    # 行数が足りない配列を足す
print(C)
