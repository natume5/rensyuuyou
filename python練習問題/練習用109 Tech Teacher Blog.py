#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Tech Teacher Blog ---")
print("--- ファイル操作をマスターしよう！Pythonでの読み込み・書き込み方法を徹底解説！ ---")


"""
Pythonを学び始めて、Pythonでテキストファイルを扱いたいと思い始めた人も少なくないでしょう。
そこで今回はPythonでテキストファイルを操作する方法について詳しく説明していきます。
それでは見ていきましょう。
"""


print("--- テキストファイルを読み込む ---")


"""
テキストファイルを読み込むためにはopen関数を使用してファイルをオープンし、
その後にファイルの内容を読み込む必要があります。
テキストファイルの内容を読み込むメソッドには
「readメソッド」「readlineメソッド」「readlinesメソッド」の3つがあります。
ここからはopen関数と、そこからテキストファイルを読み込む3つのメソッドについて詳しく説明していきます。


open関数

open関数は、Pythonのプログラムからファイルを利用できるようにしてくれるものです。
シンプルなopen関数の構文は「open　( file , mode )」です。それぞれの引数には

    file：オープンするファイル
    mode：オープンするモード

を指定します。

modeに指定できる値の種類や使い方は以下の通りです。

modeの値 	      モード
‘ r ‘ 	          読み込み用
‘r+’ 	          既存ファイルの読み書き用
‘ w ‘ 	          書き込み用
‘w+’ 	          ファイルの読み書き用
‘ a ‘ 	          追記用
‘a+’ 	          追記・読み書き用
‘ x ‘ 	          排他的書き込み用
                  すでにファイルがあるときはエラーとなる
‘ b ‘ 	          バイナリモード
‘ t ‘ 	          テキストモード

これらのモードは次のように使用します。

1.　＃　読み込む
2.　open ( ‘開きたいファイル’ , ‘r’ )
3.
4.　＃　書き込み
5.　open ( ‘開きたいファイル’ , ‘w’ )
6.
7.　＃　読み書き
8.　open ( ‘開きたいファイル’ , ‘w+’ )

または、キーワード引数を指定して記述することもできます。

1.　＃　読み込む
2.　open ( ‘開きたいファイル’ , mode=’r’ )
3.
4.　＃　書き込み
5.　open ( ‘開きたいファイル’ , mode=’w’ )
6.
7.　＃　読み書き
8.　open ( ‘開きたいファイル’ , mode=’w+’ )

モードを省略した場合、読み込みモード「’r’」とみなされるため、
読み込む際には省略することもできます。


readメソッド

「readメソッド」とは、ファイル内容をすべて読み込み、1つの文字列として返すメソッドです。
実際にコードを使用して詳しく説明していきます。
まず、次のようなテキストファイル「sample.txt」を用意します。

#sample1.txt
1. Hello World
2. Hello Python
3. Hello Sample

そして次のプログラムを実行してみましょう。
"""

f = open('sample1.txt')
str = f.read()
print(str)
f.close()

"""
実行結果は次のようになります。
"""

# 1. Hello World
# 2. Hello Python
# 3. Hello Sample

"""
このように、read( )ではファイルの中身をすべて読み込み1つの文字列として返します。


readlineメソッド

「readlineメソッド」は、ファイルから1行ずつ読み出し、文字列を返すメソッドです。
読み込みを行うサイズも指定できますよ。
では、実際に呼び出してみましょう。
"""

f = open('sample1.txt')    # 開きたいファイルを指定
line = f.readline()
print(line)
f.close()

"""
このコードを実行すると次のようになります。
"""

# 1. Hello World

"""
readline( )は最初の行から1行ずつ読み込むため、
すべての内容を読み込むにはループ処理を使用します。
"""

f = open('sample1.txt')
line = f.readline()
for i in line:
	print(line)
line = f.readline()
f.close()

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

# 1. Hello World

"""
readlinesメソッド

「readlinesメソッド」はファイル内容をすべて読み込み、各行を要素とするリストを返すメソッドです。
readlineメソッドとは違い、反復処理を簡単に記述できますよ。 
"""

f = open('sample1.txt')
list = f.readlines()
print(list)
f.close()

# ['1. Hello World\n', '2. Hello Python\n', '3. Hello Sample']

"""

readlineメソッドと同じように、
要素となる文字列の末尾には改行コードが含まれることに注意してください。
また、readメソッドと同じようにreadinesメソッドでは
基本的にはすべての内容が一度に読み込まれる点には注意しておきましょう。
readlines( )で読み込んだファイルを1行ずつ表示するにはfor文を使用して次のように記述します。
"""

f = open('sample1.txt')
list = f.readlines()
for line in list:
	print(line)

f.close()

# 1. Hello World

# 2. Hello Python

# 3. Hello Sample


print("--- テキストファイルに書き込む ---")


"""
テキストファイルへの書き込みを行う目的でファイルをオープンする場合、
mode引数に「’w’」を指定することになります。
ここでは新規ファイルとして「myfile . txt」を作成して、書き込みを行ってみましょう。
"""
























