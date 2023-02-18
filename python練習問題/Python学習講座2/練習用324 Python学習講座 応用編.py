#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Tkinter インストールとHello world ---")


"""
このページではTkinterのインストールと
初歩的なウィンドウ表示のためのコードを紹介します。
"""


print("--- Tkinterのインストール ---")


"""
まずはインストールについてです。
標準ライブラリに含まれているため通常Python 3を
インストールすれば別途インストールする必要はありません。
ただし、一部のUnix系OSではそのままでは動かない場合があります。
使用可否を確認する場合、以下のコマンドを実行してみてください。

python -m tkinter

以下のようなウィンドウが表示されれば使用可能です。
エラーになった場合はページ下部の補足を参照してください。
"""


print("--- TkinterでHello World ---")


"""
早速使ってみましょう。Pythonがインストールされた環境で
以下のスクリプトを実行してみてください。
"""

from tkinter import Tk, Label

# メインウィンドウ生成
root = Tk()

# メインウィンドウの設定
root.title('サンプル1')

# Labelウィジェットをメインウィンドウに生成＆配置
label = Label(root, text='Hello world')
label.pack()

# イベントループの開始
root.mainloop()

"""
以下のようなウィンドウが表示されます。
入門編等で作成してきたコマンドラインのものとは異なり、
ウィンドウがありマウスで操作することが可能です。
画面上部の✕ボタンをクリックすると、ウィンドウが閉じられます。

少ない行数で簡単にウィンドウを作成することができました。
コード中のそれぞれの意味は次回以降詳しく説明します。
"""


print("--- 補足 tkinterが使えない ---")


"""
WindowsやMacでインストーラを使用すると
そのままtkinterモジュールが使用できるはずですが、
一部のOSではPython3をインストールしても
tkinterが使用できない場合があります。
前述のとおり、tkinterはTkを操作するライブラリですが、
一部のOSではPythonとは別途Tkをインストールする必要があります。
例えば、Ubuntu等、Debian系の場合は以下のコマンドで
インストールすることができます。

sudo apt-get install tk-dev

RHE系の場合は以下のコマンドでインストールすることができます。

sudo yum install tk-devel
"""
