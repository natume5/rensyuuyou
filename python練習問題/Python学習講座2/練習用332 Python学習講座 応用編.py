#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Buttonウィジェット ---")


"""
ここまでウィジェット、メインウィンドウ、イベント、ウィジェットの配置方法について
解説してきました。
基本的な知識はこれで十分なのですが、
最後に解説する電卓アプリ作成のために
ここからButtonとEntryについてもう少し詳しく解説します。
"""


print("--- Button ---")


"""
Buttonウィジェットはその名の通りボタンを表します。
復習として簡単にボタンを配置したウィンドウを作成してみましょう。
"""

from tkinter import Tk, Button

# メインウィンドウ生成
root = Tk()

# ボタンウィジェットをメインウィンドウに配置
button = Button(root, text='button1')
button.pack()

# イベントループの開始
root.mainloop()

"""
実行すると以下の通りボタンが配置されたウィンドウが表示されます。
Buttonにはtextという引数でボタンの名称を指定しましたが、
これ以外に以下のようなオプションを引数で指定することができます。

代表的なオプション

    command:ボタン押下時のイベントハンドラ
    width:ボタンの幅
    height:ボタンの高さ
    background:背景色
    activebackground:ボタン押下時の背景色
    text:ボタン上に表示する文字列
"""


print("--- Buttonのオプション ---")


"""
代表的な引数について簡単に解説します。
commandによるイベントハンドラ登録

イベントの解説でbindメソッドを使用したイベント登録を紹介しましたが、
クリック時の処理であればボタン生成時に処理を登録することも可能です。
以下のコードではボタンをクリックした際にラベルも文言を変更しています。
"""

from tkinter import Tk, StringVar, Button, Label

# メインウィンドウ生成
root = Tk()

# メインウィンドウの設定
root.title('サンプル')

# ラベルの配置
text = StringVar()
text.set('サンプルラベル')
label = Label(root, textvariable=text)
label.pack()

# イベントハンドラ
def my_func():
	global text
	text.set('ボタンがクリックされました')

# ボタンウィジェットをメインウィンドウに配置、イベントを登録
button = Button(root, text='button1', command=my_func)
button.pack()

# イベントループの開始
root.mainloop()


"""
width、 heightによる横幅、高さの指定

width、heightでそれぞれ幅、高さを指定することができます。
ただし、これは単位が文字の大きさとなるため、
座標ベースでGUIを設計すると少し難儀します。
記事後半に補足がありますので参考にしてください。
以下のコードでは幅10、高さ10のボタンを生成して配置しています。
前述の通り文字の大きさが基準になっているため縦長になっています。
"""

from tkinter import Tk, Button

# メインウィンドウ生成
root = Tk()

# ボタンウィジェットをメインウィンドウに配置
button = Button(root, text='button1', width=10, height=10)
button.pack()

# イベントループの開始
root.mainloop()


"""
backgroundとactivebackgroundによる色指定

backgroundで背景色、activebackgroundで押下時の背景色を
指定することができます。
以下のコードは通常青、クリック時に白になります。
"""

from tkinter import Tk, Button

# メインウィンドウ生成
root = Tk()

# ボタンウィジェットをメインウィンドウに配置
button = Button(root, text='button1', background='#FFFFFF', activebackground='#78b6ff')
button.pack()

# イベントループの開始
root.mainloop()


print("--- 補足 Buttonサイズをピクセルで指定する方法 ---")


"""
前述の通りButtonのサイズは文字サイズが基準になります。
ピクセル単位で指定したい場合は
仮想的な1x1のピクセルイメージを引数imageで設定し
かつcompoundに'c'を指定します。
例えば、30x30のボタンを生成する場合は以下のように記述します。
"""

from tkinter import Tk, Button, PhotoImage

# メインウィンドウ生成
root = Tk()

# 仮想的なピクセルイメージを生成
virtual_button_px = PhotoImage(width=1, height=1)

# ボタンウィジェットをメインウィンドウに配置
button = Button(root, text='X', image=virtual_button_px,
	width=100, height=100, compound='c')
button.pack()

# イベントループの開始
root.mainloop()

