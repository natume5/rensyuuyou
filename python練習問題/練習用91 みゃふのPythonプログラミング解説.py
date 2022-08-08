#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- CSVモジュールの使い方 ---")


"""
Pythonでcsvを扱う方法はいくつかありますが、
ここでは最もスタンダードな標準モジュールである「csv」
を使ってcsvの読み書きができる方法を解説します。
csvはカンマ区切りのテキストファイルなので、
通常のファイル読み書きを使っても良いですが、
csvモジュールを使うことでより簡単にcsvの操作が行えるようになります。

sample csv.csv ファイル

key1,key2,key3
a-1,a-2,a-3
b-1,b-2,b-3

sample.tsv ファイル

key1	key2	key3
a-1	a-2	a-3
b-1	b-2	b-3

sample2 csv.csv ファイル

a-1,a-2
b-1,b-2

"""


print("--- csvファイルの読み込み ---")


"""
csvファイルの読み込みから見ていきましょう。


リスト形式での読み込み

読み込んだデータをリスト形式で受け取りたい場合はreader()を使います。
"""

import csv

with open('./sample csv.csv') as f:
	csv_obj = csv.reader(f)
	print(csv_obj)
	for row in csv_obj:
		print(row)
# <_csv.reader object at 0x000002756BC938E0>
# ['key1', 'key2', 'key3']
# ['a-1', 'a-2', 'a-3']
# ['b-1', 'b-2', 'b-3']

"""
csvモジュールを使う場合もwith openでまずファイルの読み込みをする必要があります。
読み込み終わったらreader()でcsv.readerのオブジェクトを作成します。
この中に読み込んだcsvデータが入っているイメージです。
読み込んだcsv.readerオブジェクトはfor..inで行ごとにデータを取得できるようになります。
取得したデータはリスト形式なので、単純にcsvファイルを読み込むよりも
扱いやすくなっているのがわかります。
ちなみにcsvモジュールを使わない場合は次のようになります。
"""

with open('./sample csv.csv') as file:
	while True:
		include_break_line = file.readline()
		row = include_break_line.rstrip()
		if row:
			print(row.split(','))
		else:
			break

# ['key1', 'key2', 'key3']
# ['a-1', 'a-2', 'a-3']
# ['b-1', 'b-2', 'b-3']
"""
結果は同じになりますが、csvモジュールを使った方がスッキリするのが分かります。


デリミタの指定

csv.reader()はデフォルトでカンマ「,」をデリミタ（区切り文字）としていますが、
delimiter引数を指定することで他のデリミタに変更できます。
例えばタブ区切りになっているファイル(正確にはtsvファイルと言います)
は次のようにすることで同じようにリスト形式で読み込めます。
"""

import csv

with open('./sample.tsv') as f:
	csv_obj = csv.reader(f, delimiter='\t')    # デリミタを指定する
	print(csv_obj)
	for row in csv_obj:
		print(row)

# <_csv.reader object at 0x00000144DDB43E80>
# ['key1', 'key2', 'key3']
# ['a-1', 'a-2', 'a-3']
# ['b-1', 'b-2', 'b-3']

"""
辞書形式での読み込み

csvファイルを辞書形式で読み込みたい場合はDictReader()を使います。
DictReader()はデフォルトで1行目の値がキーとして扱われます。
"""

import csv

with open('./sample csv.csv') as f:
	csv_obj = csv.DictReader(f)
	print(csv_obj)
	for row in csv_obj:
		print(row)

# <csv.DictReader object at 0x00000296DEAB1F70>
# {'key1': 'a-1', 'key2': 'a-2', 'key3': 'a-3'}
# {'key1': 'b-1', 'key2': 'b-2', 'key3': 'b-3'}

"""
DictReader()を使うことでOrderedDict形式でデータを取得できました。
OrderedDictは要素を入れた順序を保持してくれる（つまり順序付きの）辞書です。
当然辞書形式なので、keyを指定することで要素の取得が可能です。
"""

import csv

with open('./sample csv.csv') as f:
	csv_obj = csv.DictReader(f)
	print(csv_obj)
	for row in csv_obj:
		print(row['key2'])

