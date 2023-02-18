#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- Tkinter pack ---")


"""
このページでは、packメソッドを使用してウィンドウに
ウィジェットを配置する方法について解説します。
少し複雑なので一旦さらっと流し読み、
実際にGUIアプリケーションを作る際に必要に応じて読むことをおすすめします。
"""


print("--- pack ---")


"""
何も指定がない場合、
packはウィジェットを上から順に配置します。
2つのラベルを順に配置してみます。
"""


import tkinter as tk

root = tk.Tk()
root.title('サンプル')
root.geometry('360x240')
root.configure(bg='#E0E0E0')

label1 = tk.Label(root, text='ラベル１', bg='#FF0000', fg='#FFFFFF')
label1.pack()

label2 = tk.Label(root, text='ラベル２', bg='#0000FF', fg='#FFFFFF')
label2.pack()

root.mainloop()

"""
Tkinterでウィジェットを配置した際、見えないスペースが割り当てられます。
この講座ではそれを領域と呼称することにします。
先程のサンプルでは以下のように横長の領域が割り当てられています。

また、packを呼び出す際いくつかのオプションパラメータで
様々に配置領域をカスタマイズすることが可能です。
順に解説していきます。
"""


print("--- fill ---")


"""
fillオプションを指定すると指定した方向に領域内を満たします。
fillの値は以下の通り文字列で指定します。

    x:横方向
    y:縦方向
    both：縦横方向

fillオプションでxを指定すると横方向に領域を満たします。
"""

import tkinter as tk


root = tk.Tk()
root.title('sample')
root.geometry('360x240')
root.configure(bg='#E0E0FF')

label1 = tk.Label(root, text='ラベル１', bg='#FFA0A0', fg='#FFFFFF')
label1.pack(fill='x')

label2 = tk.Label(root, text='ラベル2', bg='#A0A0FF', fg='#FFFFFF')
label2.pack()

root.mainloop()

"""
注意点として、以下のようにyを指定しても縦方向に領域が拡大されない、
という点が挙げられます。
"""

import tkinter as tk


root = tk.Tk()
root.title('sample')
root.geometry('360x240')
root.configure(bg='#E0E0FF')

label1 = tk.Label(root, text='ラベル１', bg='#FFA0A0', fg='#FFFFFF')
label1.pack(fill='x')

label2 = tk.Label(root, text='Area 2', bg='#00A000', fg='#FFFFFF')
label2.pack(fill='y')

root.mainloop()

"""
これはpackは先程の図の通りすでに領域が割り当て済みであることに起因します。
次の解説するexpandで縦方向まで領域を拡張することができます。
"""


print("--- expand ---")


"""
expandオプションを使用すると、
ウィジェットに割り当てる領域を可能な限り拡張します。
"""

import tkinter as tk


root = tk.Tk()
root.title('sample')
root.geometry('360x240')
root.configure(bg='#E0E0E0')

label1 = tk.Label(root, text='ラベル１', bg='#FF0000', fg='#FFFFFF')
label1.pack(expand=True)

label2 = tk.Label(root, text='ラベル2', bg='#0000FF', fg='#FFFFFF')
label2.pack(expand=True)

root.mainloop()

"""
fill='both'を指定してみてください。
ウィジェットに割り当てられた領域が確認できます。
"""

import tkinter as tk


root = tk.Tk()
root.title('sample')
root.geometry('360x240')
root.configure(bg='#E0E0E0')

label1 = tk.Label(root, text='ラベル１', bg='#FF0000', fg='#FFFFFF')
label1.pack(expand=True, fill='both')

label2 = tk.Label(root, text='ラベル２', bg='#0000FF', fg='#FFFFFF')
label2.pack(expand=True, fill='both')

root.mainloop()


print("--- side ---")


"""
sideオプションでウィジェットの配置位置を以下の中から指定することが可能です。

    tk.LEFT・・・左
    tk.TOP・・・上
    tk.RIGHT・・・右
    tk.BOTTOM・・・下

ただし、ぐるりと順番に配置すると大方の予想とは異なりずれが発生します。
"""

import tkinter as tk


root = tk.Tk()
root.title('sample')
root.geometry('360x240')
root.configure(bg='#E0E0E0')

label1 = tk.Label(root, text='ラベル１', bg='#FF0000', fg='#FFFFFF')
label1.pack(side=tk.LEFT)

label2 = tk.Label(root, text='ラベル２', bg='#00FF00', fg='#FFFFFF')
label2.pack(side=tk.TOP)

label3 = tk.Label(root, text='ラベル３', bg='#0000FF', fg='#FFFFFF')
label3.pack(side=tk.RIGHT)

label4 = tk.Label(root, text='ラベル４', bg='#FF00FF', fg='#FFFFFF')
label4.pack(side=tk.BOTTOM)

root.mainloop()


"""
つまり、pack()のsideは余っている領域のうち指定した側の上から下まで、
左から右までを領域として確保します。
ですので、上下左右対象としたい場合は領域の指定順を考慮する必要があります。
以下のコードでは左右を配置した後上から配置することで上下左右対象にしています。
"""

import tkinter as tk


root = tk.Tk()
root.title('sample')
root.geometry('360x240')
root.configure(bg='#E0E0E0')

label1 = tk.Label(root, text='ラベル１', bg='#FF0000', fg='#FFFFFF')
label1.pack(side=tk.LEFT)

label3 = tk.Label(root, text='ラベル３', bg='#0000FF', fg='#FFFFFF')
label3.pack(side=tk.RIGHT)

label2 = tk.Label(root, text='ラベル２', bg='#00FF00', fg='#FFFFFF')
label2.pack(side=tk.TOP)

label4 = tk.Label(root, text='ラベル４', bg='#FF00FF', fg='#FFFFFF')
label4.pack(side=tk.BOTTOM)

root.mainloop()


print("--- ipadx、ipady ---")


"""
packの引数にipadx、ipadyを指定するとそれぞれx方向、
y方向にその領域を広げてパディングします。
"""

import tkinter as tk


root = tk.Tk()
root.title('sample')
root.geometry('360x240')
root.configure(bg='#E0E0FF')

label1 = tk.Label(root, text='Area １', bg='#A00000', fg='#FFFFFF')
label1.pack(ipadx=50, ipady=10)

label3 = tk.Label(root, text='Area ２', bg='#00A000', fg='#FFFFFF')
label3.pack(ipadx=10, ipady=50)

root.mainloop()

"""
x軸方向、y軸方向それぞれipadx、ipadyで指定した領域分拡張されます。
"""
