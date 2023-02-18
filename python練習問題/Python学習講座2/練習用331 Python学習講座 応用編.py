#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Tkinter grid ---")


"""
このページでは、gridメソッドを使用して
ウィンドウにウィジェットを配置する方法について解説します。
少し複雑で長いため一旦さらっと流し読み、
実際にGUIアプリケーションを作る際に必要に応じて読むことをおすすめします。
"""


print("--- grid ---")


"""
ウィジェットの配置方法で最後に紹介するのがgridメソッドです。
ウィンドウをグリッドと呼ばれる格子状に区画分けし、
列番号と行番号でウィジェットを配置する区画を指定します。
グリッドは下図のように0始まりで列(column)と行(row)で番号付けられます。

例えば2x2のグリッドの右下のセルにラベルを配置する場合、以下のようになります。
"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label.grid(column=1, row=1)
root.mainloop()

"""
コードの詳しい解説は後ほど行います。
実行すると以下のように右下(1, 1)の領域に
ラベルが配置されたことが確認できます。
"""


print("--- グリッドの設定 ---")


"""
gridを使用する場合、必要に応じて予め
ウィンドウなどのウィジェットを配置するオブジェクトに対して
グリッドの比率を設定します。

列の設定

columnconfigureで列の設定を行います。

ウィンドウ.columnconfigure(index, weight)

indexで列番号、weightでその列が占める幅を指定します。
例えば、2列で列の幅の比率を1:3にしたい場合、以下のように記述します。

root = tk.Tk()
root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=3)
"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)    # 変更箇所
root.columnconfigure(index=1, weight=3)    # 変更箇所
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label.grid(column=1, row=1)
root.mainloop()

"""
イメージとしては以下のように1列目と2列目の比率が1:3となります。


行の設定

rowconfigureで行の設定を行います。

ウィンドウ.rowconfigure(index, weight)

indexで行番号、weightでその行が占める幅を指定します。
例えば、2行で行の高さの比率を1:3にしたい場合、以下のように記述します。

root = tk.Tk()
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=3)

"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)    # 変更箇所
root.rowconfigure(index=1, weight=3)    # 変更箇所

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label.grid(column=1, row=1)
root.mainloop()

"""
イメージとしては以下のように1行目と2行目の比率が1:3となります。
"""


print("--- グリッドを指定した配置 ---")


"""
次に配置について解説します。
以下の書式で指定したグリッドに配置することができます。

ウィジェット.grid(**オプション)

パラメータにはオプションとして以下を指定することができます。
スパン、スティッキー、パディングについては後方で説明します。

    column：列番号
    row：行番号
    columnspan：列スパン
    rowspan：行スパン
    sticky：区画内部の配置箇所を指定
    padx：区画をx方向にパディング
    pady：区画をy方向にパディング
    ipadx：区画をx方向にパディング、ウィジェットの配置可能範囲も拡張
    ipady：区画をy方向にパディング、ウィジェットの配置可能範囲も拡張

以下のコードでは2x2のグリッドの(1, 1)に配置しています。
"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label.grid(column=1, row=1)
root.mainloop()

"""
コードの詳しい解説は後ほど行います。
実行すると以下のように右下(1, 1)の領域に
ラベルが配置されたことが確認できます。
"""


print("--- sticky ---")


"""
先程のサンプルですが、区画の大きさに対しウィジェットが小さく、
区画の中央部に配置されています。
stickyオプションを指定すると、
区画内の特定の方向にウィジェットを配置したり拡張することができます。
方向はこれまで使用してきたtkモジュールのN、E、W、Sを組み合わせて使用します。

例えば、区画の右下に配置する場合は以下のように記述します。

label.grid(column=1, row=1, sticky=tk.SE)

以下のように区画の右下に配置されました。
"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label.grid(column=1, row=1, sticky=tk.SE)    # 変更箇所
# stickyのSEはS(南)E(東)
root.mainloop()

"""
さらに方向とは異なり縦横方向に組み合わせると、
区画内でウィジェットを拡張することが可能です。
以下の通り配置/拡張されます。

例えば、以下のようにNSEWを指定すると区画内を専有することができます。

label.grid(column=1, row=1, sticky=tk.NSEW)
"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label.grid(column=1, row=1, sticky=tk.NSEW)    # 変更箇所
root.mainloop()


print("--- span ---")


"""
特定の区画を下図のように拡張することが可能でこれをスパンと呼びます。

オプションのcolumnspan、rowspanでスパン数を指定することができます。
以下のコードではこれまでの2x2のグリッドの
(0, 1)～(1, 1)まで拡張し配置しています。
なお、以降のコードでは視認性を上げるために
sticky=tk.NSEWを指定することにします。

label.grid(column=0, row=1, columnspan=2, sticky=tk.NSEW)
"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label.grid(column=0, row=1, columnspan=2, sticky=tk.NSEW)    # 変更箇所
root.mainloop()


print("--- パディング ---")


"""
padx、padyを指定すると、区画の外側をパディングすることができます。
まず、説明の準備として2x2のグリッドにラベルを配置してみます。
"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

label1 = tk.Label(
	root,
	text='sample',
	bg='blue',
	fg='white',
)

label1.grid(column=0, row=0, sticky=tk.NSEW)

label2 = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

label2.grid(column=0, row=1, sticky=tk.NSEW)

label3 = tk.Label(
	root,
	text='sample',
	bg='green',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label3.grid(column=1, row=0, sticky=tk.NSEW)

label4 = tk.Label(
	root,
	text='sample',
	bg='yellow',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label4.grid(column=1, row=1, sticky=tk.NSEW)


root.mainloop()

"""
ではここで、label4に対し以下のように(1, 1)区画の外側に対し
x方向に50、y方向に30にパディングしています。

label4.grid(column=1, row=1, sticky=tk.NSEW, padx=50, pady=30)

実行すると以下の通り区画が拡張されて隙間ができていることが確認できます。
"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

label1 = tk.Label(
	root,
	text='sample',
	bg='blue',
	fg='white',
)

label1.grid(column=0, row=0, sticky=tk.NSEW)

label2 = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

label2.grid(column=0, row=1, sticky=tk.NSEW)

label3 = tk.Label(
	root,
	text='sample',
	bg='green',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label3.grid(column=1, row=0, sticky=tk.NSEW)

label4 = tk.Label(
	root,
	text='sample',
	bg='yellow',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label4.grid(column=1, row=1, sticky=tk.NSEW, padx=50, pady=30)


root.mainloop()

"""
ipadx, ipadyを使用すると、
さらにパディングされた範囲にウィジェットを配置することが可能です。

label4.grid(column=1, row=1, sticky=tk.NSEW, ipadx=50, ipady=30)
"""

import tkinter as tk

root = tk.Tk()
root.title('grid sample')
root.geometry('360x240')

root.columnconfigure(index=0, weight=1)
root.columnconfigure(index=1, weight=1)
root.rowconfigure(index=0, weight=1)
root.rowconfigure(index=1, weight=1)

label1 = tk.Label(
	root,
	text='sample',
	bg='blue',
	fg='white',
)

label1.grid(column=0, row=0, sticky=tk.NSEW)

label2 = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

label2.grid(column=0, row=1, sticky=tk.NSEW)

label3 = tk.Label(
	root,
	text='sample',
	bg='green',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label3.grid(column=1, row=0, sticky=tk.NSEW)

label4 = tk.Label(
	root,
	text='sample',
	bg='yellow',
	fg='white',
)

# グリッドの(1, 1)にラベルを配置
label4.grid(column=1, row=1, sticky=tk.NSEW, ipadx=50, ipady=30)


root.mainloop()
