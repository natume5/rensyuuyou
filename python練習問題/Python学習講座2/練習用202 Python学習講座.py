#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 正規表現 ---")


"""
文字列入力の検証やテキストマイニングのような自然言語処理で
広く使用されている正規表現ですが、
Pythonには標準ライブラリのreモジュールで提供されています。
"""


print("--- Pythonの正規表現 ---")


"""
正規表現

正規表現はメタ文字と呼ばれる文字を利用して
文字列の検索パターンを表すことができます。
任意のテキストの中からこの検索パターンに合致する文字列を
抽出したり置換することができます。
例えば、テキストの改行のみの行にマッチさせたい場合、
'^\n$'と記述します。^は行頭、\nは改行を表します。
学習の前に、基本的な正規表現について簡単に俯瞰しておきましょう。
簡単な例を以下に示します。

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

reモジュールはPythonの標準ライブラリで、
以下のimport文で使用することができます。

import re

よくある正規表現ライブラリと同じく以下の機能が利用可能です。

    置換
    分割
    検索
"""


print("--- 正規表現で指定した文字列を置換する ---")


"""
それではreモジュールを使用してみましょう。
まずは、データクレンジング等のデータ分析の前処理でよく使用する
文字列置換からです。
sub関数を使用します。

文字列置換
re.sub(正規表現パターン, 置換後の文字列, 処理対象文字列)

まず、以下のテキストデータについて考えてみましょう。

101 CF001    コーヒー
102 CF002    コーヒー（お徳用）
201 TE01     紅茶
202 TE02-A   紅茶（お徳用A）
203 TE02-B   紅茶（お徳用B）

商品id、カタログコード、商品名の
３つのフィールドからなるテキストデータがあるとします。
スペース区切りですが、スペースの数は一定ではありません。

この区切り文字をタブに置換してTSV形式に変換してみます。
１つ以上のスペースは' +'で表すことができますので、置換する場合は、
以下のように記述します。
"""

import re

text = """101 CF001    コーヒー
102 CF002    コーヒー（お徳用）
201 TE01     紅茶
202 TE02-A   紅茶（お徳用A）
203 TE02-B   紅茶（お徳用B）"""
tsv_str = re.sub(' +', '\t', text)   
print(tsv_str)
# 101     CF001   コーヒー
# 102     CF002   コーヒー（お徳用）
# 201     TE01    紅茶
# 202     TE02-A  紅茶（お徳用A）
# 203     TE02-B  紅茶（お徳用B）

"""
可変長のスペース区切り文字列をタブ区切り文字列に変換することができました。
"""


print("--- コンパイル済み正規表現オブジェクト ---")


"""
さきほど文字列の置換でre.sub関数を使用しましたが、別の方法があります。
"""

regex = re.compile(' +')
tsv_str = regex.sub('\t', text)
print(tsv_str)
# 101     CF001   コーヒー
# 102     CF002   コーヒー（お徳用）
# 201     TE01    紅茶
# 202     TE02-A  紅茶（お徳用A）
# 203     TE02-B  紅茶（お徳用B）

"""
re.compileによりコンパイル済み正規表現オブジェクト
と呼ばれるオブジェクトを生成することができ、
reモジュールの多くの関数と同様のメソッドを実行することができます。
繰り返し使用する場合はコンパイル済み正規表現オブジェクトを
使用するほうがよいでしょう。
"""


print("--- 正規表現で区切られた文字列を分割する ---")


"""
splitを使用すると文字列を指定した正規表現で分割することができます。

分割
re.split(正規表現パターン, 処理対象文字列)

今度は先ほどの商品データを1フィールドずつ区切ってみましょう。
フィールドの区切りは空白文字と改行なので、\s+を使用します。
"""

import re

text = """101 CF001    コーヒー
102 CF002    コーヒー（お徳用）
201 TE01     紅茶
202 TE02-A   紅茶（お徳用A）
203 TE02-B   紅茶（お徳用B）"""
fields = re.split('\s+', text)   
print(fields)
# ['101', 'CF001', 'コーヒー', '102', 'CF002', 'コーヒー（お徳用）', '201', 'TE01', '紅茶', '202', 'TE02-A', '紅茶（お徳用A）', '203', 'TE02-B', '紅茶（お徳用B）']

"""
また、コンパイル済み正規表現オブジェクトを使用した場合、以下のようになります。
"""

import re

text = """101 CF001    コーヒー
102 CF002    コーヒー（お徳用）
201 TE01     紅茶
202 TE02-A   紅茶（お徳用A）
203 TE02-B   紅茶（お徳用B）"""
regex = re.compile('\s+')
fields = regex.split(text)   
print(fields)
# ['101', 'CF001', 'コーヒー', '102', 'CF002', 'コーヒー（お徳用）', '201', 'TE01', '紅茶', '202', 'TE02-A', '紅茶（お徳用A）', '203', 'TE02-B', '紅茶（お徳用B）']


print("--- 正規表現で検索する ---")


"""
テキストデータから特定の文字列を検索するためにreモジュールにはfindall、
search、matchという３つの検索機能があります。

findallによる検索

findallを使用すると、パターンにマッチするすべての文字列を
リストで取得することができます。

検索
re.findall(検索正規表現, 処理対象文字列)

サンプルです。先ほどのテキストデータからすべての「紅茶」を含む列だけ
抽出する方法について考えてみましょう。
「紅茶」を含む文字列は".*紅茶.*"で表すことができます。
"""

import re

