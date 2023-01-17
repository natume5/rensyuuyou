#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrame 基本統計量の算出 ---")


"""
DataFrameに格納されたデータは簡単に基本的な統計量を計算することができます
"""


print("--- 行数、要素数 ---")


"""
行数（レコード数）

行数を出力する場合はlen関数を使用します。
また、sizeメソッドを使用すると要素数を取得することができます。
"""

import pandas as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]],
    columns=['col1','col2'])

print(df)

print(len(df))

"""
   col1  col2
0     1    10
1     2    20
2     3    30

3

上のサンプルでは2列3行のDataFrameの行の長さをlenで取得しています。


要素数

sizeプロパティで要素数を取得することができます。
"""

# 上のサンプルの続き
print(df.size)

"""
6
"""


print("--- 基本統計量 ---")


"""
DataFrameのメソッドを使用して、列ごとの基本統計量を取得することができます。

平均、最大最小、標準偏差、分散など
"""

print(df.count())    # 要素数

print(df.mean())    # 平均

"""
col1    3
col2    3
dtype: int64

col1     2.0
col2    20.0
dtype: float64

なお、戻り値は全てDataFrame型オブジェクトとなります。
別項にて説明しますが、各列の統計量を取得する場合はインデックスを指定します。
例えば、列「col1」の平均値を取得する場合、df.mean()['col1'] と記述します。
その他、よく使うメソッドを以下にまとめます。

df.count()          要素数
df.mean()            平均
df.std()           標準偏差
df.max()            最大値
df.min()            最小値
df.var()             分散
df.sample()     ランダムサンプリング


まとめて取得

また、全体的にデータを俯瞰したい場合、
describeを使用することで基本的な統計量が一括で取得することができます。
"""

print(df.describe())

"""
       col1  col2
count   3.0   3.0
mean    2.0  20.0
std     1.0  10.0
min     1.0  10.0
25%     1.5  15.0
50%     2.0  20.0
75%     2.5  25.0
max     3.0  30.0

こちらも戻り値はDataFrameなので、
個別の値を取得したい場合ば列、行をインデックスで順に指定します。
例えば、col2の平均を取得したい場合、
df.describe()['col2']['mean'] と記述します。
"""

print(df.describe()['col2']['mean'])

"""
20.0
"""
