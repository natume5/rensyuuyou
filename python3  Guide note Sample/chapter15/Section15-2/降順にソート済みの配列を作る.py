# 降順にソート済みの配列を作る
import numpy as np


a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
a_descend = np.sort(a)[::-1]    # ソートした後で逆順にスライスする
print(a_descend)
