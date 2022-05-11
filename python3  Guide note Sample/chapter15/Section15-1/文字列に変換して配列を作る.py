# 文字列に変換して配列を作る
import numpy as np


d = np.array([1, 1.5, 2], dtype="<U")    # 文字列型で作る
print(d)

e = np.array([9.123, 10.5, 12.11], dtype="<U4")
# 9.123は→"9.12"　12.11は→"12.1"  4文字に詰まる
print(e)
