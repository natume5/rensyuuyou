#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrameのループ処理 ---")


print("--- iterrows 1行ずつ処理する ---")


"""
時系列データなどを扱う際、1行ずつ
なんらかの指標を計算することがよくあると思います。
DataFrameを1行ずつ処理する場合は
DataFrameのiterrows()メソッドを使用します。
このメソッドでループする場合、indexと行が同時に取得できる点が特徴的です。
以下、サンプルです。
"""

import pandas as pd

# DataFrameとSeriesを生成
df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'])

for index, row in df.iterrows():
	print(row['col1'], row['col2'])

"""
1 10
2 20
3 30
4 40

上のコードのrowはSeries型のオブジェクトである点に注意してください。
"""


print("--- iteritems 一列ずつ処理する ---")


"""
iteritems()メソッドを使用すると一列ずつ処理を行うことができます。
例えば、列ごとに合計を計算する場合は以下のようにします。
（もっともこの程度だとdf.sum()で算出可能ですが。）
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'])

for index, col in df.iteritems():
	print(sum(col))

"""
10
100
"""
