#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrameの値を置換する ---")


"""
業務データはものによっては誤記や入力時のエラーなどで何度か置換をして
クレンジングする場合がありますが、
pandasのDataFrameにはreplaceというメソッドを使用すると
置換処理を行うことができます。
"""


print("--- replace 値を置換する ---")


"""
基本的な置換

replaceメソッドで置換することができます。
例えば、orangeがorangggとなっているデータがあった場合、
以下のように置換して修正することができます。
"""

import pandas as pd

df = pd.DataFrame([['apple', 10], ['oranggg', 20],
	['banana', 30]], columns=['name', 'price'])

print(df.replace('oranggg', 'orange'))

print(df)

"""
     name  price
0   apple     10
1  orange     20
2  banana     30

      name  price
0    apple     10
1  oranggg     20
2   banana     30


正規表現による置換

また、引数にregex=Trueを指定することで正規表現を使用することもできます。
先ほどの置換を以下のように書くこともできます。
"""

print(df.replace('.*ggg.*', 'orange', regex=True))

"""
     name  price
0   apple     10
1  orange     20
2  banana     30


欠損値の0埋め

よく使うのが欠損値の置換です。
NaNを0で埋めたい場合は以下のようにnp.NaNで置換します。
"""

import pandas as pd
import numpy as np

df = pd.DataFrame([[1, 10], [None, 20], [3, None]],
	columns=['col1', 'col2'])

print(df.replace(np.NaN, 0))

"""
   col1  col2
0   1.0  10.0
1   0.0  20.0
2   3.0   0.0
"""
