# 3行3列の配列の要素にアクセスする
import numpy as np


data = [10, 20, 30, 40, 50, 60, 70, 80, 90]
a = np.array(data).reshape(3, 3)    # 3行3列の配列に変換する
print(a)
print(a[0, 0])    # a[0][0]と同じ
print(a[1, 0])    # a[1][0]と同じ
print(a[1, 1])    # a[1][1]と同じ
print(a[2, -1])    # a[2][-1]と同じ