# <csv.DictReader object at 0x000002533CED27C0>
# a-2
# b-2

"""
また、csvに見出しがない場合はfieldnames引数を指定することで、
そのタイミングでKeyを設定できます。
"""

import csv

with open('./sample2 csv.csv') as f:
	csv_obj = csv.DictReader(f, fieldnames=['key1', 'key2'])
	for row in csv_obj:
		print(row)

# {'key1': 'a-1', 'key2': 'a-2'}
# {'key1': 'b-1', 'key2': 'b-2'}


print("--- csvファイルの書き込み ---")


"""
次にcsvモジュールを使った書き込みについて見ていきましょう。

リスト形式での書き込み

リストを使ってcsvの書き込みをしたい場合はwriter()を使います。
"""

import csv

with open('./written.csv', 'w') as f:
	csv_obj = csv.writer(f)
	csv_obj.writerow(['d-1', 'e-1'])
	csv_obj.writerow(['d-2', 'e-2'])

with open('./written.csv') as f:
	print(f.read())

# d-1,e-1
# d-2,e-2

"""
書き込む場合はwith openのオプションで「w(またはa)」を指定する必要があります。
読み込み終わったらwriter()に読み込んだファイルオブジェクトを渡します。
csvモジュールを使って書き込みをするにはwriterrow()にリストを渡します。
なお、書き込みの場合もデリミタを指定できます。
tsvファイルを作成したい場合はデリミタにタブを指定します。
"""

# コードの一部
with open('./written.tsv', 'w') as f:
	csv_obj = csv.writer(f, delimiter='\t')    # デリミタにタブを指定

with open('./written.tsv') as f:
	print(f.read())


"""
csvファイルの追記がしたい場合

既に存在するcsvファイルに追記したい場合は、open時のオプションを「a」にします。
"""

# import csv

with open('./written.csv') as f:
	print('追記前')
	print(f.read())

with open('./written.csv', 'a') as f:    # オプションを追記にする
	csv_obj = csv.writer(f)
	csv_obj.writerow(['d-2', 'e-2'])

with open('./written.csv') as f:
	print('追記後')
	print(f.read())

# 追記前
# d-1,e-1
# d-2,e-2

# 追記後
# d-1,e-1
# d-2,e-2
# d-2,e-2

"""
追記前のファイルに対して新しい行が追加されているのが分かります。

辞書形式での書き込み

辞書でcsvファイルに書き込みをする場合はDictWriter()を使います。
2つ目の引数にヘッダ行になるリストを指定します（必須）。
"""

import csv

with open('./written_dict.csv', 'w') as f:
	csv_obj = csv.DictWriter(f, ['key1', 'key2', 'key3'])
	csv_obj.writerow({'key1': 'd-1', 'key2': 'e-1', 'key3': 'f-1'})
	csv_obj.writerow({'key1': 'd-2', 'key3': 'f-2'})

with open('./written_dict.csv') as f:
	print(f.read())

# d-1,e-1,f-1
# d-2,,f-2

"""
2行目の辞書にはkey2の要素がありません。
この場合は結果のようにスキップされ、空でデータが書き込まれます。

またこのDictWriter()ですが、デフォルトでは2つ目の引数のリストに
存在しないキーを含んだ辞書をwriterrow()に渡すとエラーになります。

※コードの一部    
　　csv_obj = csv.DictWriter(f, ['key1', 'key2', 'key3'])
csv_obj.writerow({'key1':'d-1', 'key2':'e-1', 'key3':'f-1', 'key4:g-1'}) #key4はリストに含まれてない

[出力結果]

ValueError: dict contains fields not in fieldnames: 'key4'

これはextrasaction引数にraiseという文字列がデフォルトで設定されているためです。
含まれていないキーを無視したい場合はignoreを設定します。
"""

import csv

with open('./written_dict2.csv', 'w') as f:
	csv_obj = csv.DictWriter(f, ['key1', 'key2', 'key3'], extrasaction='ignore')
	csv_obj.writerow({'key1': 'd-1', 'key2': 'e-1', 'key3': 'f-1', 'key4': 'g-1'})
	
with open('./written_dict2.csv') as f:
	print(f.read())

# d-1,e-1,f-1
