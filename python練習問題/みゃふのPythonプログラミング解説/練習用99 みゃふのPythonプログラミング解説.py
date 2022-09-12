#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説 ---")
print("--- 実行ファイル（exeファイル）化するpyinstaller ---")


"""
pyinstallerは「pythonコードを実行ファイル化して実行できるようにする」ライブラリです。

Pythonの実行環境がない場合でもpyinstallerを使って
実行ファイルにすることでプログラムを動かすことができます。

なお、ここでは次の環境で実行します。

MacOS Mojave 10.14.6
Python 3.7.6
pyinstaller 4.0


pyinstallerのインストール

pyinstallerはpipからインストールできます。

$ pip install pyinstaller

このコマンドを実行、少し待てばインストール完了です。
pyinstallerの基本

ではpyinstallerを使ってみましょう。

今回は最もシンプルに、実行したら文字列をprint()で出力するプログラムを
実行ファイル化して実行してみます。

[test.py]

print("pyinstaller succeeded.")

Python

このファイルをpyinstallerで実行ファイル化します。

実行ファイルは3つのディレクトリと1つのファイルを吐き出しますので、
まずはcdで作業ディレクトリに移動しておきましょう。

作業ファイルに移動したら次のコマンドを実行します。

$ pyinstaller test.py

pyinstallerの引数に作成したtest.pyを渡すだけです。
少し待って「completed successfully.」が表示されたら無事に実行ファイルが作成されています。
作業ディレクトリ内に「__pycache」「build」「dist」「test.spec」が作成されます。
その中のdistディレクトリの中に「test」というファイルがあります。これが実行ファイルです。
Finderからtestファイルを実行してみましょう。
実行するとターミナルが開き、print(pyinstaller succeeded.)が表示されました。
dist内のファイルを見ても分かるとおり、
pythonの実行ファイルも入っているのでpythonの実行環境がないPCでも実行することができます。
"""

"""
pyinstallerのオプション

次にpyinstallerを使う際によく使うオプションを見ていきましょう。


--onfile

--onfileオプションはdist内の複数の関連ファイルを一つのファイルにまとめられるオプションです。

$ pyinstaller test.py --onefile

生成されたdistディレクトリの中を見てみると、実行ファイルが1つのみ作成されているのがわかります。
"""


"""
どちらも同じようにプログラムの実行はできますが、
--onefileした方がスッキリしているので個人的にはこちらの方が好きです。


--noconsole

--noconsoleオプションはコンソール画面を開かずにプログラムを実行したい場合に付与します。
デスクトップアプリを実行したい場合は--noconsoleを付けましょう。
試しにこちらのコードを実行してみます。
"""

import tkinter as tk

win = tk.Tk()
win.title('pyinstaller succeeded.')    # タイトル
win.geometry('400x300')    # 画面サイズ
win.mainloop()    # 開く

"""
tkinterはpythonに標準で用意されている「デスクトップアプリを作成するためのライブラリ」です。
今回はウィンドウを開きたいだけなので、タイトルと画面サイズのみ指定しています。
次に下のコマンドを実行します。

pyinstaller test.py --noconsole

先ほどまで作成していたファイル以外に
「test.app」がdist配下に作成されるので、実行してみましょう

コンソールは開かず、代わりにウィンドウが開きました。
"""
