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


print("--- pandas入門  DataFrameの入出力---")


"""
pandasのDataFrameはこれまでのサンプルではハードコードして値を記述していましたが、
実務ではCSVなどのファイルや、DB、Excelなどから入出力することが一般的です。


代表的な入出力

DataFrameと連携できる代表的な入出力について列挙します。詳細はリンク先の説明をご参照ください。


pandas入門 DataFrame CSV、TSV形式で入出力

様々な入出力が用意されているpandasのDataFrameですが、
CSVやTSVで入出力することが一番多いのではないでしょうか。
pythonの標準ライブラリにもcsvパーサがありますが、
pandasを使用したほうがより簡単でさまざまな操作が可能なのでおすすめです。


read_csv CSV、TSVを読み込む

CSVもTSVも読み込みはread_csvメソッドを使用します。
引数にファイル名と区切り文字を設定します。
区切り文字を設定しない場合はデフォルトでカンマが指定されます。

TSVファイルを読み込む場合、以下のように記述します。
"""

df = pd.read_csv('data2.tsv', sep='\t')
print(df)

#      col1  col2
# 0      10   200
# 1      20   200
# 2      30   300

"""
また、ヘッダーがないTSVファイルを読み込む場合はheader=Noneを指定します。
"""

df = pd.read_csv('data2.tsv', sep='\t', header=None)

print(df)

#       0     
# 0    col1  col2
# 1      10   200
# 2      20   200
# 3      30   300

"""
サンプルの通り、先ほどと同じデータを読み込んでみると、
ヘッダー部分がindex=0番目のデータとして扱われていることが確認できます。


to_csv CSV、TSVに出力する

DataFrameをCSV、TSVで出力することも非常に簡単です。
to_csvメソッドでファイル名、区切り文字、indexの要否を設定します。
"""

# TSV形式でindexを出力しない場合
df.to_csv('output.tsv', sep='\t', index=False)

# TSV形式でindexを出力し、なおかつindexの列名をcol0とする場合
print(df.to_csv('output.tsv', sep='\t', index=True, index_label='col0'))


print("--- pandas入門  DataFrame excelファイルで入出力---")


"""
非IT部門の場合、データ管理をWebではなくExcelで行っていることが多々あると思いますが、
pandasではそういったExcelデータを吸い上げたりExcelで出力することができます。


事前準備 Excel入出力モジュール

Excelと連携する場合、事前に以下のモジュールをインストールしてください。

# 読み込みで必要
pip install xlrd

# 書き込みで必要
pip install openpyxl

read_excelでExcelファイルを読み込む

read_excelメソッドでファイル名を指定します。
その他、シート名、スキップする行、列数などを指定することが可能です。
CSVなどと比較してExcel自体が複雑ですのでオプションが非常に多いです。
全ては公式をご参照ください。


# 最初のシートを読み込む
df = pd.read_excel('sample.xls')

# シート名を指定し、1行目をスキップする場合
df = pd.read_excel('excelsample.xls', sheet_name='表紙', skiprows=1)
"""

"""
to_excelでExcelファイルに書き込む
"""

# とりあえず書き出す
df.to_excel('output.xlsx')

# シート名を指定する
df.to_excel('output.xlsx', sheet_name='sample')

"""
いかがでしょうか。Javaのpoiなどと比較すると格段に簡単で便利ですね。
データ分析以外にも業務用のバッチでも使用できると思います。
"""


print("--- pandas入門  DataFrame  htmlで入出力---")


"""
スクレイピングしたデータを分析することがよくあると思いますが、
pandasはurlやhtmlを指定するとtableタグを自動で見つけてDataFrameに格納してくれます。
逆にDataFrameの内容をhtmlのtableで出力することも可能です。


read_html htmlからDataFrameを生成する

read_htmlメソッドを使用すると、htmlからDataFrameを生成することができます。
事前準備

予め依存するhtmlパーサのモジュールをインストールします。

pip install lxml
pip install bs4
pip install html5lib

urlを指定する

read_htmlメソッドの引数にurlを指定すると、
httpアクセスを行いhtmlを取得しtableタグの中身をDataFrameに格納してくれます。

試しに気象庁のサイトのランキングデータを取得してみましょう。
https://www.data.jma.go.jp/obd/stats/etrn/view/rankall.php


複数のtableがありますが、シーケンスで取得できます。
一番上のtableを取得する場合は0を指定します。
"""

dfs = pd.read_html('https://www.data.jma.go.jp/obd/stats/etrn/\
view/rankall.php')

df = dfs[0]
print(df)

#     順位  都道府県     地点   観測値             現在観測を実施
#     順位  都道府県     地点     ℃          起日 現在観測を実施
# 0    1   静岡県       浜松 *  41.1  2020年8月17日       ○
# 1    〃   埼玉県      熊谷 *  41.1  2018年7月23日       ○
# 2    3   岐阜県       美濃  41.0   2018年8月8日       ○
# 3    〃   岐阜県      金山  41.0   2018年8月6日       ○
# 4    〃   高知県      江川崎  41.0  2013年8月12日       ○
# 5    6   静岡県       天竜  40.9  2020年8月16日       ○
# 6    〃   岐阜県      多治見  40.9  2007年8月16日       ○
# 7    8   新潟県       中条  40.8  2018年8月23日       ○
# 8    〃   東京都      青梅  40.8  2018年7月23日       ○
# 9    〃   山形県      山形 *  40.8  1933年7月25日       ○
# 10  11   山梨県       甲府 *  40.7  2013年8月10日       ○
# 11  12   新潟県       寺泊  40.6  2019年8月15日       ○

"""
cssやxpath形式で指定するよりも遥かに簡単にデータが取得できました。


htmlを指定する

tableタグ以外にもデータの表題などを取得したい場合があるかと思いますが、
htmlを引数に指定することも可能です。requestsなどでhtmlを取得しtableはpandasで取得し、
その他はbs4などでパースする、という方法も可能です。
htmlを指定する場合は以下のように書き換えることができます。
"""

import requests

r = requests.get('https://www.data.jma.go.jp/obd/stats/etrn/\
view/rankall.php')
r.encoding = 'UTF-8'
html = r.text
dfs = pd.read_html(html)

"""
request、bs4については以下を参照してください。
requestsの使い方 webサイトのデータを取得する
beautifulsoup4 htmlをパース、スクレイピングする その1
beautifulsoup4 htmlをパース、スクレイピングする その2
"""
