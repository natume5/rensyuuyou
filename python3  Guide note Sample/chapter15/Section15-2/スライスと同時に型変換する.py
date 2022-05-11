# スライスと同時に型変換する
import numpy as np


data = [2.1, 3.5, 2.5, 4.3, 5.1, 1.6]
a = np.array(data).reshape(3, 2)
print(a)    # 2.1~4.3の2行をを取り出したい
a2 = a[:2,].astype(int)    # 最初の2行を取り出す際に整数に変換
print(a2)    # 値は整数に変換されている
