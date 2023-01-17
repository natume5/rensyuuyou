#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrameの生成の基本 ---")


"""
次に分析の中核となるDataFrameの生成についてです。
まずは操作に馴染むためにリストなどの
シーケンシャルオブジェクトからDataFrameを生成する方法について学習します。
別項にて説明しますが、実際の業務ではこのページのサンプルのように
コードに値を書くことはまずなく、

    CSVやTSVなどのテキストファイル
    Excel
    MySQLやPostgresのようなRDB

などからデータを取得してDataFrameを生成することが一般的です。
（サンプルでは読者がコピペしやすいように記述していますが、
スクリプトを毎回書くのは手間がかかるためipythonを使用することをおすすめします。）
"""


print("--- DataFrameの生成の基本 ---")


"""
index、columnを指定しないで生成する

まずは2列×4行のDataFrameを生成してみましょう。
DataFrameのコンストラクタに2次元リストを指定します。
"""

import pandas as pd

df = pd.DataFrame([[1, 10], [2, 20], [3, 30]])
print(df)

"""
以下のように出力されます。

   0   1
0  1  10
1  2  20
2  3  30

出力結果の上段がcolumnです。
生成時に指定していなかったためデフォルト値として0,1が設定されています。
出力結果の左側がindexです。
こちらも生成時に指定していなかったためデフォルト値として0〜3が設定されています。


index、columnを指定する

こちらでも説明しましたが、DataFrameではindex、columnと呼ばれる
行、列のラベルを設定することができます。
生成時の引数にそれぞれindex、columnsを指定すると設定されます。
"""

df = pd.DataFrame([[1, 10], [2, 20], [3, 30], [4, 40]],
	index=['a', 'b', 'c', 'd'], columns=['col1', 'col2'])
print(df)

"""
   col1  col2
a     1    10
b     2    20
c     3    30
d     4    40

列名としてcol1、col2が、行名としてa〜dが設定されていることが確認できます。


辞書から生成する

Seriesと同じく辞書から生成することも可能です。
"""

data = {'col1': [1, 2, 3], 'col2': [10, 20, 30]}
df = pd.DataFrame(data)
print(df)

"""
   col1  col2
0     1    10
1     2    20
2     3    30
"""


print("--- SeriesからDataFrameを生成する ---")


"""
最後にSeriesからDataFrameを生成する方法についてです。
この方法はindexを考慮してマージしてくれるため非常に便利でよく使います。
"""

s1 = pd.Series([100, 101, 102], index=['a', 'b', 'c'])
s2 = pd.Series([100, 101, 102], index=['b', 'c', 'd'])
df = pd.DataFrame({'col1': s1, 'col2': s2})
print(df)

"""
2つの生成済みのSeriesがあり、ここからDataFrameを生成しています。
このときSeriesで設定されているindexが同じものを同じ行としてマージしてくれます。
当該indexがない場合はNaNが設定されます。
何らかのDataFrameをもとに計算した結果を複数のSeriesに格納し、
マージして新たなDataFrameを生成する、
という操作は時系列データ分析でよく使用する方法です。
"""