text = """101 CF001    コーヒー
102 CF002    コーヒー（お徳用）
201 TE01     紅茶
202 TE02-A   紅茶（お徳用A）
203 TE02-B   紅茶（お徳用B）"""

tea = re.findall(".*紅茶.*", text)
print(tea)
# ['201 TE01     紅茶', '202 TE02-A   紅茶（お徳用A）', '203 TE02-B   紅茶（お徳用B）']

# コンパイル済み正規表現オブジェクトを使う場合
regex_tea = re.compile('.*紅茶.*')
tea = regex_tea.findall(text)
print(tea)
# ['201 TE01     紅茶', '202 TE02-A   紅茶（お徳用A）', '203 TE02-B   紅茶（お徳用B）']

"""
「紅茶」を含む行が抽出出来ました。
IPythonなどのインタラクティブシェル上で
grepと同様の処理をしたい場合にも使うことができます。


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

print(text[m.start(): m.end()])
# DEFG

"""
とはいえ、インデックスを指定して文字列を取得するのは面倒ですので、
通常は取得したmatchオブジェクトのgroupメソッドを使用して
一致文字列を取得します。
"""

print(m.group())    # DEFG

"""
また、コンパイル済み正規表現オブジェクトを使用した場合、以下のようになります。
"""

import re

text = "ABCDEFGHIJKLMNOPQRSTU"
regex = re.compile('D..G')
m = regex.search(text)
print(m.group())    # DEFG

"""
matchによる検索

matchは先頭から一致した場合にmatchオブジェクトを、
そうでない場合はNoneを返します。

検索
re.match(検索正規表現, 処理対象文字列)
"""

import re

text = "ABCDEFGHIJKLMNOPQRSTU"
m = re.match('.*D..G', text)
print(m.group())    # ABCDEFG

m = re.match('.*S..V', text)
print(m)    # None

"""
一致しない場合はNoneが返されることが確認できます。
ただし、先頭から一致しているひつようがあるため、
searchと比較してあまり使用されていないように思えます。
コンパイル済み正規表現オブジェクトを使用した場合、以下のようになります。
"""

import re

text = "ABCDEFGHIJKLMNOPQRSTU"
regex = re.compile('.*D..G')
m = regex.match(text)
print(m.group())    # ABCDEFG


print("--- 正規表現グループ ---")


"""
正規表現グループは、目的の一致オブジェクトをグルーピングして
取得することができます。
データ分析やETLツールの実装でよく使う
非常に便利な機能なので知っておくと役に立つかと思います。
サンプルとして先ほどの商品リストを
１レコードずつ処理する場合について考えてみましょう。
商品idが数値、カタログコードがアルファベッド大文字と数字の組み合わせ、
商品名が任意の文字列である場合、
それぞれのフィールドは以下のように表すことができるものとします。

    商品id:[0-9]+
    カタログコード:[0-9A-Z]+
    商品名:.*
    区切り文字:スペース+

これらの正規表現をグループで表すと、以下のように記述することができます。

([0-9]+) +([0-9A-Z]+) +(.*)

このグループをパターンとして指定すると、タプルとして取得することができます。
サンプルで確認してみましょう。
"""

import re

text = """101 CF001    コーヒー
102 CF002    コーヒー（お徳用）
201 TE01     紅茶
202 TE02-A   紅茶（お徳用A）
203 TE02-B   紅茶（お徳用B）"""

re.findall('([0-9]+) +([0-9A-Z]+) +(.*)', text)
print(text)
# 101 CF001    コーヒー
# 102 CF002    コーヒー（お徳用）
# 201 TE01     紅茶
# 202 TE02-A   紅茶（お徳用A）
# 203 TE02-B   紅茶（お徳用B）

"""
1レコードが1タプルで取得できたことが確認できます。
このように、１つのデータの塊を正規表現のグループとして表せる場合は
効率的な文字列解析を行うことができるようになります。
"""


print("--- GreedyとLazy ---")


"""
正規表現の動作で注意したいのがGreedyとLazyです。
正規表現がGreedy（貪欲）とは、パターンにマッチする文字列を抽出した際、
マッチする最大範囲が抽出される状況を指します。
Pythonの正規表現はデフォルトではGreedyに動作します。
文章だけだとわかりづらいため、具体的なサンプルを挙げてみます。
"""

import re

html = "<h1>見出し</h1><p>ここはパラグラフです。 </p>"
p = re.findall('<.*>', html)
print(p)    # ['<h1>見出し</h1><p>ここはパラグラフです。 </p>']

"""
上の正規表現だと<から始まり、>で終わる文字列が指定されていますが、
結果としてテキストデータ全体がマッチされています。
もしHTMLのタグ、つまり<h1>、</h1>、<p>、</p>
だけを抽出したい場合だと問題がありますね。
そんな時に便利なのがLazy（怠惰な）マッチングです。
?をパターンの最後につけると、「可能な限り少ない」
マッチングを取得することができます。
再度サンプルでLazyなマッチングの動作を確認してみましょう。
"""

import re

html = "<h1>見出し</h1><p>ここはパラグラフです。 </p>"
p = re.findall('<.*?>', html)
print(p)    # ['<h1>', '</h1>', '<p>', '</p>']

"""
最短で一致したタグのみを取得することができました。
"""



print("--- note.nkmk.meより ---")
print("--- Pythonの正規表現モジュールreの使い方（match, search, subなど） ---")


"""
Pythonで正規表現の処理を行うには標準ライブラリのreモジュールを使う。
正規表現パターンによる文字列の抽出や置換、分割などができる。

