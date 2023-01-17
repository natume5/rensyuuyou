#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 Seriesの基本 ---")


"""
前回ご説明したとおり、Seriesはシーケンスオブジェクトに
indexと呼ばれるラベルをつけることができ、
DataFrameの一部として扱うことができます。
読者がコピペしやすいように記述していますが、
スクリプトを毎回書くのは手間がかかるため
ipythonを使用することをおすすめします。
"""


print("--- 生成 ---")


"""
まずはSeriesを生成してみましょう。
ラベル無しで生成する

基本的な生成方法です。
シーケンスオブジェクトをコンストラクタの引数に指定します。
リストである必要はなくnumpy.array等でもかまいません。
"""

import pandas as pd

s = pd.Series([10, 20, 30])
print(s)

"""
以下のように出力されます。

0    10
1    20
2    30
dtype: int64

まず、左側の0〜2がindexと呼ばれる行の名前です。
特に指定しない場合は0始まりの整数が付与されます。


indexにラベルをつける

indexは独自にラベルを指定することも可能です。
"""

import pandas as pd

s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(s)

"""
以下のように出力されます。

a    1
b    2
c    3
d    4
dtype: int64

indexがa、b、、、となっていることが確認できます。


辞書から生成する

以下の通り辞書から生成することも可能です。
"""

import pandas as pd

s = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s)

"""
a    1
b    2
c    3
dtype: int64
"""


print("--- Seriesにアクセスする ---")


"""
indexを指定して要素を取得することができます。
[]を使用した添字で指定する方法と、
.で指定する方法の2種類あります。
"""

import pandas as pd

s = pd.Series({'a': 1, 'b': 2, 'c': 3})
print(s['a'])    # 1が出力
print(s.a)    # 1が出力

"""
また、デフォルトのindexを使用している場合は
スライスを使用して部分を切り出すことができます。
"""

import pandas as pd

s = pd.Series([10, 20, 30, 40])
print(s[0:2])

"""
0    10
1    20
dtype: int64
"""


print("--- Seriesの更新 ---")


"""
要素を更新する際は代入します。
例えば0番目を更新する際は以下のようにします。
"""

s = pd.Series([10, 20, 30, 40])
s[0] = 100
print(s)

"""
0    100
1     20
2     30
3     40
dtype: int64

また、スライスを使用して部分的に更新することも可能です。
"""

s = pd.Series([10, 20, 30, 40])
s[0:2] = pd.Series([100, 200])    # 代入はlistでも可能
print(s)

"""
0    100
1    200
2     30
3     40
dtype: int64
"""


print("--- pythonのlist型に変換 ---")


"""
シーケンス型ですので以下でlistメソッドで変換することができます。
"""

print(list(s))


"""
[100, 200, 30, 40]
"""
