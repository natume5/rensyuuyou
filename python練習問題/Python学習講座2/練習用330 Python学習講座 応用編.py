#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Tkinter place ---")


"""
このページでは、placeメソッドを使用して
ウィンドウにウィジェットを配置する方法について解説します。
少し複雑で長いため一旦さらっと流し読み、
実際にGUIアプリケーションを作る際に必要に応じて読むことをおすすめします。
"""


print("--- place ---")


"""
placeメソッドはウィンドウ上の右上を原点としたx, 
y座標を指定してウィジェットを配置します。

ウィジェット上の左上が座標指定点となっていますが、この点をアンカーと呼びます。
アンカーはデフォルトでは左上ですが、8方と中央を指定することができます。
また、座標は絶対座標以外に相対座標を使用することもできます。
以下の書式で実行します。

ウィジェット.place(**オプション)

パラメータに指定できるオプションは以下のものがあります。

    x：x軸絶対座標
    y：y軸絶対座標
    relx：x軸相対座標
    rely：y軸相対座標
    anchor：アンカー位置
    width：ウィジェット幅の絶対距離
    height：ウィジェット高の絶対距離
    relwidth：ウィジェット幅の相対距離
    relheight：ウィジェット高の相対距離

例えば、ラベルを座標(300, 200)に配置する場合は以下のように記述します。
"""

import tkinter as tk

root = tk.Tk()
root.title('place sample')
root.geometry('360x240')

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

label.place(x=300, y=200)
root.mainloop()


print("--- アンカー ---")


"""
先程解説したとおり、デフォルトでは左上の座標を指定することになりますが、
anchorパラメータでアンカー位置を指定することができます。
以下の通りtkモジュールのN、E、W、Sの4方位を組み合わせた
8方とCenterの計9種類指定が指定可能です。

先程のコードについて、CENTERを指定する場合は以下のようになります。
"""

import tkinter as tk

root = tk.Tk()
root.title('place sample')
root.geometry('360x240')

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

label.place(x=300, y=200, anchor=tk.CENTER)
root.mainloop()


print("--- 相対座標指定 ---")


"""
座標はウィンドウ上の相対位置を指定することも可能です。
相対位置はウィンドウサイズを1とし、0～1の範囲で指定します。
例えば、画面中央に配置したい場合は以下のように記述します。
"""

import tkinter as tk

root = tk.Tk()
root.title('place sample')
root.geometry('360x240')

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.mainloop()

"""
先程のコードを実行してウィンドウサイズを変えると
ウィジェットの位置が中央を保っていることが確認できます。
このように相対座標を指定するとウィンドウサイズを変えても
位置関係を保つことができます。
"""


print("--- 幅、高さの指定 ---")


"""
widthとheight

widthとheightで絶対距離によるウィジェットの幅、
高さを指定することができます。
例えば、先程のコードを以下のようにすると、
100x50のウィジェットを配置することができます。
"""

import tkinter as tk

root = tk.Tk()
root.title('place sample')
root.geometry('360x240')

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

label.place(relx=0.5, rely=0.5, anchor=tk.CENTER,
	width=100, height=50)
root.mainloop()


"""
relwidthとrelheight

relwidthとrelheightで相対距離によるウィジェットの幅、
高さを指定することができます。
相対距離はウィンドウサイズを1とし、0～1の範囲で指定します。
例えば、上のコードを以下のようにすると、
画面幅の50%、高さの30%を占めるよう配置できます。
"""

import tkinter as tk

root = tk.Tk()
root.title('place sample')
root.geometry('360x240')

label = tk.Label(
	root,
	text='sample',
	bg='red',
	fg='white',
)

label.place(relx=0.5, rely=0.5, anchor=tk.CENTER,
	relwidth=0.5, relheight=0.3)
root.mainloop()