ここではまずreモジュールの関数やメソッドについて説明する。

    正規表現パターンをコンパイル: compile()
    マッチオブジェクト
    文字列の先頭がマッチするかチェック、抽出: match()
    先頭に限らずマッチするかチェック、抽出: search()
    文字列全体がマッチするかチェック: fullmatch()
    マッチする部分すべてをリストで取得: findall()
    マッチする部分すべてをイテレータで取得: finditer()
    マッチする部分を置換: sub(), subn()
    正規表現パターンで文字列を分割: split()

そのあとで、reモジュールで使える正規表現のメタ文字（特殊文字）
・特殊シーケンスについて説明する。
基本的には標準的な正規表現のシンタックスだが、
フラグの設定（特にre.ASCII）は要注意。

    Pythonでの正規表現のメタ文字・特殊シーケンスと注意点
    フラグの設定
        ASCII文字に限定: re.ASCII
        大文字小文字を区別しない: re.IGNORECASE
        各行の先頭・末尾にマッチ: re.MULTILINE
        複数のフラグを指定
    貪欲マッチと非貪欲マッチ
"""


print("--- 正規表現パターンをコンパイル: compile() ---")


"""
reモジュールで正規表現の処理を実行する方法は2つある。
関数で実行

1つ目は関数。
re.match(), re.sub()のように正規表現パターンを用いた抽出や
置換などの処理を行う関数が用意されている。
関数の詳細については後述するが、
いずれも第一引数に正規表現パターンの文字列を指定し、
その後に処理する文字列などを指定するようになっている。
"""

import re

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.match(r'([a-z]+)@([a-z]+)\.com', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(re.sub(r'([a-z]+)@([a-z]+)\.com', 'NEW_ADDRESS', s))
# NEW_ADDRESS bbb@yyy.net ccc@zzz.org

"""
ちなみに、この例の正規表現パターンの[a-z]はaからzまでのいずれかの文字
（＝アルファベットの小文字）、
+は直前のパターン（ここでは[a-z]）を1回以上繰り返す、という意味。
[a-z]+は小文字のアルファベットが1文字以上繰り返される文字列にマッチする。
.はメタ文字（特別な意味を持つ文字）なので\でエスケープする必要がある。
正規表現パターンの文字列はバックスラッシュ\を多用する場合が多いので、
例のようにraw文字列を使うと便利。


正規表現パターンオブジェクトのメソッドで実行

2つ目は正規表現パターンオブジェクトのメソッド。

re.compile()を使うと、
正規表現パターン文字列をコンパイルして
正規表現パターンオブジェクトを作成できる。
"""

p = re.compile(r'([a-z]+)@([a-z]+)\.com')

print(p)
# re.compile('([a-z]+)@([a-z]+)\\.com')

print(type(p))    # <class 're.Pattern'>

"""
re.match(), re.sub()などの関数と同様の処理が、
正規表現オブジェクトのメソッドmatch(), sub()として実行できる。
"""

print(p.match(s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(p.sub('NEW_ADDRESS', s))
# NEW_ADDRESS bbb@yyy.net ccc@zzz.org

"""
以降で説明するre.xxx()の関数はすべて
正規表現オブジェクトのメソッドとしても提供されている。
同じパターンを使う処理を繰り返し行う場合は、
re.compile()で正規表現オブジェクトを生成して使い回すほうが効率的。
以降のサンプルコードでは便宜上コンパイルせずに関数を使っているが、
同じパターンを繰り返し使う場合は、
前もってコンパイルして正規表現オブジェクトのメソッドとして
実行することをおすすめする。
"""


print("--- マッチオブジェクト ---")


"""
match()やsearch()などはマッチオブジェクトを返す。
"""

s = 'aaa@xxx.com'

m = re.match(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(type(m))    # <class 're.Match'>

"""
マッチした文字列や位置をマッチオブジェクトの以下のメソッドを使って取得できる。

    マッチした位置を取得: start(), end(), span()
    マッチした文字列を取得: group()
    各グループの文字列を取得: groups()
