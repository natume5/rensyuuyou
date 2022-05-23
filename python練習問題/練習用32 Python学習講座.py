#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　csvモジュール CSVファイルの読み書き---")


"""
csvモジュール

標準ライブラリのcsvモジュールを使用するとCSVファイルの読み書きができます。

CSVの読み込み
csv.reader

csv.readerを使用してCSVファイルの読み込みを行います。
以下のサンプルは、カレントディレクトリにあるdata.csvというCSVファイルを1行ずつリストで出力しています。
"""

import csv


# CSVファイルの読み込み
with open('data.csv', 'r') as f:
	reader = csv.reader(f)    # readerオブジェクトを生成
	print(type(reader))    # readerオブジェクトはlist型
	for row in reader:
		# 1行ずつリストで出力される
		print(row)


"""
ヘッダーを読み飛ばす

また、ヘッダー付きのCSVファイルでヘッダーを読み飛ばしたりループ前に取得したい場合は
以下のようにnext関数を使用します。
"""
"""
with open('data.csv', 'r') as f:
	reader = csv.reader(f)
	header = next(reader)    # listに格納されるため、読み飛ばしたい場合はnextを使用する
	for row in reader:
		print(row)
"""

"""
TSVファイル 区切り文字を変える

TSVファイル等でカンマ以外の区切り文字を使用したい場合は引数でdelimiterを指定します。
"""

# import csv

# TSVファイルの読み込み
with open('data.tsv', 'r') as f:
	reader = csv.reader(f, delimiter='\t')    # delimiterを指定
	for row in reader:
		print(row)

"""
CSVファイルの書き込み

リストデータをCSVファイルとして出力することも可能です。
[[1行目][2行目][3行目][4行目]...[最終行目]]といった形式で、
入れ子のリストでデータを指定し、csv.writerで出力します。
"""

# import csv


# CSVファイルの書き込み
list_data = [['a', 'b', 'c'], [1, 2, 3], [4, 5, 6]]
with open('output.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	writer.writerows(list_data)



