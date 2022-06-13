#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- pandas入門 whereによるフィルタリング---")


"""
ここでDataFrameのデータ選択方法について学習しましたが、
元のDataFrameと同じサイズのDataFrameが必要になる場合がでてきます。
そんな時はwhereを使うことで解決することができます。


DataFrameのwhere

同じサイズで抽出

使い方はwhere句の中にフィルタ対象となるbool型シーケンスを指定するだけです。
以前学習したフィルタと比較してみてみましょう。
"""

import pandas  as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'])

# 添え字でフィルタ条件指定
print(df[df['col1'] > 2])

#     col1  col2
# 2     3    30
# 3     4    40

# whereを使用

print(df.where(df['col1'] > 2))

#    col1  col2
# 0   NaN   NaN
# 1   NaN   NaN
# 2   3.0  30.0
# 3   4.0  40.0


"""
NaN以外で値を埋める

もとのDataFrameと同じサイズで該当するもの以外はNaNが設定されていることが確認できます。
また、NaN以外にも第2引数を指定すると0埋めなどすることができます。
先ほどのサンプルで0埋めする場合は以下のように記述します。
"""

print(df.where(df['col1'] > 2, 0))

#    col1  col2
# 0     0     0
# 1     0     0
# 2     3    30
# 3     4    40


"""
セル毎にNaN以外で値を埋める

また、第2引数に埋める値のDataFrameを指定すると、セル毎に埋める値を分けることも可能です。
例えばcol1は0で、col2はハイフンで埋めたい場合は以下のように記述します。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'])

# col1は0、col2はハイフンのdataframeを定義
pad = pd.DataFrame([[0, '-']] * len(df), columns=df.columns, index=df.index)
print(pad)

#    col1 col2
# 0     0    -
# 1     0    -
# 2     0    -
# 3     0    -

print(df.where(df['col1'] > 2, pad))

#    col1 col2
# 0     0    -
# 1     0    -
# 2     3   30
# 3     4   40


"""
Seriesのwhere

説明の順序が少し前後しますが、Seriesでも同様のことが可能です。サンプルのみ掲載します。
"""

s = pd.Series([1, 2, 3])

print(s[s > 1])

# 1    2
# 2    3
# dtype: int64


print(s.where(s > 1))

# 0    NaN
# 1    2.0
# 2    3.0
# dtype: float64


print("--- pandas入門  DataFrameのソート---")


"""
pandasのメリットの1つとして多次元のリストを簡単にソートすることができる点が挙げられると思います。

データ分析以外にもETL等でソートが必要な場合はpandasの使用を検討してみてください。


DataFrameのソート

DataFramオブジェクトのsort_valuesメソッドを使用すると簡単にソートすることができます。
第1引数にソート対象のカラムリスト、ascendingで昇順/降順を指定します。

サンプルです。3列のDataFrameをソートしてみましょう。
"""

df = pd.DataFrame([[3, 10, 200], [2, 30, 100], [4, 40, 300], [1, 20, 200]], 
columns=['col1', 'col2', 'col3'])

print(df)

#    col1  col2  col3
# 0     3    10   200
# 1     2    30   100
# 2     4    40   300
# 3     1    20   200


# col1で昇順、col2で降順にソートしてみる。

print(df.sort_values(['col1', 'col2'], ascending=[True, False]))

#    col1  col2  col3
# 3     1    20   200
# 1     2    30   100
# 0     3    10   200
# 2     4    40   300


print("--- pandas入門  DataFrameの更新系処理---")


"""
DataFrameに列や行を追加、更新、削除する方法についてです。


Seriesを列として追加

DataFrameに新たな列としてSeriesを追加する場合、添字に新しいカラム名を指定して代入します。
また、既存のカラム名を指定した場合、そのカラムが更新されます。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], 
index=['a', 'b', 'c', 'd'])

s = pd.Series([1, 1, 1, 1], index=['a', 'b', 'c', 'd'])

# DataFrameにSeriesを新たな列として追加
df['new_col'] = s

print(df)

#    col1  col2  new_col
# a     1    10        1
# b     2    20        1
# c     3    30        1
# d     4    40        1


# DataFrameの既存列を更新する
df['col1'] = s

print(df)

#    col1  col2  new_col
# a     1    10        1
# b     1    20        1
# c     1    30        1
# d     1    40        1

"""
元のDataFrameになくても添字で定義して代入できてしまう点が少し違和感がありますが、
簡単に追加、更新することができますね。


行を追加

appendメソッドを使用します。戻り値に新たなオブジェクトが返され、元のオブジェクトは更新されません。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], 
index=['a', 'b', 'c', 'd'])

df2 = pd.DataFrame([[9, 99]], columns=['col1', 'col2'], index=['x'])

print(df.append(df2))

#    col1  col2
# a     1    10
# b     2    20
# c     3    30
# d     4    40
# x     9    99


"""
行の削除

dropメソッドで指定したindexの行を削除することができます。
また、indexはリストなどで複数指定することも可能です。
戻り値に新たなオブジェクトが返され、元のオブジェクトは更新されません。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], 
index=['a', 'b', 'c', 'd'])

# 単一行を削除
print(df.drop('a'))