"""

print(m.start())    # 0

print(m.end())     # 11

print(m.span())    # (0, 11)

print(m.group())    # aaa@xxx.com

"""
正規表現パターンの文字列中の部分を括弧()で囲むと、
その部分がグループとして処理される。
このとき、groups()で各グループにマッチした部分の文字列が
タプルとして取得できる。
"""

s = 'aaa@xxx.com'
m = re.match(r'([a-z]+)@([a-z]+)\.([a-z]+)', s)

print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(m.groups())    # ('aaa', 'xxx', 'com')

"""
グルーピングした場合、
group()の引数に数値を指定すると任意のグループの文字列を取得できる。
省略または0を指定するとマッチ全体、
1以降の数値を指定すると順番に各グループの文字列が返される。
"""

print(m.group())    # aaa@xxx.com

print(m.group(0))    # aaa@xxx.com

print(m.group(1))    # aaa

print(m.group(2))    # xxx

print(m.group(3))    # com


print("--- 文字列の先頭がマッチするかチェック、抽出: match() ---")


"""
match()は文字列の先頭がパターンにマッチするとマッチオブジェクトを返す。
上述のように、マッチオブジェクトを使ってマッチした部分文字列を抽出したり、
単純にマッチしたかどうかをチェックしたりできる。
match()が調べるのはあくまでも先頭のみ。
先頭にマッチする文字列がない場合はNoneを返す。
"""

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.match(r'[a-z]+@[a-z]+\.com', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(re.match(r'[a-z]+@[a-z]+\.net', s))
# None


print("--- 先頭に限らずマッチするかチェック、抽出: search() ---")


"""
search()は文字列すべてが検索対象で、
先頭にない文字列にもマッチする。
match()と同じく、マッチする場合はマッチオブジェクトを返す。
マッチする部分が複数ある場合は、最初のマッチ部分のみが返される。
"""

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.search(r'[a-z]+@[a-z]+\.net', s))
# <re.Match object; span=(12, 23), match='bbb@yyy.net'>

print(re.search(r'[a-z]+@[a-z]+\.[a-z]+', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

"""
マッチする部分をすべて取得したい場合は
後述のfindall()またはfinditer()を使う
"""


print("--- 文字列全体がマッチするかチェック: fullmatch() ---")


"""
文字列全体が正規表現パターンにマッチしているかどうかの確認には
fullmatch()を使う。
文字列全体がマッチしているとマッチオブジェクトが返され、
マッチしていない部分がある
（一部しかマッチしていない、または、全くマッチしていない）
とNoneが返される。
"""

s = 'aaa@xxx.com'
print(re.fullmatch(r'[a-z]+@[a-z]+\.com', s))
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

s = '!!!aaa@xxx.com!!!'
print(re.fullmatch(r'[a-z]+@[a-z]+\.com', s))
# None


print("--- マッチする部分すべてをリストで取得: findall() ---")


"""
findall()はマッチするすべての部分文字列をリストにして返す。
リストの要素はマッチオブジェクトではなく文字列なので注意。
"""

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

result = re.findall(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(result)
# ['aaa@xxx.com', 'bbb@yyy.net', 'ccc@zzz.org']

"""
マッチした部分が何個あるかは、
リストの要素数を返す組み込み関数len()を使って確認できる。
"""

print(len(result))    # 3

"""
正規表現パターンで括弧()を使ってグルーピングすると、
各グループの文字列を要素とするタプル
（マッチオブジェクトのgroups()に相当）のリストが返される。
"""

print(re.findall(r'([a-z]+)@([a-z]+)\.([a-z]+)', s))
# [('aaa', 'xxx', 'com'), ('bbb', 'yyy', 'net'), ('ccc', 'zzz', 'org')]

"""
グループの括弧()は入れ子状に設定できるので、
マッチ全体も合わせて取得したい場合は全体を括弧()で囲めばよい。
"""

print(re.findall(r'(([a-z]+)@([a-z]+)\.([a-z]+))', s))
# [('aaa@xxx.com', 'aaa', 'xxx', 'com'), 
# ('bbb@yyy.net', 'bbb', 'yyy', 'net'), 
# ('ccc@zzz.org', 'ccc', 'zzz', 'org')]

"""
マッチしない場合は空のタプルを返す
"""

print(re.findall('[0-9]+', s))    # []


print("--- マッチする部分すべてをイテレータで取得: finditer() ---")


"""
finditer()はマッチするすべての部分をイテレータで返す。
その要素はマッチオブジェクトなので、マッチした部分の位置なども取得できる。
イテレータはそれ自体をprint()で出力しても中身は得られない。
組み込み関数next()やfor文を使うと中身が一つずつ取り出せる。
"""

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

result = re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)
print(result)
# <callable_iterator object at 0x0000020A1045F100>

print(type(result))    # <class 'callable_iterator'>

for m in result:
    print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>
# <re.Match object; span=(12, 23), match='bbb@yyy.net'>
# <re.Match object; span=(24, 35), match='ccc@zzz.org'>

"""
list()でリストに変換することも可能
"""

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'
l = list(re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s))
print(l)
# [<re.Match object; span=(0, 11), 
# match='aaa@xxx.com'>,
#  <re.Match object; span=(12, 23),
#  match='bbb@yyy.net'>,
#  <re.Match object; span=(24, 35),
#  match='ccc@zzz.org'>]

print(l[0])
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(type(l[0]))    # <class 're.Match'>

print(l[0].span())    # (0, 11)

"""
マッチするすべての部分の位置を取得したいといった場合は、
list()よりもリスト内包表記のほうが便利。
"""

print([m.span() for m in re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)])
# [(0, 11), (12, 23), (24, 35)]

"""
イテレータは順番に要素を取り出していく。
最後まで到達した後でさらに要素を取り出そうとすると
何も残っていない状態になるので注意。
"""

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

result = re.finditer(r'[a-z]+@[a-z]+\.[a-z]+', s)

for m in result:
    print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>
# <re.Match object; span=(12, 23), match='bbb@yyy.net'>
# <re.Match object; span=(24, 35), match='ccc@zzz.org'>

print(list(result))    # []


print("--- マッチする部分を置換: sub(), subn() ---")


"""
sub()を使うと、マッチした部分を他の文字列に置換できる。
第一引数に正規表現パターン、第二引数に置換後の文字列、
第三引数に処理対象の文字列を指定する。
置換処理された文字列が返される。
"""

s = 'aaa@xxx.com bbb@yyy.net ccc@zzz.org'

print(re.sub('[a-z]+@', 'ABC@', s))
# ABC@xxx.com ABC@yyy.net ABC@zzz.org

"""
第四引数countで最大置換回数（個数）を指定できる。
左側からcount個のみ置換される。
"""

print(re.sub('[a-z]+@', 'ABC@', s, 2))
# ABC@xxx.com ABC@yyy.net ccc@zzz.org

"""
括弧()でグルーピングした場合、
置換後の文字列の中でマッチした文字列を使用できる。
デフォルトでは\1, \2, \3...が、
それぞれ1つ目の()、2つ目の()、3つ目の()...
にマッチした部分に対応している。
raw文字列ではない通常の文字列だと
'\\1'のように\をエスケープする必要があるので注意。
"""

print(re.sub('([a-z]+)@([a-z]+)', '\\2@\\1', s))
# xxx@aaa.com yyy@bbb.net zzz@ccc.org

print(re.sub('([a-z]+)@([a-z]+)', r'\2@\1', s))
# xxx@aaa.com yyy@bbb.net zzz@ccc.org

"""
正規表現パターンの()の先頭に
?P<xxx>を記述してグループに名前をつけると、
\1のような番号ではなく\g<xxx>のように名前を使って指定できる。
"""

print(re.sub('(?P<local>[a-z]+)@(?P<SLD>[a-z]+)', r'\g<SLD>@\g<local>', s))
# xxx@aaa.com yyy@bbb.net zzz@ccc.org

"""
第二引数にはマッチオブジェクトを引数とする関数も指定できる。
より複雑な処理が可能になる。
"""

def func(matchobj):
    return matchobj.group(2).upper() + '@' + matchobj.group(1)

print(re.sub('([a-z]+)@([a-z]+)', func, s))
# XXX@aaa.com YYY@bbb.net ZZZ@ccc.org

"""
ラムダ式を使ってもよい。
"""

print(re.sub('([a-z]+)@([a-z]+)', lambda m: m.group(2).upper() + '@' + m.group(1), s))
# XXX@aaa.com YYY@bbb.net ZZZ@ccc.org

"""
subn()は置換処理された文字列（sub()の返り値と同じ）と
置換された部分の個数（パターンにマッチした個数）とのタプルを返す。
"""

t = re.subn('[a-z]*@', 'ABC@', s)

print(t)    # ('ABC@xxx.com ABC@yyy.net ABC@zzz.org', 3)

print(type(t))     # <class 'tuple'>

print(t[0])    # ABC@xxx.com ABC@yyy.net ABC@zzz.org

print(t[1])    # 3

"""
引数の指定方法などはsub()と同じ。
()でグルーピングした部分を使ったり、引数countを指定したりできる。
"""

print(re.subn('([a-z]+)@([a-z]+)', r'\2@\1', s, 2))
# ('xxx@aaa.com yyy@bbb.net ccc@zzz.org', 2)


print("--- 正規表現パターンで文字列を分割: split() ---")


"""
split()はパターンにマッチした部分で文字列を分割し、リストにして返す。
先頭・末尾にマッチする場合、
結果のリストの最初と最後に空文字列''が含まれるので注意。
"""

s = '111aaa222bbb333'

print(re.split('[a-z]+', s))
# ['111', '222', '333']

print(re.split('[0-9]+', s))
# ['', 'aaa', 'bbb', '']

"""
第三引数maxsplitで最大分割回数（個数）を指定できる。
左側から、指定した個数のみ分割される。
"""

print(re.split('[a-z]+', s, 1))
# ['111', '222bbb333']


print("--- Pythonでの正規表現のメタ文字・特殊シーケンスと注意点 ---")


"""
Python3のreモジュールで使える正規表現の
メタ文字（特殊文字）・特殊シーケンスの主なものは以下の通り。


