#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- NumPy入門 ベクトルの演算 ---")


print("--- ベクトルの演算 ---")


"""
加法、スカラー倍、内積、外積は以下の方法で計算することが可能です。

ndarrayの演算

ndarrayには演算が定義されていて、
+、-でベクトルの加減演算を行うことができます。
また、*、/で要素ごとに積・商（いわゆるアダマール積）を計算することができます。
"""

import numpy as np


x = np.array([1, 2, 3])
y = np.array([4, 5, 6])

print(x + y)

print(x - y)

print(x * y)

print(x / y)

"""
[5 7 9]
[-3 -3 -3]
[ 4 10 18]
[0.25 0.4  0.5 ]


スカラー倍

*演算子で定数を作用させるとスカラー倍することができます。
"""

x = np.array([1, 2, 3])
a = 100

print(x * a)

print(a * x)

"""
[100 200 300]
[100 200 300]


内積

np.dotで内積を計算することができます。
例えば以下のサンプルでは直行する基底の内積が0になることが確認できます。
"""

import numpy as np

e1 = np.array([1, 0, 0])
e2 = np.array([0, 5, 0])

print(np.dot(e1, e2))    # 0

"""
クロス積

最後にクロス積(=外積)です。numpy.crossで求めることができます。
"""

import numpy as np

e1 = np.array([1, 0, 0])
e2 = np.array([0, 5, 0])

print(np.cross(e1, e2))

print(np.cross(e2, e1))

"""
[0 0 5]
[ 0  0 -5]

上のサンプルでは結果が法線ベクトルになっていることが分かります。
"""
