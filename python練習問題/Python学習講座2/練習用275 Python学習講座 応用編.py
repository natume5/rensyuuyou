#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrameをgroupbyで集計する ---")


"""
私が実務でよく使うものの1つがgroupbyで、
例えば商品カテゴリー毎に合計やばらつきを確認したい場合などが挙げられます。
無論、SQLでも同様のことは大抵できてしまいますが、
例えば形態素解析した結果の単語ごとの集計をかけたい場合など
Pythonで一気通貫でやる場合にはpandasを使うのが便利ですね。
"""


print("--- groupby ---")


"""
その名の通りDataFrameをgroupbyで集計します。
groupbyの戻り値で得られるGroupByオブジェクトに対し
mean(), min(), max(), sum()などのメソッドを適用すると、
グループごとの平均、最小値、最大値、合計などの統計量を算出することが可能です。
使い方は簡単ですので、サンプルを見てみましょう。
カテゴリーとタグ毎になんらかの量が設定されているDataFrameに対し、
集計をかけてみます。引数に集計対象の列名を設定します。
複数でgroupbyをかけたい場合はリストで設定します。
"""

import pandas as pd

df = pd.DataFrame([['cate1', 'tag1', 150], ['cate1', 'tag2', 210],
	['cate2', 'tag2', 80], ['cate2', 'tag1', 310]],
	columns=['category', 'tag', 'value'])

print(df)

# category毎の合計を算出する
print(df.groupby('category').sum())

# category, tag毎の件数を算出する
print(df.groupby(['category', 'tag']).count())

# tag毎のばらつきを算出する
print(df.groupby(['tag']).std())

"""
  category   tag  value
0    cate1  tag1    150
1    cate1  tag2    210
2    cate2  tag2     80
3    cate2  tag1    310

          value
category
cate1       360
cate2       390

               value
category tag
cate1    tag1      1
         tag2      1
cate2    tag1      1
         tag2      1
         
           value
tag
tag1  113.137085
tag2   91.923882

いかがでしょうか。集計が簡単に使用できますので便利ですね。
"""