メタ文字    内容
.         改行以外の任意の1文字（DOTALLフラグで改行も含む）
^         文字列の先頭（MULTILINEフラグで各行の先頭にもマッチ）
$         文字列の末尾（MULTILINEフラグで各行の末尾にもマッチ）
*         直前のパターンを0回以上繰り返し
+         直前のパターンを1回以上繰り返し
?         直前のパターンを0回または1回繰り返し
{m}       直前のパターンをm回繰り返し
{m, n}    直前のパターンをm〜n回繰り返し
[]        文字の集合 - []内のいずれか1文字にマッチ
|         OR（または） - A|BでAかBいずれかのパターンにマッチ

特殊シーケンス     内容
\d         Unicode10進数字（ASCIIフラグでASCIIの数字に限定）
\D         \dの反対（\d以外）
\s         Unicode空白文字（ASCIIフラグでASCIIの空白文字に限定）
\S         \sの反対（\s以外）
\w         Unicode単語文字と_（ASCIIフラグでASCIIの英字と_に限定）
\W         \wの反対（\w以外）
"""


print("--- フラグの設定 ---")


"""
上の表でも示した通り、
メタ文字・特殊シーケンスの中にはフラグによってモードが変わるものがある。
ここでは主なフラグのみを取り上げる。


ASCII文字に限定: re.ASCII

