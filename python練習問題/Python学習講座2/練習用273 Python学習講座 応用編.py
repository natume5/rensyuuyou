#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 欠損値（NaN） ---")


"""
実務上でデータを取り扱うと、たまたまデータの取得に失敗したり、
オペレーターの入力ミスなどで欠損値が発生することが多々あります。
pandasの欠損値はnumpyのnanが使用されます。
ここでは判定方法やクレンジングの方法について学習します。
"""


print("--- NaNの判定 ---")


"""
math.isnam

NaNかどうかの判定は組込みのmathモジュールを使用します。
例えばループ処理をしている際に欠損値があり演算で
エラーが起きるので演算前にチェックをしたい、といった場合が挙げられます。
"""

import pandas as pd
import math


s = pd.Series([2, 5, 8, None])
print(s)

for num in s:
	print(math.isnan(num))

"""
0    2.0
1    5.0
2    8.0
3    NaN
dtype: float64

False
False
False
True


pandas.isnull

pandasのisnull()メソッドを使用すると、SeriesやDataFrameに対し、
NaNかどうかを判定したbool型のSeries/DataFrameを取得することができます。
先ほどと同じSeriesでisnullを使用してみましょう。
"""

print(pd.isnull(s))

"""
0    False
1    False
2    False
3     True
dtype: bool
"""


print("--- dropna 欠損値NaNを除去する ---")


"""
次にデータクレンジングでよく使う欠損値の除去についてです。
Series、DataFrameともにdropnaメソッドを使用します。

Series 欠損値を除去する

dropna()メソッドを使用するとSeriesの欠損値を除去することができます。
先ほどのサンプルのSeriesで試してみましょう。
"""

s = pd.Series([2, 5, 8, None])

print(s.dropna())

"""
0    2.0
1    5.0
2    8.0
dtype: float64


DataFrame 欠損値がある行を除去する

DataFrameの場合は2次元ですので行、列を考慮する必要があります。
単純にdropnaメソッドを実行すると、1つでもNaNのある行が削除されます。
また、subsetを指定するとカラムを指定することができます。
"""

df = pd.DataFrame([[1, None], [None, 20], [None, None], [4, 40]],
	columns=['col1', 'col2'])

print(df)

print(df.dropna())    # どれか1つでもNaNがあれば除去される。

print(df.dropna(subset=['col1']))
# col1でNaNがあるものが除去される。

"""
   col1  col2
0   1.0   NaN
1   NaN  20.0
2   NaN   NaN
3   4.0  40.0

   col1  col2
3   4.0  40.0

   col1  col2
0   1.0   NaN
3   4.0  40.0


DataFrame 欠損値がある列を除去する

私は業務上で使用したことがないのですが、
欠損値がある列を除去することもできます。
引数にaxis=1を指定します。
"""

df = pd.DataFrame([[1, 10], [None, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'])

print(df)

print(df.dropna(axis=1))

"""
   col1  col2
0   1.0    10
1   NaN    20
2   3.0    30
3   4.0    40

   col2
0    10
1    20
2    30
3    40

欠損値を含むcol1が除去されます。
"""
