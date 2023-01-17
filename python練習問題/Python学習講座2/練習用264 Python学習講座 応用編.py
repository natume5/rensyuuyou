#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 Seriesの演算 ---")


"""
pandasのSeriesには独自に演算が定義されています。
あまりこのトピックを扱った資料は少ないのですが、
この後学ぶDataFrameの操作でも使用するため、
今後の理解の支えになると思います。
"""


print("--- スカラー演算 ---")


"""
Seriesオブジェクトに対し、スカラーの演算をすることができます。

以下、四則演算のサンプルとなります。
"""

import pandas as pd

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

print(s + 10)

print(s - 10)

print(s * 1)

print(s / 2)

"""
a    1
b    2
c    3
d    4
dtype: int64
a    11
b    12
c    13
d    14
dtype: int64
a   -9
b   -8
c   -7
d   -6
dtype: int64
a    1
b    2
c    3
d    4
dtype: int64
a    0.5
b    1.0
c    1.5
d    2.0
dtype: float64

演算が定義されていないオブジェクトをSeriesに格納している場合は
「TypeError: unsupported operand」が発生します。
"""


print("--- Series同士の演算 ---")


"""
Series同士も同様に演算を行うことができます。まずは足し算のサンプルです。
"""

import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

s2 = pd.Series([3, 4, 5, 6], index=['a', 'b', 'c', 'd'])
print(s1 + s2)

"""
a    1
b    2
c    3
d    4
dtype: int64
a     4
b     6
c     8
d    10
dtype: int64

index同士をひも付けて演算が行われます。
試しにindexをずらしてみましょう。
"""

import pandas as pd

s1 = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([3, 4, 5, 6], index=['c', 'd', 'e', 'f'])
print(s1 + s2)

"""
a    NaN
b    NaN
c    6.0
d    8.0
e    NaN
f    NaN
dtype: float64

演算対象の2つのSeries双方にindex設定されていない場合はNaNとなります。
引き算、掛け算、割り算も同様なので説明は割愛します。
"""


print("--- Seriesの論理演算 ---")


"""
最後になりましたが、この後のDataFrameの操作を理解する際に
非常に重要になります。
Seriesには論理演算が定義されていて、
条件に該当するかどうかでindexごとにbool型の値が設定されます。
例えば、「2より大きいかどうか」という論理演算の結果は以下のようになります。
"""

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s > 2)

"""
a    False
b    False
c     True
d     True
dtype: bool

また、indexに対して論理演算をすることも可能です。
indexが'c'かどうか、という論理演算の結果は以下のようになります。
"""

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s.index == 'c')

"""
[False False  True False]

ただし、この場合の戻り値の型はnumpy.ndarrayとなります。
"""
