#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrameのソート ---")


"""
pandasのメリットの1つとして多次元のリストを
簡単にソートすることができる点が挙げられると思います。
データ分析以外にもETL等でソートが必要な場合は
pandasの使用を検討してみてください。
"""


print("--- DataFrameのソート ---")


"""
DataFramオブジェクトのsort_valuesメソッドを使用すると
簡単にソートすることができます。
第1引数にソート対象のカラムリスト、ascendingで昇順/降順を指定します。
サンプルです。3列のDataFrameをソートしてみましょう。
"""

import pandas as pd

df = pd.DataFrame([[3, 10, 200], [2, 30, 100], [4, 40, 300],
	[1, 20, 200]], columns=['col1', 'col2', 'col3'])

print(df)

# col1で昇順、col2で降順にソートしてみる。
print(df.sort_values(['col1', 'col2'], ascending=[True, False]))

"""
   col1  col2  col3
0     3    10   200
1     2    30   100
2     4    40   300
3     1    20   200

   col1  col2  col3
3     1    20   200
1     2    30   100
0     3    10   200
2     4    40   300
"""
