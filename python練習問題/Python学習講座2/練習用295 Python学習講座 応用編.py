#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- NumPy入門 基本的な線形代数計算 その2 転置・トレース・逆行列・行列式 ---")


print("--- 転置 ---")


"""
プロパティTで行列の転置を取得することができます。
いくつかのサンプルで確認してみましょう。
"""

import numpy as np

a = np.array([1, 2, 3])
print(a.T)

b = np.array([[1], [2], [3]])
print(b)

print(b.T)

c = np.array([[1, 2], [3, 4]])
print(c)

print(c.T)

"""
[1 2 3]

[[1]
 [2]
 [3]]

[[1 2 3]]

[[1 2]
 [3 4]]

[[1 3]
 [2 4]]
"""


print("--- トレース ---")


"""
行列の対角成分の和をトレースと呼びます。
トレースの算出はtraceメソッドを使用します。
"""

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)

print(a.trace())

"""
[[1 2]
 [3 4]]

5

(蛇足な気もしますが)、一般的には正方行列のみに定義されるトレース、
numpyでは1,1成分から斜めに行けるところまで計算します。
例外を期待した実装をすると問題を見過ごしてしまうかもしれません。
"""

import numpy as np

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)

print(b.trace)

c = np.array([[1, 2], [3, 4], [5, 6]])
print(c)

print(c.trace)

"""
[[1 2 3]
 [4 5 6]]

<built-in method trace of numpy.ndarray object at 0x000001D8639A36F0>

[[1 2]
 [3 4]
 [5 6]]

<built-in method trace of numpy.ndarray object at 0x000001D8639A39F0>
"""


print("--- 逆行列 ---")


"""
linalg.invメソッドで逆行列を求めることができます。
"""

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)

a_inv = np.linalg.inv(a)
print(a_inv)

print(np.dot(a, a_inv))

"""
[[1 2]
 [3 4]]

[[-2.   1. ]
 [ 1.5 -0.5]]

[[1.00000000e+00 1.11022302e-16]
 [0.00000000e+00 1.00000000e+00]]

最後の計算で行列の積で
単位行列になることを確認していますが誤差が発生しています。
"""


print("--- 行列式 ---")


"""
行列式はlinalg.detで求めることができます。
"""

import numpy as np

a = np.array([[1, 2], [3, 4]])
print(a)

det_a = np.linalg.det(a)
print(det_a)

"""
[[1 2]
 [3 4]]

-2.0000000000000004

1 * 4 - 2 *3 = -2なのでほぼ正しい値が取得できていることが確認できます。
"""
