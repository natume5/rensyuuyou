# 2x3の配列に行を追加する
import numpy as np


a = np.array([ 1, 2, 3, 4, 5, 6]).reshape(2, 3)
print(a)

b = np.append(a, [[7, 8, 9]], axis=0)
# [[7, 8, 9]]  配列aに合わせて2次元配列で追加する
# axis=0  行を追加する
print(b)
"""
配列に要素を追加する
append(配列, 値, axis=None)
append(配列, リスト, axis=None)
append(配列, タプル, axis=None)
"""
