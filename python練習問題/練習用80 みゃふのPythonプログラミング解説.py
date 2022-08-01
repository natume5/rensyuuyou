#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- pandasの基本① ---")


"""
pandasは「簡潔にデータを扱うために開発されたPythonのライブラリ」です。
CSVなどからデータを読み取り、追加、修正、削除などの処理をすることができます。
ここでは「pandasって何？」「pandasってどう使うの？」といった方へ、pandasの使い方を解説します。
また、「pandasで使える高機能な1次元配列と2次元配列」のようなものとしてよく使われる、
SeriesとDataFrameの基本的な使い方も解説します。
SeriesやDataFrameは標準で使える配列よりも、より多くの操作が可能な、
Pythonでデータを扱う際には必須になりますので、ぜひ使えるようになりましょう。
なお、pandasをインストールしていない場合、まずはpip等でpandasをインストールしてください。
"""


print("--- CSVファイルを読み込む ---")


"""
ではpandasを使っていきましょう。
まずはcsvファイルを読み込み、変数に入れてみましょう。
今回は以下ようなデータが入っているCSVファイルを読み込みます。

index,name,age
0,塚田 栄一,45
1,岩村 真尋,21
2,中園 美希,41
3,猪股 幸平,34
4,及川 大介,34
"""

import pandas as pd

data = pd.read_csv("sample csvファイル.csv", index_col=0)
print(data)

"""
csvファイルのデータが変数dataに入っているのが分かります。
まずpandasをインポートしましょう。次にread_csv()でcsvファイルを読み込みます。
第一引数はcsvファイルのパスです。ここはお使いの環境によって異なる部分です。
第二引数はどの列をインデックスとするかを指定しています。今回はindex列を指定しています。
"""


print("--- 読み込んだデータの情報を取得する ---")


"""
ここでは先ほど読み込んだcsvデータの情報を取得する方法をご紹介します。


データの行数と列数を取得する-shape-

データの行数、列数が知りたい場合はshapeを使います。
"""

# import pandas as pd

data = pd.read_csv("sample csvファイル.csv", index_col=0)
print(data.shape)    # (5, 2)


"""
カラムの情報を取得する-columns-

読み込んだデータのカラムの情報が知りたい場合はcolumnsを使います。
"""

# import pandas as pd

data = pd.read_csv("sample csvファイル.csv", index_col=0)
print(data.columns)    # Index(['name', 'age'], dtype='object')


"""
データを先頭から指定した行数取得する-head()-

先頭から指定した行数分データを取得したい場合はhead()を使います。
"""

# import pandas as pd

data = pd.read_csv("sample csvファイル.csv", index_col=0)
print(data.head(3))
#         name  age
# index
# 0      塚田 栄一   45
# 1      岩村 真尋   21
# 2      中園 美希   41

"""
データを末尾から指定した行数取得する-tail()-

末尾から指定した行数分データを取得したい場合はtail()を使います。
"""

# import pandas as pd

data = pd.read_csv("sample csvファイル.csv", index_col=0)
print(data.tail(3))
#         name  age
# index
# 2      中園 美希   41
# 3      猪股 幸平   34
# 4      及川 大介   34


"""
読み込んだデータに列を追加する

次に、読み込んだcsvデータに、新しい列を追加しましょう。
次の例では、リストの情報を追加しています。
"""

# import pandas as pd

data = pd.read_csv("sample csvファイル.csv", index_col=0)

list = [165, 170, 175, 180, 182]
series = pd.Series(list)
data['height'] = series.values

print(data)
#         name  age  height
# index
# 0      塚田 栄一   45     165
# 1      岩村 真尋   21     170
# 2      中園 美希   41     175
# 3      猪股 幸平   34     180
# 4      及川 大介   34     182

"""
最初に読み込んだcsvデータに「height」という列を追加しました。

リストを列に追加するには、pandasのSeries()を使います。
引数にリストを渡すと、Seriesというデータ型に変換してくれます。
最後にdataに新しく登録する列名をキーとして指定し、Seriesのvaluesでデータを入れています。


csvに出力する

最後に、列を追加したデータをcsvに出力してみましょう。
pandasではcsvやExcelファイル等への出力が簡単に行えます。
"""

# import pandas as pd

data = pd.read_csv("sample csvファイル.csv", index_col=0)

list = [165, 170, 175, 180, 182]
series = pd.Series(list)
data['height'] = series.values

data.to_csv("output.csv")

"""
先ほどのプログラムのprint()の箇所を、to_csv()というメソッドに置き換えています。
第一引数にcsvファイル名を指定することで使用できます。
また、to_excel()を使うとExcelファイルの出力も容易に行えます。
"""


print("--- Seriesの基本操作 ---")


"""
上記で少しふれたSeriesの基本操作です。
Seriesはpandasで使える1次元配列になります。

Seriesの作成

Seriesを初期化するにはpandasのSeries()を使います。
"""

