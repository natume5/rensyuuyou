#!/usr/bin/python
# -*- coding: UTF-8 -*-



print("--- Python学習講座---")
print("--- Python入門　Pythonの実行方法---")


"""
Hello World

環境構築が終わったら、さっそくプログラムを書いて実行してみましょう。

Pythonはテキストファイルでスクリプトを記述し、実行する方法とは別に、対話モードというものがあります。


スクリプトを実行する

では、まずはスクリプトを作成して実行してみましょう。メモ帳やvimなどお好きなエディタを使用して、
hello_python.pyというテキストファイルに以下の内容を書き込んで保存してください。
pythonスクリプトの拡張子は.pyとなります。
"""

print('Hello Python World')

"""
その後、以下の通りコマンドラインで入力してみましょう。
Windowsの方はコマンドプロンプトを、LinuxやMacをお使いの方はターミナルを起動し、
スクリプトを書いたフォルダに移動して以下のコマンドを実行してください。
（今後、プロンプトの記号は$で表現します。）
"""

"""
いかがでしょうか？Hello Python Worldという文字列が出力されましたでしょうか？
printという関数で文字列を標準出力することができます。

C言語やJavaとは異なり、コンパイルをせずに実行することが可能です。
対話モードで実行する

今度は対話モードを使って実行してみましょう。今度はコマンドライン上でpythonと入力してみます。

$ python
Python 3.5.1 (default, Apr 24 2016, 23:33:22) 
[GCC 5.3.1 20160413] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 

上記のように、">>>"で開始されるプロンプトが起動すると思います。

ここで、続けてprint関数を入力してエンターキーを押下すると、指定した文字列が出力されると思います。

>>> print('Hello Python World')
Hello Python World

Pythonはスクリプトを作成せずにプログラムを実行することが可能なのです。
"""


"""
コード補完

対話モードの便利な点として、コード補完の機能が挙げられます。
試しに、priまで入力してTabキーを押下してみてください。"print("まで補完されたかと思います。

組込み関数以外に、自分で定義した識別子も補完されるため非常に便利です。
対話モードの終了

対話モードを終了する場合ですが、以下のようにquit()で終了することができます。

>>> quit()
$

さて、簡単に実行する場合は便利な対話形式ですが、
当サイトでは読者がコピペしやすいようにスクリプトの形式を採用しています。
（対話形式だと>>> が頭につくため。）ほとんどサンプルは対話形式でも実行可能です。
"""


"""
Pythonの基本

では、次にスクリプトでもう少し長いプログラムを作成してPythonの特徴を確認していきましょう。
"""

def main():
	"""
	ダブルクォート3つでdocstringとなります
	ここにmain関数の説明を記述します。
	"""

	# 通常のコメントは#を使います。
	# 通常の文と同様にインデントを合わせる必要があります。
	print("hello world!")

	# passは、何もしない分です
	pass


if __name__ == "__main__":
	main()    # もちろん、文の後に書くことが出来ます。


"""
一つづつ見ていきましょう。


インデント

Pythonの特徴の一つにインデントが挙げられます。

処理のブロックごとにインデントをつけていきます。

C、C++、Java、C#、PHP、e.t.c.通常、
プログラムのクラス、関数、制御文のまとまりのブロックは中括弧でくくるのが一般的ですが、
Pythonではインデントでブロックを表します。

インデントにはタブ、スペースのどちらを利用しても実行することができますが、
PEP8という規約上ではスペース4文字が推奨されています。

インデントを間違えると、誤った処理が実行されたり、実行そのものが失敗するので注意してください。


コメントとドックストリング

Pythonのコメントは#を使用します。 #以降の文字列は処理されません。
ただし、他の文と同様、インデントを合わせる必要があるので注意が必要です。

もちろん、16行目のように文の後にコメントを打つことも可能です。

また、ダブルクォート3つでドックストリングというクラスや関数の仕様を記述するためのコメントがあります。
if __name__ == "__main__":

後々詳しく説明しますが、現時点では起動するスクリプトはこういう書き方をするものだ、
ただのお作法の一つなんだ、と思ってください。
"""


