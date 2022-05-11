# 1次元配列を2行3列の配列に変換する
import numpy as np


data = [1, 2, 3, 4, 5, 6]
a = np.array(data)    # リストから配列を作る
print(a)
a = a.reshape(2, 3)    # 2行3列の配列にする
print(a)
