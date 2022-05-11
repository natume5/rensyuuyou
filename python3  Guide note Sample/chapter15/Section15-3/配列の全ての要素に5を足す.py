# 配列の全ての要素に5を足す
import numpy as np


A = np.array([10, 20, 30, 40]).reshape(2, 2)
print(A)

B = A + 5    # 配列に5を足す
print(B)    # すべての要素に5が足される
