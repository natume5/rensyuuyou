# reshape()で作った配列bを変更すると元の配列aも変更される
import numpy as np


a = np.array([10, 20, 30, 40])
b = a.reshape(2, 2)
print(a is b)    # 同じオブジェクトではない
b[0, 0] = 99    # 配列bの要素を99に書き替える
print(b)
print(a)    # 配列aの要素も99に書き替わる
