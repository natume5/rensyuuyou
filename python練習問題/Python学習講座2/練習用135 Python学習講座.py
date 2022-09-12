#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- コマンドライン引数 ---")


"""
学習をすすめる上で、実行時に適当な値を設定して確認したくなる場合が出てくるかもしれません。
方法の1つとしてコマンドラインで指定した引数を取得するという方法が挙げられます。
本稿にはモジュールや関数、if文等、未解説の用語が登場しますが、
まずはコマンドライン引数を使用する場合にはこういう書き方をするのだ、
という程度に理解し、必要に応じて復習してください。
"""


print("--- Pythonのコマンドライン引数 ---")


"""
コマンドライン引数の取得

Pythonスクリプトを実行する際にコマンドライン引数を指定する場合、
標準ライブラリであるsysモジュールのargvを利用します。
argvはスクリプトに渡されたコマンドライン引数が格納されたリストとなります。
0番目はスクリプトのファイル名が設定され、1番目以降にコマンドライン引数が設定されます。
また、入力値は文字列型として扱われます。
では、サンプルで動作を確認してみましょう。


サンプルコード args.py

import sys 
args = sys.argv
print(args)

args.pyという名前で保存して、引数なし、引数ありでそれぞれ動作を確認してみます。

実行結果

# 引数なし
$ python args.py
['args.py']

# 引数:hoge
$ python args.py hoge
['args.py', 'hoge']

# 引数: hoge foo
$ python args.py hoge foo
['args.py', 'hoge', 'foo']

0番目にスクリプト名、それ以降にコマンドライン引数がセットされたリストであることが解ると思います。

このため、以下のように大カッコで番号を指定すると値を取得することが可能です。


sample.py

from sys import argv

print(argv[0]) # スクリプトファイル名 
print(argv[1]) # 1番目の引数
print(argv[2]) # 2番目の引数

実行結果

python sample.py hoge fuga
sample.py
hoge
fuga


コマンドライン引数の数をチェックする

上のプログラムでは、引数が不足しているとlist index out of range
というエラーが発生します。
こういったエラーを回避するために処理前に引数をチェックするような処理を入れるには、
以下のように、len関数で引数の数をチェック(※1, ※2)します。
また、前述の通り、文字列として扱われますので、適宜数値チェック等を入れましょう。
"""

import sys


def main(cod3, name):
	print('main処理を実行します')
	# 以下省略

if __name__ == '__main__':
	args = sys.argv

	if len(args) == 3:
		code = args[1]
		name = args[2]
		main(code, name)
	else:
		print('以下形式でcodeとnameを指定してください')
		print('$ sample.py <code> <name>')
		quit()

"""
上のコードでは引数に過不足があると、main処理は実行されず、
コードのパラメータ指定方法が出力されます。

※1 len関数は後のページで解説するリストなどの
シーケンシャルな型の要素数を取得することができる、
Pythonに予め組み込まれている組み込み関数の1つです。

※2 ifとは制御文の一種で、条件ごとに処理を振り分けることが可能となります。
"""


print("--- 補足 argparse ---")


"""
簡単な引数を使用する場合はこのページで紹介したargvで十分ですが、
ある程度機能が増え任意オプションなどが必要となる場合は
argparseを使用することをおすすめします。
"""


print("--- Qiitaより ---")
print("--- Pythonでコマンドライン引数を受け取る ---")


"""
コマンドライン引数受け取ってそれを処理する問題が出たときに、
そういえば、Pythonでコマンドライン引数受け取るのやったことなくて、
やらかしたので、メモ。(問題の根幹部分ではなかったから助かったが。)


コマンドライン引数を受け取る

sysモジュールのargvを使用する。コマンドライン引数のリストが取得できる。
commandline_args.py

import sys

args = sys.argv

print(args[0])
print(args[1])
print(args[2])

$ python commandline_args.py a b

で実行すると、
出力は、

commandline_args.py
a
b

となる。
上記からわかるように、
リストの1つ目(args[0])は、実行ファイル名になる。
"""


print("--- 実際の使用時 ---")


"""
実際使用する際は、おそらく、いくつの引数を受け取ったかを確認し、
さらに、期待する形の入力かをチェックする必要がありそう。
fizzBuzz.py

import sys


def fizzBuzz(n):
    if n <= 0:
        return ()
    else:
        fizzBuzz(n-1)
        if n % 3 == 0 and n % 5 == 0:
            print(n, ' : ', 'FizzBuzz')
        elif n % 3 == 0:
            print(n, ' : ', 'Fizz')
        elif n % 5 == 0:
            print(n, ' : ', 'Buzz')
        else:
            print(n, ' : ', n)
        return ()


if __name__ == '__main__':
    args = sys.argv
    if 2 <= len(args):
        if args[1].isdigit():
            fizzBuzz(int(args[1]))
        else:
            print('Argument is not digit')
    else:
        print('Arguments are too short')


    引数無し

引数無しエラー

$ python fizzBuzz.py
Arguments are too short



    引数が数値じゃない

引数タイプエラー

$ python fizzBuzz.py a
Argument is not digit



    引数が数値

正常実行

python fizzBuzz.py 15
1  :  1
2  :  2
3  :  Fizz
4  :  4
5  :  Buzz
6  :  Fizz
7  :  7
8  :  8
9  :  Fizz
10  :  Buzz
11  :  11
12  :  Fizz
13  :  13
14  :  14
15  :  FizzBuzz



    引数が数値で、複数存在

最初の1つを使用し実行

python fizzBuzz.py 3 5 15
1  :  1
2  :  2
3  :  Fizz
"""


