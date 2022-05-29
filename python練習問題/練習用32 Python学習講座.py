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


print("--- Python入門　正規表現---")


"""
Pythonの正規表現
正規表現

正規表現はメタ文字と呼ばれる文字を利用して文字列の検索パターンを表すことができます。
任意のテキストの中からこの検索パターンに合致する文字列を抽出したり置換することができます。
例えば、テキストの改行のみの行にマッチさせたい場合、'^\n$'と記述します。^は行頭、\nは改行を表します。
学習の前に、基本的な正規表現について簡単に俯瞰しておきましょう。簡単な例を以下に示します。

特殊文字 	意味
. 	        改行以外の任意の文字
^ 	        文字列先頭
$ 	        文字列末尾
ab|cd 	    文字列abか文字列cdのどちらかにマッチ（いずれか）
[ab-d] 	    aとb〜dにマッチ（範囲指定）
[^ab-d] 	aとb〜d以外にマッチ（否定）
.(abc). 	xabcxなどにマッチ（グループ化）
[ab]{2} 	aかbが２回繰り返される
[ab]{2,5} 	aかbが２〜5回繰り返される
[ab]{2,} 	aかbが２回以上繰り返される
+ 	        直前の文字が１回以上出現
* 	        直前の文字が0回以上出現
? 	        直前の文字が0回もしくは１回出現


エスケープ

特殊文字を表す場合には\記号を使用します。
また、\自身のエスケープにも\を使用します。簡単な例を以下に示します。

例 	意味
\d 	任意の10進数文字
\D 	任意の非10進数文字
\w 	任意の単語文字（[a-zA-Z0-9_] と等価）
\W 	任意の非単語文字（[^a-zA-Z0-9_] と等価）
\s 	任意の空白文字（スペース、タブ、\r、\n、\v）
\S 	任意の非空白文字
\b 	単語の境界
\n 	改行（New Line）
\r 	キャリッジ・リターン
\t 	タブ
\. 	ピリオド
\\ 	\マーク


reモジュール

reモジュールはPythonの標準ライブラリで、以下のimport文で使用することができます。

import re

よくある正規表現ライブラリと同じく以下の機能が利用可能です。

    置換
    分割
    検索


正規表現で指定した文字列を置換する

それではreモジュールを使用してみましょう。
まずは、データクレンジング等のデータ分析の前処理でよく使用する文字列置換からです。
sub関数を使用します。

文字列置換
re.sub(正規表現パターン, 置換後の文字列, 処理対象文字列)

まず、以下のテキストデータについて考えてみましょう。

101 CF001    コーヒー
102 CF002    コーヒー（お徳用）
201 TE01     紅茶
202 TE02-A   紅茶（お徳用A）
203 TE02-B   紅茶（お徳用B）

商品id、カタログコード、商品名の３つのフィールドからなるテキストデータがあるとします。
スペース区切りですが、スペースの数は一定ではありません。

この区切り文字をタブに置換してTSV形式に変換してみます。
１つ以上のスペースは' +'で表すことができますので、置換する場合は、以下のように記述します。
"""

import re

text = """101 CF001    コーヒー
102 CF002    コーヒー(お徳用)
201 TE01     紅茶
202 TE02-A   紅茶(お徳用A)
203 TE02-B   紅茶(お徳用B)"""
tsv_str = re.sub(' +', '\t', text)
print(tsv_str)

"""
可変長のスペース区切り文字列をタブ区切り文字列に変換することができました。


コンパイル済み正規表現オブジェクト

さきほど文字列の置換でre.sub関数を使用しましたが、別の方法があります。
"""

text = """101 CF001    コーヒー
102 CF002    コーヒー(お徳用)
201 TE01     紅茶
202 TE02-A   紅茶(お徳用A)
203 TE02-B   紅茶(お徳用B)"""
regex = re.compile(' +')
tsv_str = regex.sub('\t', text)
print(tsv_str)

"""
re.compileによりコンパイル済み正規表現オブジェクトと呼ばれるオブジェクトを生成することができ、
reモジュールの多くの関数と同様のメソッドを実行することができます。

繰り返し使用する場合はコンパイル済み正規表現オブジェクトを使用するほうがよいでしょう。


正規表現で区切られた文字列を分割する

splitを使用すると文字列を指定した正規表現で分割することができます。

分割
re.split(正規表現パターン, 処理対象文字列)

今度は先ほどの商品データを1フィールドずつ区切ってみましょう。
フィールドの区切りは空白文字と改行なので、\s+を使用します。
"""

text = """101 CF001    コーヒー
102 CF002    コーヒー(お徳用)
201 TE01     紅茶
202 TE02-A   紅茶(お徳用A)
203 TE02-B   紅茶(お徳用B)"""
fields = re.split('\s+', text)
print(fields)