# import pandas as pd
s = pd.Series([76, 54, 92])
print(s)
# 0    76
# 1    54
# 2    92
# dtype: int64

"""
また、データに名前をつけたい場合は、第二引数を次のようにします。
"""

# import pandas as pd
s = pd.Series([76, 54, 92], index=['国語', '英語', '数学'])
print(s)
# 国語    76
# 英語    54
# 数学    92
# dtype: int64


"""
値を追加・変更・削除する

次に初期化済みのSeriesに対して、値の追加・変更・削除を行ってみましょう。
"""

# import pandas as pd
s = pd.Series([76, 54, 92], index=['国語', '英語', '数学'])
s['日本史'] = 99    # 追加
s['英語'] = 62    # 変更
s = s.drop('国語')    # 削除
print(s)
# 英語     62
# 数学     92
# 日本史    99
# dtype: int64

"""
追加と変更はインデックスを使って参照します。

削除はdrop()を使います。drop()の第一引数にインデックスを指定してデータを削除します。


Series同士で足し算する

次に2つのSeriesのデータを足し算してみましょう。
"""

# import pandas as pd

s = pd.Series([76, 54, 92], index=['国語', '英語', '数学'])
s2 = pd.Series([34, 61, 22], index=['国語', '英語', '数学'])
print(s + s2)
# 国語    110
# 英語    115
# 数学    114
# dtype: int64

"""
2つのSeriesを+演算子で繋げるだけで、全てのデータを足し算できます。
ちなみに片方にしか存在しないインデックスがある場合は「NaN（非数）」になるので注意しましょう。
"""


print("--- DataFrameの基本操作 ---")


"""
次にDataFrameについて見ていきましょう。
pandasではDataFrameがデータ型の基本で、Seriesの集まりがDataFrameです。


DataFrameの作成

まずはDataFrameの初期化方法です。
csvやexcelを読み込む方法もありますが、今回はリストから作成してみましょう。
"""

# import pandas as pd

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
d = pd.DataFrame(lists)
d.index = ["1", "2", "3"]
d.columns = ["A", "B", "C"]
print(d)
#    A  B  C
# 1  1  2  3
# 2  4  5  6
# 3  7  8  9

"""
DataFrameはDataFrame()に二次元配列を渡すことで作成できます。
また、index()は行の名前、columns()は列の名前を付けることができます。


列・行を追加する

次にDataFrameに列や行を追加する方法を見ていきましょう。
まずは列の追加方法からご紹介します。
"""

# import pandas as pd

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
d = pd.DataFrame(lists)
lists2 = [10, 11, 12]
d[3] = lists2
print(d)

"""
四列目が追加されました。インデックス番号が3の列にリストを渡すことで列を追加しています。
では次に行の追加方法です。列の追加とほとんど変わりません。
"""

# import pandas as pd

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
d = pd.DataFrame(lists)
lists2 = [10, 11, 12]
d.loc[3] = lists2    # 変更
print(d)
#     0   1   2
# 0   1   2   3
# 1   4   5   6
# 2   7   8   9
# 3  10  11  12

"""
d.loc[3]の箇所を変えています。
行を追加する場合はlocというインスタンス変数を使います。


必要な値を取り出す

最後にDataFrame内の必要な値を取り出す処理を見てみましょう。
値にアクセスするには先ほども使ったlocを使います。
"""

# import pandas as pd

lists = [[1, 2, 3], [4, 5, 6]]
d = pd.DataFrame(lists)
d.index = ['1r', '2r']
d.columns = ['A', 'B', 'C']

print(d.loc['2r', 'B'])    # 5

"""
このdataFrameは次のようになっています。

    A  B  C
1r  1  2  3
2r  4  5  6

今回はこの中から「2r行」の「B列」の値を取得しています。
locは次のように使います。

[構文]

loc[行のインデックス, 列のインデックス]

また、locはスライスに対応しているので、次のように一部を切り取ったデータを取得することも可能です。
"""

# import pandas as pd

lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
d = pd.DataFrame(lists)
d.index = ['1r', '2r', '3r']
d.columns = ["A", "B", "C"]

print(d.loc['2r': '3r', 'B': 'C'])
#     B  C
# 2r  5  6
# 3r  8  9

"""
[構文]

loc[行の開始インデックス:終了インデックス, 列の開始インデックス:終了インデックス]

pandasでは、ほかにも様々な処理ができますので、適宜調べてみると良いでしょう。
"""


print("--- DataFrameをもっと便利に使うには？ ---")


"""
以上、Pandasの基本的な使い方について解説しました。
本記事で触れたDataFrameですが、使いこなす上で様々な関数があります。
DataFrameの関数については全て紹介すると長くなってしまう為、以下記事に譲りました。
Pandasをもっと使いこなしたい方は是非ご覧ください！
"""
