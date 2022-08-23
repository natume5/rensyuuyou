#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Tech Teacher Blog ---")
print("--- マスターしよう！PythonでのCSVファイル操作方法を徹底解説！ ---")


"""
Pythonを学習し始めた方で、CSVの扱いでつまずいている人もいるでしょう。

「PythonにおけるCSVの読み書きについて正確な方法が知りたい」
「CSVの読み書きの応用が知りたい」

このような悩みを抱えている方に、CSVの読み書きの基本から応用方法まで詳しく解説します。
"""


print("--- PythonのCSVとは ---")


"""
「CSV」とは、”Comma Separated Value”の略称で、
「 , 」で区切ってデータを並べたファイル形式を指します。
CSVファイルはアプリケーション間でデータをやり取りするときに使用されます。
CSV形式のファイルはメモ帳などのテキストエディタで作ることが可能で、
以下のように1行の文字列を半角カンマで複数の項目に分割して記述します。

1.　name , street address , birthday , pthone numder

ファイルの拡張子は「.csv」です。Excelやテキストファイルで開くことができ、編集も可能です。
CSVファイルはよく使用されるためしっかり覚えておきましょう。
"""


print("--- 【入力】PythonのCSVファイル読み込みの基本と応用 ---")


"""
PythonでCSVファイルを取り扱うには「csvモジュール」を使用するのが一般的です。
モジュールを使うことによって、
CSVファイルの読み込み・書き込みに関するさまざまな操作を素早く進めることができます。
まず、csvモジュールをインポートするところからスタートしてみましょう。
csvモジュールのインポート方法は以下の通りです。
"""

import csv

"""
PythonでCSVファイルを扱う際には最初にcsvモジュールをインポートする必要があるので覚えておきましょう。
CSVファイルの読み込みにはcsvモジュール内の「csv.readerクラス」を使用します。

基本的な使い方

実際のコードを使って基本的な使い方を説明していきます。
"""

# import csv

with open('csvファイル.csv', 'r') as f:
	reader = csv.reader(f)
	for line in reader:
		print(line)

# ['red ', ' blue ', ' green ', ' purple ', ' black']
# ['apple ', ' grape ', ' banana ', ' orange ', ' strawberry']
# ['cat ', ' dog ', ' pig ', ' tiger ', ' elephant']

"""
PythonでCSVファイルを扱うには、まずopen関数でファイルを取り込む必要があります。
上の例のように、第1引数に開くCSVファイルを、
第2引数に「’r’」を指定することで読み込みができるようになります。
そして、「csv . reader ( )」の引数にopen( )で開いたファイルオブジェクト「f」を渡して
for文で反復処理させることによって行を1つずつ取得することができます。


CSVファイルの具体例

次のCSVファイル「sample . csv」を読み込んでみましょう。

csvファイル.csv
red , blue , green , purple , black
apple , grape , banana , orange , strawberry
cat , dog , pig , tiger , elephant
"""

import csv

with open("csvファイル.csv", "r") as f:    # ファイルを開く
	reader = csv.reader(f)    # ファイルからデータを読み込む
	for line in reader:    # for文で1行ずつ取得する
		print(line)    # lineの中身を表示

# ['red ', ' blue ', ' green ', ' purple ', ' black']
# ['apple ', ' grape ', ' banana ', ' orange ', ' strawberry']
# ['cat ', ' dog ', ' pig ', ' tiger ', ' elephant']

"""
このように、各行のデータを要素に持ったリストが取得できました。

行・列・要素を取得

CSVファイル全体を1つの二次元リストに格納することもできます。
"""

with open("csvファイル.csv", "r") as f:
	reader = csv.reader(f)
	line = [row for row in reader]

"""
行を取得する方法は下記の通りです。
"""

print(line[1])

# ['apple ', ' grape ', ' banana ', ' orange ', ' strawberry']

"""
要素を取得する方法は下記通りです。
"""

print(line[1][1])

# grape

"""
また、列を取得したい場合は行と列を入れ替える転置を行ってから
「インデックス［ ］」で指定するとできますよ。


区切り文字を指定する

「csv.reader( )」は、区切り文字を「 , 」として扱うのがデフォルトです。
これはCSVファイルを念頭に置いているためですが、時には次のようなファイルを扱いたい場合があります。

#example.txt
red blue green purple black
apple grape banana orange strawberry
cat dog pig tiger elephant

このファイルでは半角スペースでデータが区切られています。
これはCSVファイルではなくTXTファイルとして保存されていますが、
csvモジュールを使えばこのようなデータを処理することも可能です。
"""

with open('csvファイル.csv', 'r') as f:
	reader = csv.reader(f, delimiter=' ')    # デリミタに半角スペースを指定
	line = [row for row in reader]

print(line)

