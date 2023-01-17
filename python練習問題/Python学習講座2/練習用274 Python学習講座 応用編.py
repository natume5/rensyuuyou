#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 column(列名) index(行名)の変更 ---")


"""
pandasで集計関数を使用すると同じ名前の列のDataFrameができますが、
それらを統合する際列名をわかりやすくリネームする必要がでてきます。
ここではcolumnやindexをリネームする方法について学習します。
"""


print("--- DataFrame.rename column、indexをリネームする ---")


"""
columns引数かindex引数に辞書形式でキーに変更前、
値に変更後の文字列を設定します。
また、inplace引数でTrueを指定すると破壊的に変更し、
Falseを指定すると変更したコピーが返されます。
inplace引数のデフォルトはFalseです。
"""

import pandas as pd


# DataFrameを生成する
df = pd.DataFrame([[1, 10], [2, 20]], columns=['col1', 'col2'],
	index=['a', 'b'])

print(df)

# 列名を変更する
new_df = df.rename(columns={'col1': 'new1', 'col2': 'new2'})
print(new_df)

# 行名を変更する
new_df2 = df.rename(index={'a': 'new1', 'b': 'new2'})
print(new_df2)

# 破壊的に変更する
df.rename(columns={'col1': 'new1', 'col2': 'new2'}, inplace=True)
print(df)

"""
   col1  col2
a     1    10
b     2    20

   new1  new2
a     1    10
b     2    20

      col1  col2
new1     1    10
new2     2    20

   new1  new2
a     1    10
b     2    20
"""
