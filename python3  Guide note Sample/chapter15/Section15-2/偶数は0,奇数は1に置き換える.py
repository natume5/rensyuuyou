# 偶数は0,奇数は1に置き換える
import numpy as np


a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
a = a.reshape(4, 4)
print(a)

a[a%2 == 0] = 0    # 偶数を0に置き換える

print(a)

a[a%2 == 1] = 1    # 偶数を1に置き換える

print(a)