# [['red', ',', 'blue', ',', 'green', ',', 'purple', ',', 'black'], 
# ['apple', ',', 'grape', ',', 'banana', ',', 'orange', ',', 'strawberry'], 
# ['cat', ',', 'dog', ',', 'pig', ',', 'tiger', ',', 'elephant']]

"""
このように、csv.reader()の第2引数として「delimiter = 区切り文字」を指定することで、
区切り文字で区切られたデータを処理することができます。
上の例では区切り文字として半角スペース「’ ’」を指定しています。


辞書として読み込み

各行を辞書として読み込むには「csv.DictReader」を使用します。
通常のcsv.readerのように動作しますが、読み込んだ情報を辞書にマッピングします。

1.　＃　CSVファイル「examplebirthday.csv」
2.　name , department , birthday
3.　Adam ,Engineering Department , July 7
4.　Alice , Office work , January 1

上記のファイルを辞書として読み込んでみましょう。
"""
"""
import csv

with open('examplebirthday.csv', 'r') as csv_file:
	csv_reader = csv.DictReader(csv_file)
	line_count = 0
	for row in csv_reader:
		if line_count == 0:
			print(f'Column names are{','.join(row)}')
		line_count += 1

print(f'\t{row [‘name’]} works in the { row [‘department’]}department, and was born in {row[‘birthday’]}.')
line_count += 1
print(f'Processed {line_count} lines.')
"""
"""
このように文字列のリストを処理するのではなく、csvデータを辞書に直接読み込むこともできますよ。
"""


print("--- 【出力】PythonのCSVファイル書き込みの基本と応用 ---")


"""
CSVファイルの書き込みにはcsvモジュール内の「csv . writerクラス」を使用します。

基本的な使い方

「writerow( )メソッド」を使用することによって、csvファイルに1行の書き込みができます。
"""

import csv

word = 'red, blue'
words = word.split(',')

with open('csvファイル.csv', 'w') as f:    # 'w'=書き込み
	writer = csv.writer(f)
	writer.writerow(words)

# red, blue

"""
上記のようにopen( )の第2引数に「’w’」を指定することによって書き込みができるようになります。

追記する方法

CSVファイルにデータｗ追加するには、open関数の第2引数に「’a’」を指定します、

1.　with open ( ‘csvファイル.csv’ , ‘a’ ) as f :　　　＃　’a’＝追記
2. 　writer = csv . writer ( f )
3　writer . writerow ( [ ‘追記したいもの’ } )

ファイルが存在する場合は末尾に追加され、ファイルが存在しない場合は新しくファイルが作成されますよ。


区切り文字を指定する

CSVファイルによく似たファイル形式に「TSVファイル」があります。
CSVの「C」が「コンマ」の略だったのに対して、「T」は「タブ」の略です。
その名の通り、TSVファイルとはタブでデータを区切ったファイル形式になります。
TSVファイルとして保存したい場合は、次のようにcvs . writer( )の第2引数を
「delimiter=’\t’」とするといいですよ。
"""

with open("example.tsv", "w") as f:
	writer = csv.writer(f, delimiter='\t')
	writer.writerow(line)

with open("example.tsv") as f:
	print(f.read())

# "[""['red"", ""',"", ""'"", 'blue', ""',"", ""'"", 
# 'green', ""',"", ""'"", 'purple', ""',"", ""'"", ""black']""]"	
# "[""['apple"", ""',"", ""'"", 'grape', ""',"", ""'"", 
# 'banana', ""',"", ""'"", 'orange', ""',"", ""'"", ""strawberry']""]"	
# "[""['cat"", ""',"", ""'"", 'dog', ""',"", ""'"", 
# 'pig', ""',"", ""'"", 'tiger', ""',"", ""'"", ""elephant']""]"

"""
辞書として書き込み

「csv . DictWriter」は各行に辞書を書き込みます。
"""

import csv

with open('csvファイル.csv', 'w') as csv_file:
	fieldnames = ['name', 'dept', 'birth']
	writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

	writer.writeheader()
	writer.writerow({'name': 'Adam', 'dept': 'Engineering Department',
	'birth': 'July 7' })
	writer.writerow({'name': 'Alice', 'dept': 'Office work',
	'birth': 'January 1' })


print("--- まとめ ---")


"""
今回、CSVの読み書きの基本から応用方法まで詳しく説明してきましたがいかがでしたでしょうか。

今回の要点をまとめると以下のようになります。

    CSVとはデータを「 , 」で区切ったファイル
    PythonでCSVファイルを扱うには「csvモジュール」を使用
    CSVファイルの読み込みには「csv . readerクラス」を使用
    CSVファイルの書き込みには「csv . writerクラス」を使用

学習し始めたばかりだとつまずいてしまうこともあるでしょう。
スムーズに学習を行えるように、しっかり理解を深めておきましょう。
"""
