#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- pandas入門  DataFrame htmlで入出力---")


"""
htmlを出力する

htmlに出力することも可能です。分析結果をwebに出力する場合などに重宝するでしょう。

df.to_html('sample.html')

引数に出力ファイル名を指定するだけでhtmlのtableで出力することができます。
"""

import pandas as pd

dfs = pd.read_html('https://www.data.jma.go.jp/obd/stats/etrn/\
view/rankall.php')

df = dfs[0]
print(df)

#     順位  都道府県     地点   観測値             現在観測を実施
#    順位  都道府県     地点     ℃          起日 現在観測を実施
# 0    1   静岡県   浜松 *  41.1  2020年8月17日       ○
# 1    〃   埼玉県   熊谷 *  41.1  2018年7月23日       ○
# 2    3   岐阜県     美濃  41.0   2018年8月8日       ○
# 3    〃   岐阜県     金山  41.0   2018年8月6日       ○
# 4    〃   高知県    江川崎  41.0  2013年8月12日       ○
# 5    6   静岡県     天竜  40.9  2020年8月16日       ○
# 6    〃   岐阜県    多治見  40.9  2007年8月16日       ○
# 7    8   新潟県     中条  40.8  2018年8月23日       ○
# 8    〃   東京都     青梅  40.8  2018年7月23日       ○
# 9    〃   山形県   山形 *  40.8  1933年7月25日       ○
# 10  11   山梨県   甲府 *  40.7  2013年8月10日       ○
# 11  12   新潟県     寺泊  40.6  2019年8月15日       ○

df.to_html('sample.html')

# <table border="1" class="dataframe">
#   <thead>
#     <tr>
#       <th></th>
#       <th>順位</th>
#       <th>都道府県</th>
#       <th>地点</th>
#       <th colspan="2" halign="left">観測値</th>
#       <th>現在観測を実施</th>



print("--- pandas入門  DataFrame クリップボードで入出力---")


"""
IPythonなどでインタラクティブな検証をしている時、
いちいちファイルで入出力すると面倒ですし、不要なファイルが溜まってきます。
そんなとき、クリップボードで入出力できるので是非活用してみてください。

read_clipboard クリップボードから読み込む

まず、エクセルなどで適当な範囲がクリップボードにコピーされているものとします。
インタラクティブモードかIPythonを起動した状態で以下のコマンドを実行すると、
クリップボードの内容がDataFrameに格納されます。

df = pd.read_clipboard(sep='\t')

sepで区切り文字が指定できます。
to_clipboard クリップボードに書き込む

to_clipboardでDataFrameの内容をクリップボードに書き込むことができます。

df.to_clipboard()


Python で pandas モジュールを使用してテキストをクリップボードにコピーする


主にデータ分析と機械学習に使用される pandas モジュールには、
クリップボードのサポートも組み込まれています。関数 to_clipboard() を使用して、
テキストを Pandas DataFrame に入力または渡すことを条件に、
pandas のクリップボードにコピーできます。

次のコードは、pandas モジュールを使用して、Python でテキストをクリップボードにコピーします。

import pandas as pd
df=pd.DataFrame(['Text to copy'])
df.to_clipboard(index=False,header=False)
"""