print("--- Python入門　print関数---")


"""
print関数の基本

Pythonには予め用意されいる関数があり、組み込み関数と呼ばれています。
print関数は組み込み関数の1つで、引数に指定した変数や値の文字列表現を標準出力に出力します。
print関数
print(値1 , 値2 , ・・・, end="終端文字")

別ページで詳しく説明しますが、Pythonの文字列はダブルクォートかシングルクォートで囲みます。
例えば、文字列「Sample」を出力したい場合、以下のようなコードになります。
"""

print("Sample")

"""
また、カンマ区切りで値を指定するとスペース区切りで列挙されます。いくつか追加で例を見てみましょう。
"""

print('サンプル文字列')    # 'サンプル文字列'が出力される

x = "text"
print(x)    # 'text'が出力される

y = 100
print(y)    # 100が出力される

print(x, y)    # text 100が出力される


"""
print関数で改行させたくない場合

print関数の引数でend引数を指定すると、出力する文字列の終端を指定することができます。
print関数では改行が自動的に行われますが、改行させたくない場合は以下のようにend引数に空白文字、
つまり""や''を指定します。
"""

print("aaa", end='')
print("bbb")    # aaabbb


"""
無論、他の文字列を指定することもできます。
以下のコードでは、aaa,bbb,cccを★で結合して、最後に改行しています。
"""

print("aaa", end='★')
print("bbb", end='★')
print("ccc")    # aaa★bbb★ccc


"""
文字列結合とstr関数

いくつかの変数を続けて表示せたい場合、+記号で文字列を結合することができます。
"""

x1 = 'text'
x2 = 'moziretsu'
print(x1 + '' + x2)    # text moziretsuが出力される


"""
ただし、文字列以外を結合する場合は注意が必要です。
数値と文字列を+で結合する方法が定義されていないため、以下のコードはエラーとなります。

x = 'text'
y = 100
print(x + y) 
# TypeError: Can't convert 'int' object to str implicitly

この場合、一旦数値に対し組み込み関数のstrで文字列変換することにより、結合することが可能となります。
少し正確性を犠牲にしますが、当面はstr関数は任意の変数を文字列化する関数だと考えてください。
"""

x = 'text'
y = 100
print(x + str(y))    # text100が出力される


"""
printで色をつける

ANSIエスケープシーケンスを使用するとprintで色を付けることも可能です。詳しくは以下を参照してください。
"""


print("--- コマンドライン引数---")
"""
Pythonのコマンドライン引数
コマンドライン引数の取得

Pythonスクリプトを実行する際にコマンドライン引数を指定する場合、
標準ライブラリであるsysモジュールのargvを利用します。
argvはスクリプトに渡されたコマンドライン引数が格納されたリストとなります。

0番目はスクリプトのファイル名が設定され、1番目以降にコマンドライン引数が設定されます。
また、入力値は文字列型として扱われます。

では、サンプルで動作を確認してみましょう。

サンプルコード args.py
"""
# import sys
# args = sys.argv
# print(args)

"""
args.pyという名前で保存して、引数なし、引数ありでそれぞれ動作を確認してみます。
実行結果

# 引数なし
# $ python args.py
# ['args.py']

# 引数:hoge
# $ python args.py hoge
# ['args.py', 'hoge']

# 引数: hoge foo
# $ python args.py hoge foo
# ['args.py', 'hoge', 'foo']
"""

"""
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
"""

"""
コマンドライン引数の数をチェックする

上のプログラムでは、引数が不足しているとlist index out of rangeというエラーが発生します。
こういったエラーを回避するために処理前に引数をチェックするような処理を入れるには、以下のように、
len関数で引数の数をチェック(※1, ※2)します。
また、前述の通り、文字列として扱われますので、適宜数値チェック等を入れましょう。
サンプルコード

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

上のコードでは引数に過不足があると、main処理は実行されず、コードのパラメータ指定方法が出力されます。

※1 len関数は後のページで解説するリストなどのシーケンシャルな型の要素数を取得することができる、
Pythonに予め組み込まれている組み込み関数の1つです。
"""






