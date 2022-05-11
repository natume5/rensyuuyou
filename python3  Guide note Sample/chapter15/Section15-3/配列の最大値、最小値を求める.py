# 配列の最大値、最小値を求める
import numpy as np


A = np.array([56, 45, 83, 67, 59, 41]).reshape(2, 3)
print(A.max())    # 全体の最大値
print(A.max(0))    # 各列の最大値
print(A.max(1))    # 各行の最大値
print(A.min())    # 全体の最小値
print(A.min(0))    # 各列の最小値
print(A.min(1))    # 各行の最小値
print(A.mean())    # 全体の平均
print(A.mean(0))    # 各行の平均値
print(A.mean(1))    # 各列の平均値
