# 1次元配列を2行3列の配列に変換する2
import numpy as np


data = [1, 2, 3, 4, 5, 6]
a = np.array(data).reshape(2, 3)     # 1行で書くことが出来る
print(a)
