#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- ウィジェット ---")


"""
前回、文字列を表示するだけのGUIアプリケーションを作ってみました。
今回はラベル以外にボタンや入力欄などを配置してみましょう。
※ 2022/10/17 解説コードのウィジェットについて
当初ttkを使用していましたがデフォルトに変更しました。
ttkについてはこちらで解説しています。
"""


print("--- ウィジェットとは ---")


"""
Tkでは「ウィジェット」でと呼ばれる要素で画面に表示されるものが構成されます。
例えば、前回HelloWorldを表示したラベルや、ボタン、入力欄、
チェックボックス、ラジオボタン等がウィジェットの例として挙げられます。
GUIツールキットによってはコントロールと呼ばれることもあります。
また、メインウィンドウもウィジェットの一種で、
Tkのdocstringには「Toplevel widget of Tk」と説明されています。

メインウィンドウとウィジェットの配置

Tkで画面に何かを表示するということは
ウィジェットを配置することとほぼ同義になります。
前回作成したコードをもう一度見てみましょう。
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
Tk()でウィンドウを生成することができます。
メインウィンドウとも呼ばれるこのウィンドウには
タイトルや最小化、閉じるボタン、マウスでのドラッグアンドドロップができたり等の
基本的な機能が予め用意されています。
上のコードではこのウィンドウの上に11行目で
Labelと呼ばれる文字列を表示するウィジェットを生成しています。
また、通常、ウィジェットには配置のためのメソッドがいくつか用意されており、
12行目で実行しているpack()はそのうちの1つです。
基本的にはTk()でウィンドウを作成し、
ウィジェットを生成する際に
どのウィンドウに配置するかを指定、生成、pack等の配置メソッドを呼び出し、
最後にイベントループを開始する、というフローになります。
（イベントループについては次回説明します。）
"""


print("--- 基本的なウィジェット ---")


"""
ウィジェットには様々な種類があるのですが、
ここでは基本的な以下のものについて紹介します。

    Label
    Frame
    Button
    Checkbutton
    Radiobutton
    Entry
    OptionMenu

今回は各ウィジェットの紹介に留めます。
まずはそれぞれのウィジェットがどういったものなのか、
というのを簡単に知っておいてください。

Label

Labelとは先程説明したようにその名の通りラベルで
文字列を表示するウィジェットです。
生成する際に引数に表示する文字列を指定します。


Frame

Frameとは画面上の枠を表すウィジェットです。
"""

from tkinter import Tk, Label, Frame


# メインウィンドウ生成
root = Tk()

# メインウィンドウの設定
root.title('サンプル')
root.geometry('100x100')

# frameウィジェットをメインウィンドウに配置
frame = Frame(root, width=50, height=50, bg='#000000')
frame['borderwidth'] = 1
frame.pack()

# Labelウィジェットをframe上に配置
label = Label(frame, text='Hello world')
label.pack()

# イベントループの開始
root.mainloop()

"""
以下のようにlabelが枠に囲まれました。
ラベルや後述するボタン、エントリーなどをグルーピング化する際に使用します。


Button

Buttonはその名の通りボタンのウィジェットで押下すると
何らかの処理を呼び出すことができます。
引数textでボタンに表示する文字列を指定することができます。
"""

from tkinter import Tk, Button


# メインウィンドウ生成
root = Tk()

# メインウィンドウの設定
root.title('サンプル')

# Buttonウィジェットをメインウィンドウに生成＆配置
button = Button(root, text='sample button')
button.pack()

# イベントループの開始
root.mainloop()

"""
以下のようにボタンが表示されます。


Checkbutton

Checkbuttonはチェックボタン、チェックボックスなどと呼ばれ、
チェック入力のためのウィジェットです。
押下するとチェック/チェック解除ができます。
"""

from tkinter import Tk, Checkbutton


# メインウィンドウ
root = Tk()

# メインウィンドウの設定
root.title('サンプル')

# Checkbuttonウィジェットをメインウィンドウに生成＆配置
check_button = Checkbutton(root, text='check me.')
check_button.pack()

# イベントループの開始
root.mainloop()

"""
Radiobutton

これもその名の通りラジオボタンのウィジェットです。
"""

from tkinter import Tk, IntVar, Radiobutton

# メインウィンドウ
root = Tk()

# メインウィンドウの設定
root.title('サンプル')

# Radiobuttonウィジェットをメインウィンドウに生成＆配置
variable = IntVar()
radio_button1 = Radiobutton(root, text='option 1', variable=variable, value=1)
radio_button2 = Radiobutton(root, text='option 2', variable=variable, value=2)
radio_button3 = Radiobutton(root, text='option 3', variable=variable, value=3)
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

# イベントループの開始
root.mainloop()

"""
Entry

Entryは入力欄を表すウィジェットです。
"""

from tkinter import Tk, Entry

# メインウィンドウ
root = Tk()

# メインウィンドウの設定
root.title('サンプル')

