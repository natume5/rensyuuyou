#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- ウィジェットの配置 ---")


print("--- 3つのGeometry manager ---")


"""
これまでのサンプルでは、packというメソッドでウィジェットを配置しました。
pack以外にplace、gridという配置用のメソッドが用意されています。
これらはGeometry managerと呼ばれており、
アプリケーションのレイアウトを様々な方法で指定することができます。

    pack：指定した順に（上から）配置する
    place：座標を指定して配置する
    grid：グリッド位置を指定して配置する

以降、それぞれの概要を解説します。


pack

packはこれまで使用してきたように、
指定がない限り上から順に詰め込むようにウィジェットを配置するメソッドです。
座標などの指定がなく簡単に使用できるためサンプルコード等でよく使われますが、
癖が強く複雑なUIのアプリケーションを作成する場合は
あまり使用されないという印象があります。

place

placeはウィンドウ上の座標を指定してウィジェットを配置するメソッドです。
座標は絶対座標と相対座標で指定することが可能です。
ドローツール等で作成したUI設計書の座標が使えるため、
個人的には一番使うのが楽だと感じています。

grid

gridはウィンドウを格子状の区画で区切り、
どの区画に配置するかを指定するメソッドです。
レイアウトをグリッドベースで設計する場合にはこちらのメソッドが楽かと思います。
"""


print("--- Labelの補足 ---")


"""
Geometry managerの解説の前に、
解説で使用するためLabelウィジェットについて補足説明します。
今後ウィジェットの配置の解説でLabelウィジェットを使用します。
labelは生成時に以下の引数で背景色とフォント色を指定することが可能です。

    bg：背景色
    fg：フォント色

たとえば、背景色青(0000FF)、文字色白(FFFFFF)のラベルを生成する場合は
以下のように記述します。

label1 = tk.Label(root, text="Area", bg="#0000FF", fg="#FFFFFF")

これを使用して以降の解説でウィジェットの領域部分を表現します。
例えば、次ページで解説するpackの場合以下のように2つ配置すると、
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