"""
また、コンパイル済み正規表現オブジェクトを使用した場合、以下のようになります。
"""

text = """101 CF001    コーヒー
102 CF002    コーヒー(お徳用)
201 TE01     紅茶
202 TE02-A   紅茶(お徳用A)
203 TE02-B   紅茶(お徳用B)"""
regex = re.compile('\s+')
fields = regex.split(text)
print(fields)

"""
正規表現で検索する

テキストデータから特定の文字列を検索するためにreモジュールには
findall、search、matchという３つの検索機能があります。

findallによる検索

findallを使用すると、パターンにマッチするすべての文字列をリストで取得することができます。

検索
re.findall(検索正規表現, 処理対象文字列)

サンプルです。
先ほどのテキストデータからすべての「紅茶」を含む列だけ抽出する方法について考えてみましょう。
「紅茶」を含む文字列は".*紅茶.*"で表すことができます。
"""

text = """101 CF001    コーヒー
102 CF002    コーヒー(お徳用)
201 TE01     紅茶
202 TE02-A   紅茶(お徳用A)
203 TE02-B   紅茶(お徳用B)"""

tea = re.findall(".*紅茶.*", text)
print(tea)
# ['201 TE01    紅茶', '202 TE02-A    紅茶(お徳用A)', '203 TE02-B    紅茶(お徳用B)']

# コンパイル済み正規表現オブジェクトを使う場合
regex_tea = re.compile('.*紅茶.*')
tea = regex_tea.findall(text)
print(tea)

"""
「紅茶」を含む行が抽出出来ました。
IPythonなどのインタラクティブシェル上でgrepと同様の処理をしたい場合にも使うことができます。


searchによる検索

searchはfindallとは異なり、
パターンの最初の出現の開始位置と終了位置のインデックスを持った
matchオブジェクトと呼ばれるオブジェクトを返します。

検索
re.search(検索正規表現, 処理対象文字列)
"""

import re

text = "ABCDEFGHIJKLMNOPQRSTU"
m = re.search('D..G', text)
print(m.start(), m.end())    # 3 7

print(text[m.start():m.end()])    # DEFG

"""
とはいえ、インデックスを指定して文字列を取得するのは面倒ですので、
通常は取得したmatchオブジェクトのgroupメソッドを使用して一致文字列を取得します。
"""

text = "ABCDEFGHIJKLMNOPQRSTU"
m = re.search('D..G', text)
print(m.group())    # DEFG

"""
また、コンパイル済み正規表現オブジェクトを使用した場合、以下のようになります。
"""

# import re

text = "ABCDEFGHIJKLMNOPQRSTU"
regex = re.compile('D..G')
m = regex.search(text)
print(m.group())    # DEFG


"""
matchによる検索

matchは先頭から一致した場合にmatchオブジェクトを、そうでない場合はNoneを返します。

検索
re.match(検索正規表現, 処理対象文字列)
"""

# import re

text = "ABCDEFGHIJKLMNOPQRSTU"
m = re.match('.*D..G', text)
print(m.group())    # ABCDEFG

m = re.match('.*S..V', text)
print(m)    # None

"""
一致しない場合はNoneが返されることが確認できます。
ただし、先頭から一致しているひつようがあるため、searchと比較してあまり使用されていないように思えます。

コンパイル済み正規表現オブジェクトを使用した場合、以下のようになります。
"""

# import re

text = "ABCDEFGHIJKLMNOPQRSTU"
regex = re.compile('.*D..G')
m = regex.match(text)
print(m.group())    # ABCDEFG


"""
正規表現グループ

正規表現グループは、目的の一致オブジェクトをグルーピングして取得することができます。
データ分析やETLツールの実装でよく使う非常に便利な機能なので知っておくと役に立つかと思います。

サンプルとして先ほどの商品リストを１レコードずつ処理する場合について考えてみましょう。

商品idが数値、カタログコードがアルファベッド大文字と数字の組み合わせ、商品名が任意の文字列である場合、
それぞれのフィールドは以下のように表すことができるものとします。

    商品id:[0-9]+
    カタログコード:[0-9A-Z]+
    商品名:.*
    区切り文字:スペース+

これらの正規表現をグループで表すと、以下のように記述することができます。

([0-9]+) +([0-9A-Z]+) +(.*)

このグループをパターンとして指定すると、タプルとして取得することができます。サンプルで確認してみましょう。
"""

# import re

text = """101 CF001    コーヒー
102 CF002    コーヒー(お徳用)
201 TE01     紅茶
202 TE02-A   紅茶(お徳用A)
203 TE02-B   紅茶(お徳用B)"""

