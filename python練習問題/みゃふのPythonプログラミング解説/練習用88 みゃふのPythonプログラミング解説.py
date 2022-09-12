#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- コマンドライン引数の使い方（sys）  ---")


"""
コマンドライン引数をご存知でしょうか？
コマンドライン引数とはpythonのファイルを実行するときに渡す引数のことです。
ここでは「コマンドライン引数って何？」「コマンド引数はどうやって使うの？」といった方へ、
コマンドライン引数について解説します。
"""


print("--- コマンドライン引数とは？  ---")


"""
コマンドラインで引数を指定してプログラムを実行したい場合、コマンドライン引数を使うことで実行できます。
WindowsではコマンドプロンプトでPCのローカルにあるプログラムを実行する際に、引数を指定して実行します。
"""


print("--- コマンドライン引数の使い方  ---")


"""
コマンドライン引数はsysライブラリのargvを使います。
インデックス番号を指定してコマンドライン引数を取得する

pythonのプログラムを実行する際に引数を渡すと、
プログラム内でsys.argvを使うことでコマンドライン引数を取得することができます。

まずは、pythonファイルを準備します。

[sys_sample.py]

import sys

print('1 : ' + sys.argv[1])
print('2 : ' + sys.argv[2])
print('3 : ' + sys.argv[3])
print('4 : ' + sys.argv[4])

[実行コマンド]

$ python sys_sample.py Hello みゃふ 100 True

まずプログラム内でsysをインポートします。インポート後、
実行コマンドから渡される予定の引数をsys.argvで取得し出力しています
（なぜ[1]から始まるのかについては後述）。

コードはsys_sample.pyというファイル名で保存し、実行コマンドで呼び出します。
その際「Hello」「みゃふ」「100」「True」の4つの引数を半角スペース区切りで指定します。
こうすることでプログラム内に引数を渡すことができ、結果として渡した引数が出力されました。


sys.argvの1番目の要素はファイル名

さて、sys.argvがなぜ[1]から始まるのか？という点が気になるかと思います。
通常のインデックス番号であれば0から始まるのがセオリーです。
実はsys.argvは0番目に必ず実行したファイル名が格納されます。
なので、引数は1番目から入ってくるので注意が必要です。

[sys_sample.py]

import sys
print('0 : ' + sys.argv[0])

[実行コマンド]

$ python sys_sample.py

[出力結果]

0 : sys_sample.py


コマンドライン引数は全て文字列

コマンドライン引数は全て文字列として扱われます。
100やTrueなどの本来文字列として扱いたくない引数は、
プログラム内で受け取った後に変換する必要があります。

[sys_sample2.py]

import sys

print('変換前')
print(type(sys.argv[1]))
print(type(sys.argv[2]))
print('変換後')
print(type(int(sys.argv[1])))
print(type(bool(sys.argv[2])))

[実行コマンド]

$ python sys_sample2.py 100 True

[出力結果]

変換前
<class 'str'>
<class 'str'>
変換後
<class 'int'>
<class 'bool'>


コマンドライン引数を全て取得する

sys.argvは文字列のリストなので、for..inで全ての引数を取得できます。
その場合1番目の引数がファイル名であることに注意しましょう。
次のようにすることで1番目の要素以外を取得できます。

import sys

for i, argv in enumerate(sys.argv):
    if (i == 0): continue
    print(argv)

[実行コマンド]

$ python sys_sample3.py Hello みゃふ 100 True

[出力結果]

Hello
みゃふ
100
True


len()を使ってエラーを回避する

sys.argvはリストなので、想定しているよりも引数の数が少ないとIndexErrorになります。

import sys
print(sys.argv[3])

[実行コマンド]

$ python sys_sample.py 1 2

[出力結果]

IndexError: list index out of range

これを回避するにはlen()を使ってリストの要素数を取得するのが効果的です。

import sys

if len(sys.argv) - 1 >= 3:
    print(sys.argv[3])
else:
    print('引数が足りていません')

[実行コマンド]

$ python sys_sample4.py 1 2

[出力結果]

引数が足りていません


try〜exceptでエラーを回避する

len()を使う以外にもtry〜exceptを使ってエラーを回避する方法もあります。
try〜exceptではエラーを検知したときに異常時の処理を実行するための構文です。

import sys

try:
    print(sys.argv[3])
except IndexError:
    print('引数が足りていません')

[実行コマンド]

$ python sys_sample5.py 1 2

[出力結果]

引数が足りていません
"""



























