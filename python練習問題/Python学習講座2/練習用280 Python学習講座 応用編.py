#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- pandas入門 DataFrame CSV、TSV形式で入出力 ---")


"""
様々な入出力が用意されているpandasのDataFrameですが、
CSVやTSVで入出力することが一番多いのではないでしょうか。
pythonの標準ライブラリにもcsvパーサがありますが、
pandasを使用したほうがより簡単でさまざまな操作が可能なのでおすすめです。
"""


print("--- read_csv CSV、TSVを読み込む ---")


"""
CSVもTSVも読み込みはread_csvメソッドを使用します。
引数にファイル名と区切り文字を設定します。
区切り文字を設定しない場合はデフォルトでカンマが指定されます。
TSVファイルを読み込む場合、以下のように記述します。
"""

import pandas as pd

df = pd.read_csv('data1.tsv', sep='\t')
print(df)

"""
また、ヘッダーがないTSVファイルを読み込む場合はheader=Noneを指定します。
"""

df = pd.read_csv('data1.tsv', sep='\t', header=None)
print(df)

"""
             0
0   col1  col2
1     10   200
2     20   200
3     30   300

サンプルの通り、先ほどと同じデータを読み込んでみると、
ヘッダー部分がindex=0番目のデータとして扱われていることが確認できます。
"""


print("--- to_csv CSV、TSVに出力する ---")


"""
DataFrameをCSV、TSVで出力することも非常に簡単です。
to_csvメソッドでファイル名、区切り文字、indexの要否を設定します。
"""

# TSV形式でindexを出力しない場合
df.to_csv('output.tsv', sep='\t', index=False)

# TSV形式でindexを出力し、なおかつindexの列名をcol0と設定する場合
df.to_csv('output.tsv', sep='\t', index=True, index_label='col0')

"""
簡単にCSV、TSVを扱うことができますので分析をしない方にもおすすめです。
"""
