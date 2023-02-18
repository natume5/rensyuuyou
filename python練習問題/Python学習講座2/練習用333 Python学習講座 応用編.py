#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Entryウィジェット ---")


"""
このページではEntryウィジェットの使い方について解説します。
"""


print("--- Entryウィジェット ---")


"""
テキスト入力欄のウィジェットをTkinterではEntryと呼びます。
まずは簡単な表示をしてみましょう。
"""

from tkinter import Tk, Entry

# メインウィンドウ生成
root = Tk()

# ボタンウィジェットをメインウィンドウに配置
entry = Entry(root)
entry.pack()

# イベントループの開始
root.mainloop()

"""
テキスト入力欄が配置されました。
代表的なものとして以下のようなオプションを指定することができます。

    background:背景色
    width:横幅
    textvariable:入力値を格納する変数
    justify:入力位置(left, right, center)
"""


print("--- Entryのオプション ---")


"""
それではEntryのオプション引数について簡単に解説します。
backgroundによる背景色の指定

他のウィジェットでも使用した通り#RGB等で色を指定することが可能です。
以下のように記述すると青色の入力欄を配置することができます。
"""

from tkinter import Tk, Entry

# メインウィンドウ生成
root = Tk()

# ボタンウィジェットをメインウィンドウに配置
entry = Entry(root, background='#0000FF')    # 変更箇所
entry.pack()

# イベントループの開始
root.mainloop()


"""
justifyによる入力位置指定

デフォルトでは左寄せとなりますが、
justify引数に文字列left, right, centerを指定するとそれぞれ左寄せ、
右寄せ、中央寄せにカスタマイズすることができます。
例えば、右寄せにする場合は以下のように指定します。
"""

from tkinter import Tk, Entry

# メインウィンドウ生成
root = Tk()

# ボタンウィジェットをメインウィンドウに配置
entry = Entry(root, justify='right')    # 変更箇所
entry.pack()

# イベントループの開始
root.mainloop()


"""
textvariableによる変数指定

入力したテキストを格納するStringVar変数を指定します。
以下のコードでは、Entryで入力したテキストをラベルに表示しています。
Entryに適当に文字を入力すると、ラベルにその値が反映されます。
"""

from tkinter import Tk, Entry, Label, StringVar


# メインウィンドウ生成
root = Tk()

# ラベルの配置
text = StringVar()
text.set('サンプル文字列')
label = Label(root, textvariable=text)
label.pack()

# ウェジェットをメインウィンドウに配置
entry = Entry(root, textvariable=text)
entry.pack()

# イベントループの開始
root.mainloop()
