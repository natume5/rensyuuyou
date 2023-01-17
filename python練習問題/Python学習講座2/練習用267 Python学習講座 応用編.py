#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrameのデータ参照 ---")


"""
これまでDataFrameに関する説明と、
基本的な統計量の算出方法について説明しました。
このページではDataFrame内部のデータを参照する方法について学習します。
"""


print("--- 列を取得する ---")


"""
カラムを指定して列データをSeriesとして取得する方法は2つあります。
DataFrameオブジェクト['カラム名']もしくは、
DataFrameオブジェクト.カラム名と記述します。
DataFrameは以下の3行2列のDataFrameを使用するものとします。
"""

import pandas as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]],
    columns=['col1','col2'], index=['a', 'b', 'c'])

print(df)

# col1を取得する
print(df['col1'])

# col2を取得する
print(df.col2)

"""
   col1  col2
a     1    10
b     2    20
c     3    30

a    1
b    2
c    3
Name: col1, dtype: int64

a    10
b    20
c    30
Name: col2, dtype: int64

取得できるオブジェクトの型は前述の通り、Series型となります。
したがって、このあと行を指定する場合は以下のように[]か.で記述します。
"""

# col2のa行目を[]で取得
print(df.col2['a'])

# col2のa行目を.で取得
print(df.col2.a)

"""
10
10
"""


print("--- スライスする ---")


"""
またDataFrameはスライス構文を取得すると行を絞ったDataFrameが取得できます。
私はpandasのこの仕様で最初非常に混乱しました。
スライスで指定できるのは行で、
取得できるのがDataFrameである点に注意してください。
サンプルです。3行2列のDataFrameでindexはデフォルトが使用されています。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]],
	columns=['col1', 'col2'])

print(df)

# スライスしてみる
print(df[1:2])

"""
   col1  col2
0     1    10
1     2    20
2     3    30

   col1  col2
1     2    20

1行以降、2行目未満がDataFrameで取得されます。
"""


print("--- loc、ilocで行データをSeries形式で取得 ---")


"""
loc、ilocで行データをseries形式で取得することができます。
locはラベル名、つまりindexを指定し、ilocはinteger-location、
つまり位置を表す整数でアクセスします。
DataFrameは以下の3行2列のDataFrameを使用するものとします。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]],
   columns=['col1', 'col2'])
print(df)

"""
   col1  col2
0     1    10
1     2    20
2     3    30


loc

まずはlocです。たとえば、index=0を指定する場合以下のように記述します。
"""

print(df.loc[0])

"""
col1     1
col2    10
Name: 0, dtype: int64

また、スライスを使用することも可能です。
この場合取得できるのはDataFrameオブジェクトです。
"""

print(df.loc[1:2])

"""
   col1  col2
1     2    20
2     3    30

例えば、0行目のcol1のデータを取得する場合は以下のように記述します。
"""

print(df.loc[0]['col1'])

"""
1


iloc

locと使用方法はほとんど同じです。integer-location形式で指定します。
例えば、0から数えて1行目を取得する場合は以下のように記述します。
"""

print(df.iloc[1])

"""
col1     2
col2    20
Name: 1, dtype: int64
"""


print("--- at、iatで行、列を指定して値を取得する ---")


"""
at、iatで行、列を指定して値を取得することができます。
at

atはラベル名でアクセスします。行、列の順で添字に指定します。
例えば、indexがaの行でカラムがcol1のデータを取得する場合、
以下のように記述します。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]],
   columns=['col1', 'col2'], index=['a', 'b', 'c'])
print(df)

print(df.at['a', 'col1'])


"""
iat

atと使用方法はほとんど同じです。integer-location形式で指定します。
例えば0から数えて1行1列目の要素を取得する場合、以下のように記述します。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]],
   columns=['col1', 'col2'])
print(df)

print(df.iat[1, 1])

"""
   col1  col2
0     1    10
1     2    20
2     3    30

20
"""


print("--- 補足 ---")


"""
loc、iloc、at、iatに加え、axというメソッドがありますが、
最新バージョンではなくなっているため説明は割愛します。
"""
