# 5以上の奇数
import numpy as np


a = np.array([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3])
print(a[(a>=5) & (a%2 == 1)])    # 論理積(5以上かつ奇数)
