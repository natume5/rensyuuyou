# 型が混在している配列は作ることが出来ない
import numpy as np

a = np.array([1, 1.5, 2])    # intとfloat
print(a)
# 全てfloatになる
b = np.array(["1", 1.5, 2])    # 文字列と数値
print(b)
# 全て文字列になる
c = np.array([True, False, 1.5])    # 数値論と数値
print(c)
# 全て数値(float)になる
