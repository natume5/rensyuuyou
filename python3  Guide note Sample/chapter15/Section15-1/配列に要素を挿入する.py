# 配列に要素を挿入する
import numpy as np


a = np.array([0, 1, 2])
b = np.insert(a, 1, 99)    # 配列aのインデックス1の位置に99を挿入する
print(b)    # 新しい配列bが作られる
"""
配列に要素を挿入する
insert(配列, 位置, 値, axis=None)
insert(配列, 位置, リスト, axis=None)
insert(配列, 位置, タプル, axis=None)
"""