Python3の文字列に対しては、
\wはデフォルトで全角の日本語や英数字などにもマッチする。
標準的な正規表現とは異なり\wと[a-zA-Z0-9_]は等価ではない。
"""

print(re.match(r'\w+', 'あいう漢字ABC123'))
# <re.Match object; span=(0, 11), match='あいう漢字ABC123'>

print(re.match('[a-zA-Z0-9_]+', 'あいう漢字ABC123'))
# None

"""
各関数で引数flagsにre.ASCIIを指定するか、
正規表現パターンの文字列の先頭にインラインフラグ(?a)をつけると、
ASCII文字にのみマッチするようになる
（全角の日本語や英数字などにはマッチしない）。
この場合は\wは[a-zA-Z0-9_]と等価。
"""

print(re.match(r'\w+', 'あいう漢字ABC123', flags=re.ASCII))
# None

print(re.match(r'(?a)\w+', 'あいう漢字ABC123'))
# None

"""
re.compile()でコンパイルする場合も同様。
引数flagsかインラインフラグ(?a)を使う。
"""

p = re.compile(r'\w+', flags=re.ASCII)
print(p)    # re.compile('\\w+', re.ASCII)

print(p.match('あいう漢字ABC123'))    # None

p = re.compile(r'(?a)\w+')
print(p)    # re.compile('(?a)\\w+', re.ASCII)

print(p.match('あいう漢字ABC123'))     # None

"""
またre.ASCIIは短縮形re.Aとしても提供されている。どちらを使ってもよい。
"""

print(re.ASCII is re.A)    # True

"""
\wの反対を表す\Wもre.ASCIIや(?a)の影響を受ける。
"""

print(re.match(r'\W+', 'あいう漢字ABC123'))
# None

print(re.match(r'\W+', 'あいう漢字ABC123', flags=re.ASCII))
# <re.Match object; span=(0, 5), match='あいう漢字'>

"""
\wと同様に、数字にマッチする\d、空白にマッチする\sも、
デフォルトでは半角にも全角にもマッチする。
re.ASCIIや(?a)を指定すると半角のみに限定される。
"""

print(re.match(r'\d+', '123'))
# <re.Match object; span=(0, 3), match='123'>

print(re.match(r'\d+', '１２３'))
# <re.Match object; span=(0, 3), match='１２３'>

print(re.match(r'\d+', '123', flags=re.ASCII))
# <re.Match object; span=(0, 3), match='123'>

print(re.match(r'\d+', '１２３', flags=re.ASCII))
# None

print(re.match(r'\s+', '　'))
# <re.Match object; span=(0, 1), match='\u3000'>

print(re.match(r'\s+', '　', flags=re.ASCII))
# None

"""
それらの反対、\D, \Sもre.ASCIIや(?a)の影響を受ける。


大文字小文字を区別しない: re.IGNORECASE

デフォルトでは大文字小文字が区別される。
両方にマッチさせるには大文字と小文字の両方を
パターンに入れる必要がある。
re.IGNORECASE]を指定すると大文字小文字を区別せずにマッチする。
標準的な正規表現のiフラグに相当。
"""

print(re.match('[a-zA-Z]+', 'abcAbC'))
# <re.Match object; span=(0, 6), match='abcABC'>

print(re.match('[a-z]+', 'abcABC', flags=re.IGNORECASE))
# <re.Match object; span=(0, 6), match='abcABC'>

print(re.match('[A-Z]+', 'abcABC', flags=re.IGNORECASE))
# <re.Match object; span=(0, 6), match='abcABC'>

"""
インラインフラグ(?i)、または、短縮形のre.IでもOK。


各行の先頭・末尾にマッチ: re.MULTILINE

正規表現のメタ文字^は文字列の先頭にマッチする。
デフォルトでは文字列全体の先頭のみにマッチするが、
re.MULTILINEを指定すると各行の先頭にもマッチするようになる。
標準的な正規表現のmフラグに相当。
"""

s = """aaa-xxx
bbb-yyy
ccc-zzz"""

print(s)
# aaa-xxx
# bbb-yyy
# ccc-zzz

print(re.findall('^[a-z]+', s))
# ['aaa']

print(re.findall('^[a-z]+', s, flags=re.MULTILINE))
# ['aaa', 'bbb', 'ccc']

"""
末尾にマッチする$も同様。
デフォルトでは文字列全体の末尾のみにマッチ、
re.MULTILINEを指定すると各行の末尾にもマッチするようになる。
"""

print(re.findall('[a-z]+$', s))
# ['zzz']

print(re.findall('[a-z]+$', s, flags=re.MULTILINE))
# ['xxx', 'yyy', 'zzz']

"""
インラインフラグ(?m)、または、短縮形のre.MでもOK。


複数のフラグを指定

