# 偶数、奇数に分ける
import numpy as np


a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
print(a[a%2 == 0])    # 偶数  2で割った余りが0の値を抽出
print(a[a%2 == 1])    # 奇数
