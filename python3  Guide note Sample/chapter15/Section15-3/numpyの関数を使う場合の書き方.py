# numpyの関数を使う場合の書き方
import numpy as np


A = np.array([56, 45, 83, 67, 59, 41]).reshape(2, 3)
print(np.sum(A))    # Aの合計値
print(np.max(A, 1))    # Aの各行の最大値