print("--- Hbk projectより ---")
print("--- 【Python】 コマンドライン引数の使い方（sys.argv） ---")


"""
コマンドライン引数はターミナルコマンドライン上からプログラムを実行する際に設定する引数で、
リストsys.argvに格納されます。
コマンドライン引数を設定するにはいくつか方法がありますが、
ここでは一番簡単なsys.argvを直接読み込んで使う方法についてまとめます。
"""


print("--- コマンドライン引数とは ---")


"""
Pythonスクリプトをコマンドライン上で実行する場合、例えば以下のように入力します。

$ python3 sample.py 'hello'

スクリプト名(sample.py)の後に記述される引数(‘hello’)がコマンドライン引数です。
公式ドキュメントから書式を引用すると、以下のようになります。

python [-bBdEhiIOqsSuvVWx?] [-c command | -m module-name | script | - ] [args]  

一番最後の引数argsに記述されるsys.argvに引き渡されます。
（その他の引数については公式ドキュメント参照）
リストsys.argvの構成は以下です。

argv[0]     スクリプト名（上記例でいうと、”sample.py”）
argv[1:]    コマンドライン引数（上記例でいうと、”hello”）

コマンドライン引数は、sys.argv[1:]に格納されるという点に注意です。
ちなみに第一引数の[-bBdEhiIOqsSuvVWx?]は、オプションを示しています。
詳細は公式リファレンスを参照ください。
"""


print("--- 使い方 ---")


"""
具体的な手順

コマンドライン引数をプログラム中で取得する手順を具体的に見ていきます。

    sysモジュールをインポートし、
    sys.argvに格納されている文字列を取得する
        sys.argv[0]：　 スクリプト名
        sys.argv[1:] ：　コマンドライン引数

コードで表すと下記のようになります。


# ---------------
#  argv.py
# ---------------
import sys

# コマンドライン引数を変数argsに代入
args = sys.argv

print(args)

スクリプトをコマンドライン上で実行した結果を以下に示します。
sys.argv[0]にスクリプト名、sys.argv[1:]
にコマンドライン引数が格納されていることがわかります。

$ python3 argv.py hello good
['argv.py', 'hello', 'good']


コマンドライン引数の型に気をつけよう

尚、sys.argvに格納される値は文字列です。
例えば以下のようなコードを試してみます。

#---------------
#  argv.py
#---------------
import sys

# コマンドライン引数をそれぞれ変数x, yに格納
x = sys.argv[1]
y = sys.argv[2]

# コマンドライン引数x, yの和を出力したい
print(x+y)

コマンドライン上で実行した結果を以下に示します。
コマンドライン引数として設定した”1″, “2”は文字列として格納されるので、
結果は文字列の結合というかたちで出力されています。


$ python argv.py 1 2
12

数値として扱えるように、int型に変換してみます。（下記★部）

#---------------
#  argv.py
#---------------
import sys
x = int(sys.argv[1])　★
y = int(sys.argv[2])　★

print(x+y)

スクリプトを実行した結果を以下です。期待取りの結果が得られました。

$ python argv02.py 1 2
3


もう少し実践的な例

これだけだとあまりに味気ないので、
（sys.argvの長さ）< 2の場合
（＝sys.argv[0]のみの場合、即ち、コマンドライン引数が無い場合）
はエラーメッセージを出すようにしました。
また、最後に確認のためsys.argvの中身を表示するようにしました。

#---------------
# sample1.py
#---------------

import sys

# sys.argvの長さが2より小さい = コマンドライン引数無し
if len(sys.argv) < 2:
    print("No argument!")
    sys.exit()
print("Argument:{}".format(sys.argv[1]))

# sys.argvの内容を確認
print("sys.argv = {}".format(sys.argv))

このスクリプトを実行した結果は以下です。

$ python3 sample.py one two three
Argument:one
sys.argv = ['sample.py', 'one', 'two', 'three']

コマンドライン引数を省略した場合はエラーメッセージが表示されます。

$ python3 sample.py
No argument!
"""


print("--- まとめ ---")


"""
今回は、Pythonでコマンドライン引数を使う方法のうち、
最も簡単なsys.argvを直接取り込む使った方法についてまとめました。
この他、高度な設定が可能なPython標準ライブラリのargparseモジュールを使う方法や
3rdParty製モジュールのclickなどを使う方法もあります。
"""