# Entryウィジェットをメインウィンドウに生成＆配置
entry = Entry(root)
entry.pack()

# イベントループの開始
root.mainloop()

"""
OptionMenu

OptionMenuはドロップダウンメニュー、コンボボックス、セレクトボックス等と
呼ばれる、複数の選択肢の中から値を選ぶことができるウィジェットです。
"""

import tkinter as tk
from tkinter import ttk    # 新たに追加

# メインウィンドウ
root = Tk()

# メインウィンドウの設定
root.title('サンプル')

# Comboboxウィジェットをメインウィンドウに生成＆配置
values = ['One', 'Two', 'Three']
combobox = ttk.Combobox(root, values=values)    # Combobox→ttk.Comboboxに修正
combobox.pack()

# イベントループの開始
root.mainloop()

"""
本講座ではこの後の記事でボタン、エントリーのみ詳細な説明を行います。
それらが理解できれば他のものも公式資料ですんなり理解できると思いますので
他のものの説明は割愛する予定です。
"""



print("--- https://python.keicode.com/ より ---")
print("--- Tkinter Combobox ---")


print("--- ttk.Combobox とは？ ---")


"""
Combobox (コンボボックス) はドロップダウンリストと、
Entry (テキストボックス) の組み合わせボックスです。 
自由に入力できる他、決められた値をドロップダウンリストから
選択することもできます。
「ドロップダウンリスト」と「テキストボックス (Entry)」のコンボなので、
「コンボ」ボックスです。
"""


print("--- ttk.Combobox のオプション ---")


"""
ttk.Combobox ウィジェットの標準オプション

ttk.Combobox ウィジェットでは次の標準オプションが利用できます。

    class
    cursor
    style
    takefocus


ttk.Combobox ウィジェットの justify オプション
ttk.Combobox ウィジェットの justify オプションは
ウィジェット内で文字がどのように整列するか指定します。 
有効な値は left, center, right です。

ttk.Combobox ウィジェットの height オプション
ttk.Combobox ウィジェットの height オプションは
リストボックスの高さを指定します。

ttk.Combobox ウィジェットの postcommand オプション
ttk.Combobox ウィジェットの postcommand オプションは
リストボックスを表示する直前に評価する関数を指定します。

ttk.Combobox ウィジェットの state オプション
ttk.Combobox ウィジェットの state オプションは
コンボボックスの状態を指定します。 
有効な値は normal, readonly, disabled です。
readonly の場合はコンボボックス内の文字の編集はできません。

ttk.Combobox ウィジェットの textvariable オプション
ttk.Combobox ウィジェットの textvariable オプションは
コンボボックスの値を保持するグローバル変数を指定します。

ttk.Combobox ウィジェットの values オプション
ttk.Combobox ウィジェットの values オプションは、
ドロップダウンに表示する値のリストを指定します。

ttk.Combobox ウィジェットの width オプション
ttk.Combobox ウィジェットの width オプションは 
Entry ウィンドウの表示幅を文字数で指定します。
"""


print("--- ttk.Combobox のスタイル ---")


"""
ttk.Combobox のスタイルクラス名は TCombobox です。

TCombobox では次のオプションが指定できます。

    arrowcolor
    arrowsize
    background : 背景色の設定
    bordercolor
    darkcolor
    focusfill
    foreground : 文字色の設定
    fieldbackground
    insertwidth
    lightcolor
    padding
    postoffset
    selectbackground
    selectforeground
"""


print("--- ttk.Combobox のスタイルttk.Combobox のイベント ---")


"""
コンボボックスは、ユーザーがドロップダウンから値を選択した時に
 <<ComboboxSelected>> イベントを生成します。
コンボボックスの bind() メソッドを用いて、
イベントと関数を関連付けすることができます。
"""


print("--- Tkinter Combobox のサンプルコード ---")


"""
ここでは選択項目が変わったときに選択された値を出力します。
また、ボタンを押したときにも、その時点での値を表示します。
"""

from tkinter import *
from tkinter import ttk

if __name__ == '__main__':
    fruits = ['Apple', 'Banana', 'Grape']

    root = Tk()
    root.title('Combobox 1')

    # Frame
    frame = ttk.Frame(root, padding=10)
    frame.grid()

    # Combobox
    v = StringVar()
    cb = ttk.Combobox(
        frame, textvariable=v,
        values=fruits, width=10)
    cb.set(fruits[0])
    cb.bind(
        '<<ComboboxSelected>>',
        lambda e: print('v=%s' % v.get()))
    cb.grid(row=0, column=0)

    # Button
    button1 = ttk.Button(
        frame, text='OK',
        command=lambda: print('v=%s' % v.get()))
    button1.grid(row=0, column=1)

    root.mainloop()

"""
Combobox の値は textvariable 属性で指定した変数に
その都度格納されます。
Combobox の選択が変更したときのコールバックは bind メソッドを用いて、
 <<ComboboxSelected>> 仮想イベントにコールバック関数をアタッチします。
コールバックメソッドは Event オブジェクトを受けとるので、
ひとつ引数を受けとるようにしておきます。
"""




