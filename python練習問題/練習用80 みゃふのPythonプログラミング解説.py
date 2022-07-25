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


















