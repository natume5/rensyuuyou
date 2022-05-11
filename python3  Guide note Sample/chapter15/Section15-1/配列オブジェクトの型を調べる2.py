# 配列オブジェクトの型を調べる
import numpy as np


a = np.array([1, 2, 3])
print(a.dtype)    # 要素の型
"""
本ではa.dtypeはdtype('int64')と出ているが
コマンドプロンプトで入力したらint32と表示された。
"""
