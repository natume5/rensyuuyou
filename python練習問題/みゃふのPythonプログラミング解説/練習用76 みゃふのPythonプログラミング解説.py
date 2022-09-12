#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- 例外処理（try～except） ---")


"""
プログラムを実行するとエラーになってしまう場合がありますが、
そのプログラムがエラーを起こすことがあらかじめ想定されているのなら、
エラー時の処理を別に用意したい場合があります。
そのようなときに使うのが例外処理です。
ここでは「Pythonでどうやって例外処理するの？」といった方へ、Pythonでの例外処理を解説します。
"""

print("--- 例外処理の基本 ---")


"""
Pythonの例外処理は「try〜except」を使います。

 [構文]

try:
    エラーが発生しうる処理
except:
    エラーが発生した場合に実行する処理

tryブロックの中でエラーが発生した場合、exceptブロックへ移動します。
エラーが発生しなかった場合はexceptブロックはスルーされます。
では実際に使ってみましょう。
ここでは型変換がうまくいかなかった場合に発生する「ValueError」を補足してみましょう。
"""

def str_to_num(str):
	try:
		num = int(str)    # ここで例外発生
	except:
		num = None
	return num

print(str_to_num('5個'))    # None

"""
関数str_to_numは「引数の文字列を数値に変換する。
できなかった場合はNoneを返却する」プログラムです。
変数strには「5個」が入っているので、num = int(str)でエラーが発生しました。
exceptブロックに処理が移り、numにNoneを代入し、return numで返却。
最後にprintで関数の結果を出力しています。
今回は”5個”を引数にしましたが、これ以外にも”aaa”や”2019/12/25”
などの予想しない文字列が入ってくる可能性があります。
また、そもそも文字列が入って来ない場合も想定できます。
このように「予想外のデータが入ってきた場合、
プログラムへの影響を最小限にするために」例外処理を使う場合は多いです。
"""


print("--- finallyで例外発生の有無に関係なく処理を実行する ---")


"""
finallyは、例外が発生するかどうかにかかわらず、try 〜 exceptを抜ける前に実行するブロックです。

[構文]

try:
    エラーが発生しうる処理
except:
    エラーが発生した場合に実行する処理
finally:
    try 〜 exceptを抜ける前に実行する処理

では例を見てみましょう。ここではゼロ除算で発生する「ZeroDivisionError」を補足します。
"""

int1 = 5
int2 = 0
try:
	result = int1 / int2
	print(result)
except:
	print('エラーが発生しました')
finally:
	print('-処理終了-')

# エラーが発生しました
# -処理終了-

"""
tryの中で0除算が発生しています。exceptでエラーを補足し「エラーが発生しました」と出力しています。
最後にfinallyブロックに移動し、「-処理終了-」を出力しています。
finallyは、エラーの有無にかかわらず「必ず実行したい処理」を記述するために使われます。
"""


print("--- よく起こるエラーと対策方法 ---")


"""
try〜except〜finallyでエラーの処理が可能であることを解説してきましたが、
あくまで例外処理は「プログラム上回避できない例外が発生するパターンがある」
場合に限定することが望ましいです。
ここではPython開発中によく起こるエラーと、その対策方法を見ていきましょう。

SyntaxError

構文が間違っている場合に発生するエラーです。Syntaxは日本語で「構文」です。
print "hello" #これはPython2の書き方なのでNG

[出力結果（一部省略）]

SyntaxError: Missing parentheses in call to 'print'

構文エラーなので、Pythonの構文に合った記述をすることで回避できます。
なので例外処理は必要ありません。

ZeroDivisionError

ゼロで値を割ったときに発生するエラーです。いわゆるゼロ除算と呼ばれるモノです。

print (5 / 0)

[出力結果]

ZeroDivisionError: division by zero

ZeroDivisionErrorは計算結果を除算に使う場合は常に発生する可能性があります。
確実に0にならない場合を除き、除算する時はtry〜exceptで例外処理する必要があります。
"""

x = 3
y = -3
try:
	print(5 / (x + y))    # x + y = 0なのでゼロ除算
except:
	print(5 / 1)    # 5.0


"""
TypeError

演算や関数の引数に適切ではない型の変数がきた場合に発生するエラーです。
例えばprint()で文字列 + 数値の演算をした場合に起こります。

total = 20
print('りんごの数は' + total + '個です。')

[出力結果]

TypeError: must be str, not int

上記の場合はformat()を活用することで回避できます。 
"""

total = 20
print('りんごの数は{}個です。'.format(total))    # りんごの数は20個です。

