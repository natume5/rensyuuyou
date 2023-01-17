#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 whereによるフィルタリング ---")


"""
ここでDataFrameのデータ選択方法について学習しましたが、
元のDataFrameと同じサイズのDataFrameが必要になる場合がでてきます。
そんな時はwhereを使うことで解決することができます。
"""


print("--- DataFrameのwhere ---")


"""
同じサイズで抽出

使い方はwhere句の中にフィルタ対象となるbool型シーケンスを指定するだけです。
以前学習したフィルタと比較してみてみましょう。
"""

import pandas as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'])

# 添え字でフィルタ条件指定
print(df[df['col1'] > 2])

"""
   col1  col2
2     3    30
3     4    40
"""

# whereを使用
print(df['col1'] > 2)

"""
0    False
1    False
2     True
3     True
Name: col1, dtype: bool


NaN以外で値を埋める

もとのDataFrameと同じサイズで該当するもの以外は
NaNが設定されていることが確認できます。
また、NaN以外にも第2引数を指定すると0埋めなどすることができます。
先ほどのサンプルで0埋めする場合は以下のように記述します。
"""

print(df.where(df['col1'] > 2, 0))

"""
   col1  col2
0     0     0
1     0     0
2     3    30
3     4    40


セル毎にNaN以外で値を埋める

また、第2引数に埋める値のDataFrameを指定すると、
セル毎に埋める値を分けることも可能です。
例えばcol1は0で、col2はハイフンで埋めたい場合は以下のように記述します。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'])

# col1は0、col2はハイフンのdataframeを定義
pad = pd.DataFrame([[0, '-']] * len(df),
	columns=df.columns, index=df.index)

print(pad)

print(df.where(df['col1'] > 2, pad))

"""
   col1 col2
0     0    -
1     0    -
2     0    -
3     0    -

   col1 col2
0     0    -
1     0    -
2     3   30
3     4   40
"""


print("--- Seriesのwhere ---")


"""
説明の順序が少し前後しますが、Seriesでも同様のことが可能です。
サンプルのみ掲載します。
"""

s = pd.Series([1, 2, 3])

print(s[s > 1])

print(s.where(s > 1))

"""
1    2
2    3
dtype: int64

0    NaN
1    2.0
2    3.0
dtype: float64
"""