複数のフラグを同時に有効にしたい場合は|を使う。
インラインフラグの場合は(?am)のように各文字を続けて記述する。
"""

s = """aaa-xxx
あああ-んんん
bbb-zzz"""

print(s)
# 

print(re.findall(r'^\w+', s, flags=re.M))
# ['aaa', 'あああ', 'bbb']

print(re.findall(r'^\w+', s, flags=re.M | re.A))
# ['aaa', 'bbb']

print(re.findall(r'(?am)^\w+', s))
# ['aaa', 'bbb']


print("--- 貪欲マッチと非貪欲マッチ ---")


"""
これは正規表現の一般的な問題でPythonだけの問題ではないが、
ハマりがちなので書いておく。
デフォルトでは*, +, ?は貪欲（greedy）マッチで、
できる限り長い文字列にマッチする。
"""

s = 'aaa@xxx.com bbb@yyy.com'

m = re.match(r'.+com', s)
print(m)
# <re.Match object; span=(0, 23), match='aaa@xxx.com bbb@yyy.com'>

print(m.group())
# aaa@xxx.com bbb@yyy.com

"""
?を後ろにつける（*?, +?, ??）と、非貪欲（non-greedy）、
最小（minimal）のマッチとなり、できる限り短い文字列にマッチする。
"""

s = 'aaa@xxx.com bbb@yyy.com'

m = re.match(r'.+?com', s)
print(m)
# <re.Match object; span=(0, 11), match='aaa@xxx.com'>

print(m.group())
# aaa@xxx.com

"""
デフォルトの貪欲マッチだと
思わぬ文字列にマッチする場合があるので要注意。
"""



print("--- くまのブログより ---")
print("--- 【python】分かりやすく正規表現を解説！【初心者向け】 ---")


"""
今回はpythonの「正規表現」を解説していきます。
正規表現はpython初心者の方にとって難しいですよね。
私も最初、正規表現でかなり苦戦しました。
使う表現のみ限定して、分かりやすい説明が欲しかったり
例文多めに書いてもらえればもっと分かりやすいのに…と思っていました。
その頃を思い出して、正規表現について解説しました。
初心者の方が正規表現は
・どんなものか
・どう使えばいいか
をすぐ理解できるように解説しました。
"""


print("--- 正規表現とは？ ---")


"""
正規表現は一般的に複数の文字列を
より簡単に一つの形式で表現するための表現方法のことです。
と言われても分かりにくいです。
ちょっとした具体例を交えて説明します。
例えば、文字列から「abx」、「aby」、「abz」
の三つの単語を取り出したいとします。
冗長ですが、分かりやすい書き方は以下の形です。
"""

x = 'abxabyabz'

print(re.findall('abx|aby|abz', x))
# ['abx', 'aby', 'abz']

"""
それぞれ三つ「abx」「aby」「abz」と書いて取り出すよりも、
正規表現で「ab[x-z]」と書いた方が明らかに短くすっきりします。
"""

x = 'abxabyabz'

print(re.findall('ab[x-z]+', x))
# ['abx', 'aby', 'abz']

"""
このように複数の文字列（「abx」「aby」「abz」）
を短くすっきりさせるために、
一つの形式（「ab[x-y]」）で表現する方法が正規表現です。
次は数字を例として、より分かりやすく正規表現を説明します。
"""


print("--- 正規表現の具体例 ---")


"""
例えば以下のような文字列があったとします。

s = 'prince:1000yen'

この価格となる数字「1000」のみを抽出したい場合、
一番長ったらしいですが、分かりやすい書き方は
"""

s = 'price:1000yen'

print(re.search('[0123456789]+', s))
# <re.Match object; span=(7, 11), match='1000'>

"""
となります。
match=‘1000’で欲しい数字が出てきますが、これでは長い。
そのため、[0123456789]を短くした[0-9]という書き方があります。
"""

s = 'price:1000yen'

print(re.search('[0-9]+', s))
# <re.Match object; span=(7, 11), match='1000'>

"""
もっと短くすると[\d]という書き方になります。これは[0-9]と同じ意味です。
"""

print(re.search('[\d]+', s))
# <re.Match object; span=(7, 11), match='1000'>

"""
この[\d]は全角数字にも使えます。
"""

S = 'price:１０００yen'

print(re.search('[\d]+', S))
# <re.Match object; span=(6, 10), match='１０００'>

"""
[\d]だけで「0123456789０１２３４５６７８９」をカバーできます。
これも複数の文字列を一つの形式で表す正規表現です。
では、ここから[\d]のような正規表現の特殊シーケンスの一覧を紹介します。
"""


print("--- 正規表現の特殊シーケンス ---")


"""
表現      同じ意味                     意味
\d        [0-9]            任意の数字(全半角)
\D        [^0-9]           任意の数字以外
\w        [a-zA-Z0-9_]     任意の英文字(全半角)と
                           数字(全半角)とアンダースコア
\W        [^a-zA-Z0-9_]    任意の英文字と数字と
                           アンダースコア以外

以上が一般的な特殊シーケンスの一覧です。
ここから一つずつ例文を紹介します。
一度に多くに該当が取れるようにfindall関数を使用した例文になります。

    \d と \D (数字と数字以外)
"""

s = 'tel:012-3456-7890'

print(re.findall('[\d]+', s))
# ['012', '3456', '7890']

print(re.findall('[\D]+', s))
# ['tel:', '-', '-']

"""
\w と \W (英文字、数字、アンダースコアと
英文字、数字、アンダースコア以外)
"""

s = 'Name:YAMADA_ＴＡＲＯ Mail:test@mail.com Tel:012-3456-7890'

print(re.findall('[\w]+', s))
# ['Name', 'YAMADA_ＴＡＲＯ', 'Mail', 'test', 'mail', 'com', 'Tel', '012', '3456', '7890']

print(re.findall('[\W]+', s))
# [':', ' ', ':', '@', '.', ' ', ':', '-', '-']

"""
正規表現の特殊シーケンスの例外（英字のみと日本語対応）

ここから少し例外を紹介します。
上記の特殊シーケンスでは取りにくい英文字のみや
日本語対応を下記にまとめてみました。

表現         意味
[a-z]     任意の半角英小文字
[A-Z]     任意の半角英大文字
[ぁ-ゟ]    任意のひらがな
[ァ-ヿ]    任意のカタカナ
[一-龥]   任意の漢字
"""

s = 'Python, ひらカナ, 正規表現'

# 英小文字
print(re.findall('[a-z]+', s))
# ['ython']

# 英大文字
print(re.findall('[A-Z]+', s))
# ['P']

# ひらがな
print(re.findall('[ぁ-ゟ]', s))    # ゟ→「より」と読む？
# ['ひ', 'ら']

# カタカナ
print(re.findall('[ァ-ヿ]', s))    # ヿ→「より」と読む？
# ['カ', 'ナ']

# 漢字
print(re.findall('[一-龥]', s))    # 龥→「ュ」と読む？
# ['正', '規', '表', '現']

"""
エスケープシーケンス

