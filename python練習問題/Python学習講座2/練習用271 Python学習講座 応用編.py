#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrameの更新系処理 ---")


"""
DataFrameに列や行を追加、更新、削除する方法についてです。
"""


print("--- Seriesを列として追加 ---")


"""
DataFrameに新たな列としてSeriesを追加する場合、
添字に新しいカラム名を指定して代入します。
また、既存のカラム名を指定した場合、そのカラムが更新されます
"""

import pandas as pd

# DataFrameとSeriesを生成
df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])

s = pd.Series([1, 1, 1, 1], index=['a', 'b', 'c', 'd'])

# DataFrameにSeriesを新たな列として追加
df['new_col'] = s

print(df)

# DataFrameの既存列を更新する
df['col1'] = s
print(df)

"""
   col1  col2  new_col
a     1    10        1
b     2    20        1
c     3    30        1
d     4    40        1

   col1  col2  new_col
a     1    10        1
b     1    20        1
c     1    30        1
d     1    40        1

元のDataFrameになくても
添字で定義して代入できてしまう点が少し違和感がありますが、
簡単に追加、更新することができますね。
"""


print("--- 行を追加 ---")


"""
appendメソッドを使用します。
戻り値に新たなオブジェクトが返され、
元のオブジェクトは更新されません。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])

print(df)

df2 = pd.DataFrame([[9, 99]], columns=['col1', 'col2'],
	index=['x'])

df.append(df2)

print(df)

"""
FutureWarning: The frame.append method is deprecated and 
will be removed from pandas in a future version. 
Use pandas.concat instead.

今後の警告: frame.append メソッドは非推奨であり、
将来のバージョンで pandas から削除される予定です。 
代わりに pandas.concat を使用してください。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])

print(df)

df2 = pd.DataFrame([[9, 99]], columns=['col1', 'col2'],
	index=['x'])

print(pd.concat([df, df2]))

"""
   col1  col2
a     1    10
b     2    20
c     3    30
d     4    40

   col1  col2
a     1    10
b     2    20
c     3    30
d     4    40
x     9    99
"""


print("--- 行の削除 ---")


"""
dropメソッドで指定したindexの行を削除することができます。
また、indexはリストなどで複数指定することも可能です。
戻り値に新たなオブジェクトが返され、元のオブジェクトは更新されません。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])

print(df)

# 単一行を削除
print(df.drop('a'))

# 複数行を削除
print(df.drop(['a', 'b']))

"""
   col1  col2
a     1    10
b     2    20
c     3    30
d     4    40

   col1  col2
b     2    20
c     3    30
d     4    40

   col1  col2
c     3    30
d     4    40
"""


print("--- 列の削除 ---")


"""
行の削除の時と同様dropメソッドを使用するのですが、
axis引数に1もしくは'columns'を設定します。
（指定しない場合はデフォルトで0が設定されています。）
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])

print(df)

print(df.drop('col1', axis=1))

"""
   col1  col2
a     1    10
b     2    20
c     3    30
d     4    40

   col2
a    10
b    20
c    30
d    40
"""


print("--- 要素の更新 ---")


"""
私はめったに使わないのですが、要素を更新する方法です。
とはいえ、atかiatで要素を取得して代入するだけです。
at、iatの使用方法はこちらをご参照ください。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])

print(df)

df.at['a', 'col1'] = 999

print(df)

"""
   col1  col2
a     1    10
b     2    20
c     3    30
d     4    40

   col1  col2
a   999    10
b     2    20
c     3    30
d     4    40
"""
