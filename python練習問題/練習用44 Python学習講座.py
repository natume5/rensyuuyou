#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- pandas入門  column(列名) index(行名)の変更---")


"""
pandasで集計関数を使用すると同じ名前の列のDataFrameができますが、
それらを統合する際列名をわかりやすくリネームする必要がでてきます。
ここではcolumnやindexをリネームする方法について学習します。


DataFrame.rename column、indexをリネームする

columns引数かindex引数に辞書形式でキーに変更前、値に変更後の文字列を設定します。
また、inplace引数でTrueを指定すると破壊的に変更し、Falseを指定すると変更したコピーが返されます。
inplace引数のデフォルトはFalseです。
"""

import pandas as pd

# DataFrameを生成する
df = pd.DataFrame([[1, 10], [2, 20]], columns=['col1', 'col2'], 
index=['a', 'b']) 

print(df)

#    col1  col2
# a     1    10
# b     2    20

# 列名を変更する
new_df = df.rename(columns={'col1': 'new1', 'col2': 'new2'})

print(new_df)

#    new1  new2
# a     1    10
# b     2    20

# 行名を変更する
new_df = df.rename(index={'a': 'new1', 'b': 'new2'})

print(new_df)

#       col1  col2
# new1     1    10
# new2     2    20

# 破壊的に変更する
df.rename(columns={'col1': 'new1', 'col2': 'new2'}, inplace=True)

print(df)

#    new1  new2
# a     1    10
# b     2    20


print("--- pandas入門  DataFrameをgroupbyで集計する---")


"""
私が実務でよく使うものの1つがgroupbyで、
例えば商品カテゴリー毎に合計やばらつきを確認したい場合などが挙げられます。
無論、SQLでも同様のことは大抵できてしまいますが、
例えば形態素解析した結果の単語ごとの集計を書けたい場合など
Pythonで一気通貫でやる場合にはpandasを使うのが便利ですね。


groupby

その名の通りDataFrameをgroupbyで集計します。
groupbyの戻り値で得られるGroupByオブジェクトに対し
mean(), min(), max(), sum()などのメソッドを適用すると、
グループごとの平均、最小値、最大値、合計などの統計量を算出することが可能です。
使い方は簡単ですので、サンプルを見てみましょう。
カテゴリーとタグ毎になんらかの量が設定されているDataFrameに対し、
集計をかけてみます。引数に集計対象の列名を設定します。
複数でgroupbyを書けたい場合はリストで設定します。
"""

df = pd.DataFrame([['cate1', 'tag1', 150], ['cate1', 'tag2', 210], 
['cate2', 'tag2', 80], ['cate2', 'tag1', 310], ], 
columns=['category', 'tag', 'value'])

print(df)

#  category   tag  value
# 0    cate1  tag1    150
# 1    cate1  tag2    210
# 2    cate2  tag2     80
# 3    cate2  tag1    310

# category毎の合計を算出する
print(df.groupby('category').sum())

# category
# cate1       360
# cate2       390

# category,tag毎の件数を算出する

print(df.groupby(['category', 'tag']).count())

#                value
# category tag
# cate1    tag1      1
#          tag2      1
# cate2    tag1      1
#          tag2      1

# tag毎のばらつきを算出する

print(df.groupby(['tag']).std())

#            value
# tag
# tag1  113.137085
# tag2   91.923882

"""
いかがでしょうか。集計が簡単に使用できますので便利ですね。
"""


print("--- pandas入門  DataFrameの値を置換する---")


"""
業務データはものによっては誤記や入力時のエラーなどで
何度か置換をしてクレンジングする場合がありますが、
pandasのDataFrameにはreplaceというメソッドを使用すると置換処理を行うことができます。


replace 値を置換する

基本的な置換

replaceメソッドで置換することができます。
例えば、orangeがorangggとなっているデータがあった場合、
以下のように置換して修正することができます。
"""

df = pd.DataFrame([['apple', 10], ['oranggg', 20], 
['banana',30]],columns=['name', 'price'])

print(df.replace('oranggg', 'orange'))

#      name  price
# 0   apple     10
# 1  orange     20
# 2  banana     30