"""
ValueError

主に型の変換がうまくできなかった場合に発生するエラーです。
特に文字列から他の型に変換しようとした場合が挙げられます。

str = "5個"
num = int(str)

[出力結果]

ValueError: invalid literal for int() with base 10: '5個'

Pythonでは文字列が数値かを判定してくれるisdecimal()メソッドが用意されているので、
単純な整数であればisdecimal()を使いましょう。
"""

str = '5個'
if str.isdecimal():
	num = int(str)
else:
	num = str    # 変換できない場合はそのまま
print(str)    # 5個

"""
しかし、文字列が小数を含んでいる場合は上記の方法では対応しきれません。
文字列がfloat型に変換できるかどうかは次のようにすることで判定できます。
"""

def is_float(str):
	try:
		float(str)
	except:
		return False
	return True

str = '-1.23'
if is_float(str):
	print('変換可能')
else:
	print('変換不可')

# 変換可能

"""
例外を捕捉した場合はfloat型に変換できないのでFalse、
例外にならない場合は変換できるのでTrueを返却するis_float()を定義しました。
float()は文字列をfloat型に変換する関数ですが、
変換できない場合はValueErrorになるので、それを利用しています。
"""

"""
IndexError

リストやタプルなどで存在しないインデックス番号の値を取得しようとした場合に発生するエラーです。
インデックス番号が0から始まるのに慣れていない初心者の方が陥りがちなエラーです。

list = [1, 2, 3]
print(list[3])

[出力結果]

IndexError: list index out of range

Pythonではfor..inでループ処理を行うのでそれでIndexErrorを起こすことはありません。
IndexErrorはケアレスミスで発生することが多いので、十分に注意することで回避できます。


NameError

初期化していない変数を使った場合に発生するエラーです。

foo = 'bar'
print(hoo) #タイポ ×hoo ◯foo

[出力結果]

NameError: name 'hoo' is not defined

NameErrorは間違った変数名を指定した場合に発生しやすい例外です。

こちらも十分に気を付けることが回避できます。


FileNotFoundError

開こうとしたファイルが見つからなかった場合に発生するエラーです。

open('./not_found.txt') #存在しないファイル

[出力結果]

FileNotFoundError: [Errno 2] No such file or directory: './not_found.txt'
FileNotFoundErrorは先にファイルが存在するかどうかを確認することで回避できます。
ファイルの存在チェックはOSライブラリのisfile()を使います。
"""

import os

path = './not_found.txt'

if os.path.isfile(path):
	open(path)
else:
	print('ファイル[' + path + ']は存在しません')

# ファイル[./not_found.txt]は存在しません

"""
ModuleNotFoundError

インポートしようとしたモジュールが見つからなかった場合に発生するエラーです。

import nampy #タイポ ×nampy ◯numpy

[出力結果]

ModuleNotFoundError: No module named 'nampy'

上記の場合は単にミスせず記述をすることで回避できます。
上記以外の場合だとpipでモジュールをインストールし忘れている可能性があるので、
次のコマンドでインストールされているかを確認すると良いです。

$ pip list


ImportError

モジュールが見つからない以外で、インポートで問題が起こったときに発生するエラーです。

例えばfrom...importで指定した名前をインポートできない場合に起こります。

from math import py #タイポ ×py ◯pi
print(py)

[出力結果]

ImportError: cannot import name 'py'

こちらも記述ミスをしなことで回避できます。


AttributeError

主にメソッド名が間違っている場合に発生するエラーです。
また「インポートしたモジュールと同じ名前のファイルが同じディレクトリに存在する場合」
にもこのエラーが発生する可能性が高まります。
これは同じディレクトリに存在するファイルが読み込まれてしまい、
本来読み込む予定だったモジュールが読み込まれなくなるために起こる現象です。

例えばnumpy.pyというファイルを、実行するpythonのファイルと同じ階層に配置して、
numpyをインポートしてみましょう。

import numpy as np #同じディレクトリに「numpy.py」を配置
ary = np.array([1, 2, 3])

[出力結果]

AttributeError: module 'numpy' has no attribute 'array'

モジュール ’numpy’ には ’array’ 属性（メソッド）はありません。というエラーが返ってきます。

実際のnumpyにはarray()は存在しますが、
同じディレクトリのnumpy.pyが読み込まれてしまっているためAttributeErrorが発生しました。

初見だと気付けず、何が悪いのか分からない...となりがちです。
インポートしたいモジュールと同じ名前のファイル名が存在しないように注意しましょう。
"""
