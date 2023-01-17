#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrameの行列を入れ替える ---")


"""
今回は短いトピックですが、DataFrameno行列を入れ替える方法です。
DataFrame.Tを使用すると転置したDataFrameを取得することができます。
"""

import pandas as pd


df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])

print(df)

print(df.T)

"""
   col1  col2
a     1    10
b     2    20
c     3    30
d     4    40

       a   b   c   d
col1   1   2   3   4
col2  10  20  30  40
"""