"""
正規表現による置換

また、引数にregex=Trueを指定することで正規表現を使用することもできます。
先ほどの置換を以下のように書くこともできます。
"""

print(df.replace('.*ggg.*', 'orange', regex=True))

#      name  price
# 0   apple     10
# 1  orange     20
# 2  banana     30


"""
欠損値の0埋め

よく使うのが欠損値の置換です。NaNを0で埋めたい場合は以下のようにnp.NaNで置換します。
"""

# import pandas as pd
import numpy as np


df = pd.DataFrame([[1, 10], [None, 20], [3, None]], 
columns=['col1', 'col2'])

print(df.replace(np.NaN, 0))

#    col1  col2
# 0   1.0  10.0
# 1   0.0  20.0
# 2   3.0   0.0


print("--- pandas入門  ピボットテーブル---")


"""
クロス集計に欠かせないのがピボットテーブルですが、pandasのピボットテーブルは合計、
平均以外にも複雑な計算ができます。
ですが、集計方法を指定する際にラムダ式もしくは関数オブジェクトを使うため、
初見だと少し戸惑うかもしれません。


pivot_tableメソッド

DataFrameのpivot_tableメソッドでピボットテーブルを生成することができます。
まずはサンプルから見てください。
カテゴリーとタグがつけられたデータに何らかの値が付与されているデータの合計を集計してみます。
"""

# import pandas as pd

df = pd.DataFrame([['cate1', 'tag1', 4], ['cate2', 'tag1', 10], 
['cate1', 'tag2', 5], ['cate3', 'tag3', 5], ['cate2', 'tag3', 5]], 
columns=['category', 'tag', 'value'])

print(df)

#   category   tag  value
# 0    cate1  tag1      4
# 1    cate2  tag1     10
# 2    cate1  tag2      5
# 3    cate3  tag3      5
# 4    cate2  tag3      5

# 合計をクロス集計する
print(df.pivot_table(index=['category'], columns=['tag'], 
values='value', fill_value=0, aggfunc=lambda x: sum(x)))

# tag       tag1  tag2  tag3
# category
# cate1        4     5     0
# cate2       10     0     5
# cate3        0     0     5

"""
何をしているのかはなんとなく解ると思います。pivot_tableで指定する引数は以下の通りです。

    index：縦の集計項目を指定します。複数指定することができます。
    columns：縦の集計項目を指定します。複数指定することができます。
    values：集計対象の値の項目を指定します。
    fill_value：NaNを何で埋めるかです。サンプルでは0埋めしています。
    aggfunc：集計関数を指定します。

さて、最後のaggfuncが少しわかりづらいですね。
ここにシーケンスに対して処理を行うラムダ式か関数オブジェクトを指定します。

例えば、個数、平均、標準偏差を集計する場合、以下のように記述します。
（データが少し適当すぎましたね（汗）適宜数字をいじって試してみてください。）
"""

# 個数
print(df.pivot_table(index=['category'], columns=['tag'], 
values='value', fill_value=0, aggfunc=lambda x: len(x)))

# tag       tag1  tag2  tag3
# category
# cate1        1     1     0
# cate2        1     0     1
# cate3        0     0     1

# 平均
print(df.pivot_table(index=['category'], columns=['tag'], 
values='value', fill_value=0, aggfunc=lambda x: np.average(x)))

# tag       tag1  tag2  tag3
# category
# cate1        4     5     0
# cate2       10     0     5
# cate3        0     0     5

# 標準偏差
print(df.pivot_table(index=['category'], columns=['tag'], 
values='value', fill_value=0, aggfunc=lambda x: np.std(x)))

# tag       tag1  tag2  tag3
# category
# cate1        0     0     0
# cate2        0     0     0
# cate3        0     0     0

"""
このaggfuncをカスタマイズすると、複雑な集計が可能となりますが、最初は難しく感じますね。
"""


print("--- pandas入門  DataFrameの行列を入れ替える---")


"""
今回は短いトピックですが、DataFrameno行列を入れ替える方法です。
DataFrame.Tを使用すると転置したDataFrameを取得することができます。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], 
columns=['col1', 'col2'], index=['a', 'b', 'c', 'd'])

print(df.T)

#        a   b   c   d
# col1   1   2   3   4
# col2  10  20  30  40