re.findall('([0-9]+) + ([0-9A-Z]+) + (.*)', text)
# [('101', 'CF002', 'コーヒー'),
#  ('102', 'Cf002', 'コーヒー(お徳用)'),
#  ('201', 'TE01', '紅茶')]
print(text)

"""
1レコードが1タプルで取得できたことが確認できます。
このように、１つのデータの塊を正規表現のグループとして表せる場合は
効率的な文字列解析を行うことができるようになります。


GreedyとLazy

正規表現の動作で注意したいのがGreedyとLazyです。

正規表現がGreedy（貪欲）とは、パターンにマッチする文字列を抽出した際、
マッチする最大範囲が抽出される状況を指します。Pythonの正規表現はデフォルトではGreedyに動作します。

文章だけだとわかりづらいため、具体的なサンプルを挙げてみます。
"""

# import re

html = "<h1>見出し</h1><p>ここはパラグラフです。</p>"
p = re.findall('<.*>', html)
print(p)    # ['<h1>見出し</h1><p>ここはパラグラフです。</p>']

"""
上の正規表現だと<から始まり、>で終わる文字列が指定されていますが、
結果としてテキストデータ全体がマッチされています。
もしHTMLのタグ、つまり<h1>、</h1>、<p>、</p>だけを抽出したい場合だと問題がありますね。

そんな時に便利なのがLazy（怠惰な）マッチングです。
?をパターンの最後につけると、「可能な限り少ない」マッチングを取得することができます。

再度サンプルでLazyなマッチングの動作を確認してみましょう。
"""

# import re

html = "<h1>見出し</h1><p>ここはパラグラフです。</p>"
p = re.findall('<.*?>', html)
print(p)    # ['<h1>', '</h1>', '<p>', '</p>']

"""
最短で一致したタグのみを取得することができました。
"""


print("--- Python入門　configparser 設定ファイルの読み込み---")


"""
iniファイル

一般的に、データベースの接続先や、保存先ファイルといった設定値はソースコードに直接書き込むのではなく
設定ファイルを使用します。Pythonでは、設定ファイルの読み込み用に、
configparserというini形式に対応したパーサーが用意されています。
ini形式とは以下のような大カッコで括った「セクション」と、その配下にあるキーと値の組からなる形式です。
セミコロンでコメントを入れることもできます。
Windowsのレジストリなどで使用している拡張形式には対応していないので注意してください。


; iniファイルの例
[DB]
host = localhost
port = 3306
user = kuro
pass = kuropass
; ここはコメント

[FILE]
; ここもコメント
output = /opt/output.txt
"""

"""
configparserの使用方法

それではconfigparserを使用してみましょう。以下の設定ファイルを読み込んでみます。

[SAMPLE1]
; 文字列
str_key = hogehoge
; 整数
int_key= 100

[SAMPLE2]
; 実数
float_key = 0.1
; 論理 yes/no on/off
bool_key = yes

基本的な使い方

configparserは、文字列以外に整数、実数、論理型の変数を扱うことが可能です。
論理型は、yes/no以外にon/offを記述することができます。まずは基本的な使い方です。
セクションとキーを指定して値を取得します。
"""

import configparser

# configファイルの読み込み
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

# 値を文字列で取得する
config['SAMPLE1']['str_key']

# configの方に応じた値を取得する
str_value = config.get('SAMPLE1', 'str_key')
int_value = config.getint('SAMPLE1', 'int_key')
float_value = config.getfloat('SAMPLE2', 'float_key')
bool_value = config.getboolean('SAMPLE2', 'bool_key')

"""
8行目では辞書のようにセクションとキーを指定しています。
この指定の仕方の場合、値は文字列型で取得されるため、必要に応じて型を変換する必要があります。
このため、11行目以降ではget〜メソッドを使用しています。この方法を使用すると、型変換をする必要がなくなります。


その他の使い方

おそらく実務上は上記の使い方だけで十分事足りると思いますが、別の使い方も見ていきましょう。
"""

# import configparser

# configファイルの読み込み
config = configparser.ConfigParser()
config.read('config.ini', encoding='utf-8')

# セクションを一覧で取得
print(config.sections())

# セクションの取得
sample1 = config['SAMPLE1']

# セクションにもgetメゾットが用意されている
int_key = sample1.getint('int_key')
print(int_key)

# 代替値の設定
int_key = sample1.getint('int_key2', '0')
print(int_key)

"""
8行目のようにsections()メソッドを指定すると、セクションを一覧で取得することができます。
また、11行目にキーにセクション名だけ指定すると、セクションのオブジェクトが取得でき、
14行目のようにget〜メソッドを使用することができます。
設定がない場合にデフォルト値を指定したい場合は18行目のように、第2引数を指定します。
"""