#    col1  col2
# b     2    20
# c     3    30
# d     4    40


# 複数行を削除
print(df.drop(['a', 'b']))

#    col1  col2
# c     3    30
# d     4    40


"""
列の削除

行の削除の時と同様dropメソッドを使用するのですが、axis引数に1もしくは'columns'を設定します。
（指定しない場合はデフォルトで0が設定されています。）
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], 
index=['a', 'b', 'c', 'd'])

print(df.drop('col1', axis=1))

#    col2
# a    10
# b    20
# c    30
# d    40


"""
要素の更新

私はめったに使わないのですが、要素を更新する方法です。
とはいえ、atかiatで要素を取得して代入するだけです。
at、iatの使用方法はこちらをご参照ください。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], 
index=['a', 'b', 'c', 'd'])

df.at['a', 'col1'] = 999
print(df)

#    col1  col2
# a   999    10
# b     2    20
# c     3    30
# d     4    40


print("--- pandas入門  DataFrameのループ処理---")


"""
iterrows 1行ずつ処理する

時系列データなどを扱う際、1行ずつなんらかの指標を計算することがよくあると思います。
DataFrameを1行ずつ処理する場合はDataFrameのiterrows()メソッドを使用します。
このメソッドでループする場合、indexと行が同時に取得できる点が特徴的です。
以下、サンプルです。
"""

# import pandas as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], 
index=['a', 'b', 'c', 'd'])

for index, row in df.iterrows():
	print(row['col1'], row['col2'])

# 1 10
# 2 20
# 3 30
# 4 40

"""
上のコードのrowはSeries型のオブジェクトである点に注意してください。


iteritems 一列ずつ処理する

iteritems()メソッドを使用すると一列ずつ処理を行うことができます。
例えば、列ごとに合計を計算する場合は以下のようにします。
（もっともこの程度だとdf.sum()で算出可能ですが。）
"""

# import pandas as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]], columns=['col1', 'col2'], 
index=['a', 'b', 'c', 'd'])

for index, col in df.iteritems():
	print(sum(col))

# 10
# 100


print("--- pandas入門  欠損値（NaN）---")


"""
実務上でデータを取り扱うと、たまたまデータの取得に失敗したり、
オペレーターの入力ミスなどで欠損値が発生することが多々あります。
pandasの欠損値はnumpyのnanが使用されます。
ここでは判定方法やクレンジングの方法について学習します。


NaNの判定
math.isnam

NaNかどうかの判定は組込みのmathモジュールを使用します。
例えばループ処理をしている際に欠損値があり演算でエラーが起きるので演算前にチェックをしたい、
といった場合が挙げられます。
"""

# import pandas as pd
import math


s = pd.Series([2, 5, 8, None])
print(s)

# 0    2.0
# 1    5.0
# 2    8.0
# 3    NaN
# dtype: float64

for num in s:
	print(math.isnan(num))

# False
# False
# False
# True

"""
pandas.isnull

pandasのisnull()メソッドを使用すると、SeriesやDataFrameに対し、
NaNかどうかを判定したbool型のSeries/DataFrameを取得することができます。
先ほどと同じSeriesでisnullを使用してみましょう。
"""

# import pandas as pd
# import math

s = pd.Series([2, 5, 8, None])

print(pd.isnull(s))

# 0    False
# 1    False
# 2    False
# 3     True
# dtype: bool


"""
dropna 欠損値NaNを除去する

次にデータクレンジングでよく使う欠損値の除去についてです。
Series、DataFrameともにdropnaメソッドを使用します。


Series 欠損値を除去する

dropna()メソッドを使用するとSeriesの欠損値を除去することができます。
先ほどのサンプルのSeriesで試してみましょう。
"""

s = pd.Series([2, 5, 8, None])

print(s.dropna())

# 0    2.0
# 1    5.0
# 2    8.0
# dtype: float64


"""
DataFrame 欠損値がある行を除去する

DataFrameの場合は2次元ですので行、列を考慮する必要があります。
単純にdropnaメソッドを実行すると、1つでもNaNのある行が削除されます。
また、subsetを指定するとカラムを指定することができます。
"""

df = pd.DataFrame([[1, None], [None, 20], [None, None], [4, 40]], 
columns=['col1', 'col2'])

print(df)

#    col1  col2
# 0   1.0   NaN
# 1   NaN  20.0
# 2   NaN   NaN
# 3   4.0  40.0

# どれか一つでもNaNがあれば除去される
print(df.dropna())

#    col1  col2
# 3   4.0  40.0

# col1でNaNがあるものが除去される
print(df.dropna(subset=['col1']))

#    col1  col2
# 0   1.0   NaN
# 3   4.0  40.0


"""
DataFrame 欠損値がある列を除去する

私は業務上で使用したことがないのですが、欠損値がある列を除去することもできます。
引数にaxis=1を指定します。
"""

df = pd.DataFrame([[1, 10], [None, 20], [3, 30], [4, 40]], 
columns=['col1', 'col2'])

print(df.dropna(axis=1))

#    col2
# 0    10
# 1    20
# 2    30
# 3    40

"""
欠損値を含むcol1が除去されます。
"""