print("--- すらぷろ　Python STAND ---")
print("--- [Python/tkinter] Combobox を使ってみよう！ ---")


print("--- Combobox を使うための準備 ---")


"""
Combobox ウィジェットは、通常の tkinter ではなく 
tkinter.ttk モジュールに用意されているものになります。
そのため事前に ttk モジュールをインポートする必要があります。
"""
import tkinter.ttk as ttk



print("--- Combobox の生成 ---")


"""
ttk モジュールをインポートしたら次はCombobox リストに
表示させたいリストを作成してみましょう。
まずは、 ttk を利用してCombobox のウィジェットを生成します。


option = ['A', 'B', 'C', 'D']    # 選択肢
variable = tk.StringVar()    # A~Dが文字列の場合
combo = ttk.Combobox(root, values=option, textvariable=variable)
"""
"""
ここで、ウィジェット変数であるA~Dの変数が
「文字列」「整数」「浮動小数点」「Boolean値（True,False）」
なのかによって変数を指定する必要があります。
それぞれ以下のように指定します。



文字列の場合：　
variable = tk.StringVar()

整数の場合：　
variable = tk.IntVar()

浮動小数点の場合：　
variable = tk.DoubleVar()

Boolean値の場合：　
variable = tk.BooleanVar()


ここで ttk.Combobox () の引数は、以下を指定しています。

    root：オブジェクト名の指定
    values：表示させたいリストの指定
    textvariable：Combobox の結果を受け取るための文字列の指定
"""


print("--- Comboboxのオプション一覧 ---")


"""
Combobox で使用できるオプションの一覧を以下の表に示します。

オプション名        指定箇所
height          ドロップダウンリストに表示する高さの指定
width           文字数を指定（横幅）
cursor          カーソルがホバーしている時の形状を指定
justify         テキスト文字列の配置方法（LEFT, CENTER, RIGHT）
postcommand     Comboboxの▼をクリックしたときのコールバック関数を指定
style           カスタムウィジェットスタイルを指定
textvariable    ウィジェット変数の指定
values          リストに表示するデータを指定
font            テキスト文字のフォント、サイズ、太さを指定
state           コンボボックスの状態を指定


オプションの使用例

height
heightoption = ttk.Combobox ( root , height = 2 )

width
widthoption = ttk.Combobox ( root , width = 2)

cursor
cursoroption = ttk.Combobox ( root , cursor = " arrow " )

justify
justifyoption = ttk.Combobox ( root , justify = " center " )

state
stateoption = ttk.Combobox ( root , state = " readonly " )

textvariable
variable = tk.StringVar()
textvariableoption = ttk.Combobox ( root , textvariable = variable )

values
option = ["A", "B", "C", "D"] 
valuesoption = ttk.Combobox ( root , values = option )

font
fontoption = ttk.Combobox ( root , font = ( "MS Gothic" , 16 , "bold" ) )   #boldを指定すると太字になる
"""


print("--- Combobox が選択された際に、値を取得する方法 ---")


"""
combobox オブジェクトのリストから、
選択肢がクリックされた場合に実行したい処理がある場合には
 bind() を使用します。
bind() では、引数を以下のように指定しています。
第一引数では仮想イベントを指定します。
今回用いるイベント　<<ComboboxSelected>>　は、
リストから選択肢が選択された場合にイベントを発生させるものです。
ttk.Combobox で定義されている仮想イベントは 
<<ComboboxSelected>> のみです。
このイベントが行われた際に、
実行したい関数を第二引数であるコールバック関数に記載します。
そうすることでリストから選択された際に、
処理を実行することができるというわけです！

 combo.bind ( " <<ComboboxSelected>> " , コールバック関数 )
"""


print("--- 完成したプログラム ---")


"""
ではCombobox を用いて、リストが選択された際に「○○が選択されました！」
と表示するプログラムを作成してみましょう！
以下のコードを実行してみて下さい。
本プログラムは、main関数を定義しているため
 global 関数として combo = str() を指定しています。
 main 関数を定義しない場合は必要ありません。
"""

import tkinter as tk
from tkinter import *
import tkinter.ttk as ttk


def main():
    global combo
    label1 = tk.Label(root, text='通勤手段を選んでください')
    label1.pack()
    option = ['徒歩', '車', '電車', 'その他']    # 選択肢
    variable = tk.StringVar()
    combo = ttk.Combobox(root, values=option, textvariable=variable)
    combo.bind('<<ComboboxSelected>>', combo_selected)
    combo.pack()

def combo_selected(event):
    global combo
    print(combo.get(), 'が選択されました')

if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('300x100')
    root.title('comboboxのデータ取得')
    combo = str()
    main()
    root.mainloop()

"""
このように combobox が生成されました！
そして上図のように「車」を選択した場合には、
実行結果に「車が選択されました」と表示されていることが分かります。
"""