エスケープシーケンスとは、バックスラッシュ「 \ 」
で始まる通常の文字列で表せない特殊な文字や
機能を特定の形式で表したものです。
つまりは、空白や改行コードなどです。
このエスケープシーケンスも正規表現の一部になります。
また、次のraw文字列でもエスケープシーケンスは出てきます。
そのエスケープシーケンスの一部を一覧で並べます。

表現          意味
\s          空白文字(半角スペースや\n\t\r\f)
\S          空白文字以外
\t          タブ文字
\n          改行文字
\r          リターン
\f          改ページ
\\          バックスラッシュ
"""


print("--- 正規表現のメタ文字 ---")


"""
今までは数字、英文字など特定の種類の正規表現を説明していきました。
次は、より便利な使い方ができる「メタ文字」です。
メタ文字とは、正規表現では本来の文字の意味とは
異なる意味を持つ文字です。
そのメタ文字の一覧を並べます。

表現      意味              使用例      該当例
.      任意の文字
    (英数字ひらカナ漢字)        a.c        aac, abc, a1c
                                        aあc など
*   前の文字を0回以上繰り返す   a.*c       ac, abc, abccc, a123c, aあ〜いc など
                                       「.*」で任意の文字を0回以上繰り返し
+   前の文字を1回以上繰り返す   a(\d)+c    a1c, a123cはOK acやabcはNG
                                       「\d」は0-9で1回以上繰り返し
?   前の文字を0回か1回表示    ac?         a, acのみOK
                                       「https?」はhttp, httpsとなる
{ m }   前の文字をm回繰り返す a{2}c        aacのみOK
                                        ac, aaac, accはNG
{ m,n } 前の文字をm~n回繰り返す   ab{2,4}c    abbc, abbbc, abbbbcのみ
[ ] [ ]内の任意の1文字を示す  [0-9]       1, 3, 8, 9などはOK
                                       12や100など複数はNG
( ) ( )内をまとまりとする    (123)*         123, 123123など
^   文字列の先頭を示す   ^a(\w)*          a, abc, a12_などはOK
                                        b12はNG
$   文字列の末尾を示す   (\d)*x$          123x, 0xなど
"""


print("--- 正規表現とraw文字列 ---")


"""
特定文字を抽出したい文字列を囲む
シングルクオテーションかダブルクオテーションの前に、
「r」か「R」をつけるとエスケープシーケンスが無効化されます。
無効化というと分かりにくいですが、簡単に言えば、
バックスラッシュもそのまま表示されます。
raw文字列はこんな感じの文字列です。
"""

s = r'I\'m a man.'

"""
エスケープシーケンスは上記の

\t （タブ文字）、\n （改行文字）、\r （リターン）、
\f （改ページ）

だけではなく、

\’ （シングルクオテーション(‘)）、\” （ダブルクオテーション(”)）

なども含まれます。
つまり、文字列の中に「’(シングルクオテーション)」を入れたい場合は
"""

print('I\'m a man')    # I'm a man

"""
となります。これがエスケープシーケンスの一例です。
しかし、Raw文字列でrをつけるとエスケープシーケンスが無効化されるため
"""

print(r'I\'m a man')    # I\'m a man

"""
となります。え、文がおかしくなってダメじゃん。
と思いますが、本来はこういう時に使います。
"""

print(r'C:\\User\Python\test')
# C:\\User\Python\test

"""
これなら問題ないです。
では、「\d」や「\w」など特殊シーケンスではどうなるか？
これは簡単で、エスケープシーケンスではないため、
Raw文字列をやっても効果がないです。
"""


print("--- pythonのreモジュール ---")


"""
正規表現をよく使用する「re」モジュールの一部を紹介していきます。
分かりやすいように機能別です。「置換」「抽出」「分割」の3つです。


置換

reモジュールの中で置換する関数は「sub」です。
どのように使うかというと
"""

import re

re.sub('置換したい部分の正規表現', '置換後の文字', '文字列')

s = '0123-456-789'
print(re.sub('(\d)', 'x', s))
# xxxx-xxx-xxx

"""
抽出

文字列の先頭パターンが一致した場合に抽出する「match」
"""

import re

re.match('正規表現', '文字列')

s = '100-1010'
print(re.match('(\d){3}', s))
# <re.Match object; span=(0, 3), match='100'>

t = 'postcode100-1010'
print(re.match('(\d){3}', t))
# None

"""
文字列の先頭パターンに限らず一致した最初の部分を抽出する「search」
"""

import re

re.search('正規表現', '文字列')

s = "100-1010"
print(re.search("(\d){3}", s))
# <re.Match object; span=(0, 3), match='100'>

t = 'postcode100-1010'
print(re.search('(\d){3}', t))
# <re.Match object; span=(8, 11), match='100'>

"""
文字列の一致した部分を全てリスト化して抽出する「findall」
"""

import re

re.findall('正規表現', '文字列')

s = "100-1010"
print(re.findall('\d*', s))
# ['100', '', '1010', '']

"""
分割

正規表現で一致した部分で分割を行う「split」
"""

import re

re.split('正規表現', '文字列')

s = '0123-456-789'
print(re.split('\W', s))
# ['0123', '456', '789']


print("--- 最後に ---")


"""
今までpythonの正規表現とreモジュールを紹介していきました。
「習うより慣れろ」という言葉がある通り、
実際に使って覚えて自分のものにしていってください。
"""
