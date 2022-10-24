#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- csvモジュール CSVファイルの読み書き ---")


"""
今回はCSVファイルを扱える標準ライブラリのcsvモジュールについて解説します。
集計や分析を場合はサードパーティ製のpandasを使用することをおすすめしますが、
単純な処理であればこれも十分使えます。
"""


print("--- csvモジュール ---")


"""
標準ライブラリのcsvモジュールを使用するとCSVファイルの読み書きができます。
"""


print("--- CSVの読み込み ---")


"""
csv.reader

csv.readerを使用してCSVファイルの読み込みを行います。
以下のサンプルは、カレントディレクトリにある
data.csvというCSVファイルを1行ずつリストで出力しています。
"""

import csv

# CSVファイルの読み込み
with open('data.csv', 'r', encoding='UTF-8') as f:
	reader = csv.reader(f)    # readerオブジェクトを生成
	print(type(reader))    # readerオブジェクトはlist型  <class '_csv.reader'>
	for row in reader:
		# 1行ずつリストで出力される
		print(row)    # ['data.csv']


"""
ヘッダーを読み飛ばす

また、ヘッダー付きのCSVファイルでヘッダーを読み飛ばしたり
ループ前に取得したい場合は以下のようにnext関数を使用します。
"""

with open('data.csv', 'r') as f:
	reader = csv.reader(f)
	header = next(reader)
	# listに格納されるため、読み飛ばしたい場合はnextを使用する
	for row in reader:
		print(row)    #


"""
TSVファイル 区切り文字を変える

TSVファイル等でカンマ以外の区切り文字を使用したい場合は
引数でdelimiterを指定します。
"""

import csv

# TSVファイルの読み込み
with open('data.tsv', 'r', encoding='UTF-8') as f:
	reader = csv.reader(f, delimiter='\t')    # delimiterを指定
	for row in reader:
		print(row)    # ['data.tsvの中身を読み込んでいます。']


print("--- CSVファイルの書き込み ---")


"""
リストデータをCSVファイルとして出力することも可能です。
[[1行目][2行目][3行目][4行目]...[最終行目]]といった形式で、
入れ子のリストでデータを指定し、csv.writerで出力します。
"""

import csv

# CSVファイルの書き込み
list_data = [['a', 'b', 'c'], [1, 2, 3], [4, 5, 6]]
with open("output.csv", "w", newline='') as f:
	writer = csv.writer(f)
	writer.writerows(list_data)
