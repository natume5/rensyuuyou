#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- 初めてのプログラミング編 モジュールを使ってみよう---")


"""
モジュールとは

これまで1つのPythonファイルでPythonのコードを作ってきましたが実際の開発では
ファイルをいくつかに分割して部品のように扱います。

予め作った外部から呼び出せるPythonのファイルやファイルの塊をモジュールと呼びます。
ライブラリと呼ばれることもあります。モジュールは大きく分けると以下の2つに分類できます。

    標準ライブラリ
    サードーパーティ製ライブラリと独自モジュール

標準ライブラリとは組み込みモジュールとも呼ばれ、
Pythonをインストールすると一緒に同梱されているモジュールのことです。

また、標準ライブラリ以外に自分でモジュールを作成することも可能で
サードーパーティ製ライブラリと呼ばれます。
インストールや適切な場所に配置する必要があります。
特に自分で作成したものを独自モジュールや自作モジュールと呼ぶ場合があります。

この講座では予め用意されたモジュールの使用方法について解説します。
独自モジュールの作成方法は入門編を参照してください。

モジュールの例 mathモジュール

さっそくモジュールを使ってみましょう。
モジュールの使用方法を具体的な例として標準ライブラリのmathモジュールを使用して解説します。

モジュールを使用する場合はimport文を使用します。
またモジュールには関数や定数、固有の型などが含まれており、
呼び出す場合はドットでつなげて呼び出します。

例えば以下のコードではmathモジュールをインポートし、mathモジュールに含まれているpi（円周率）
の定数をprint出力しています。
"""

import math

print(math.pi)    # 3.141592653689793

"""
また、piだけ使用したい場合は以下のようにfromを使用した書き方でpiのみインポートすることも可能です。
"""

from math import pi

print(pi)    # 3.141592653689793

"""
さらに使ってみましょう。mathモジュールには、上記の定数以外にも
三角関数、指数関数、対数関数等、様々な数学計算の関数が用意されています。

定数
pi 	            円周率
e 	            自然対数の底

関数
sin(x) 	        ラジアンxの正弦
cos(x) 	        ラジアンxの余弦
tan(x) 	        ラジアンxの正接
pow(x, y) 	    xのy乗
exp(x) 	        自然対数の底としたeのx乗
log(x) 	        xの10を底とした対数(常用対数)
log(x, base) 	xのbaseを底とした対数(常用対数)
log10(x) 	    xの10を底とした対数(常用対数)

例えば、1/2πの正弦を求める場合、以下のように記述します。
"""

# import math

x = math.pi / 2
y = math.sin(x)
print(y)    # 1.0

"""
もしこれらの関数を自分でコーディングしようとするとよほどスキルの高い人でない限り非常に大変ですが、
Pythonを使用するとモジュールの助けによりこういった複雑な処理がわずか数行で書けてしまうという点が
大きな利便性となっています。

学習されている方には
「なるべく自分でコードを書かないで利用できるライブラリがないかを常に探すようにする」
という点を心に留めていただきたいと思います。


演習

それでは演習です。モジュールを使用したコードを書いてみましょう。
演習1

mathモジュールをインポートし、自然対数の底をprint出力してください。
"""

# import math

print(math.e)    # 2.718281828459045

"""
演習2

mathモジュールの定数piを使用して、半径3の円の円周と面積をそれぞれ求めてprint出力してください。
"""

# import math

# r=半径
r = 3

# 直径R = 半径 * 2
R = 3 * 2

# 円周C = 直径R * 円周率
C = R * math.pi
print(C)    # 18.84955592153876

# 面積S = 半径r * 半径r * 円周率
S = r * r * math.pi
print(S)    # 28.274333882308138


print("--- 初めてのプログラミング編 GUIに挑戦してみよう---")


"""
基礎編での文法や構文に関する説明は前回で終わりです。
ここからはいくつかのPythonのライブラリを使ってコードを動かしてます。
少し長めのコードが多いですが細かいことにこだわらず、
コピーペーストで動かしてみて雰囲気を掴みましょう。

簡単なGUI

Pythonの標準ライブラリにはGUIを作成するtkinterというモジュールが含まれています。
以下のコードをコピー&ペーストして実行してみてください。
"""

import tkinter as tk

root = tk.Tk()
my_label = tk.Label(text='TKinter Sample')
my_label.pack()
root.mainloop()

"""
最大化、最小化、ドラッグアンドドロップによるウィンドウサイズの変更、
ウィンドウを閉じるといった最低限の操作が可能です。
Pythonで複雑なGUIアプリを作成することは難しいのですが、
簡単なものであればtkinterで作成することが可能です。
"""


"""
BMI計算ツール

tk.Tk()でウィンドウを構成するオブジェクトが生成されます。
また、tk.Labelを使用するとラベルを表示することができます。

それ以外にもtk.Entryで入力欄、tk.Buttonでボタンを使用することができます。
また、tk.StringVarで画面上の出力を変えることもできます。
これらを使用してもう少し複雑なサンプル、BMI計算ツールを作ってみましょう。
BMIの計算式はBMI(kg/㎡)＝ 体重(kg) ÷ 身長(m) ÷ 身長(m）で与えられます。
"""

# import tkinter as tk

root = tk.Tk()
root.title("BMI計算ツール")
root.geometry('250x150')

# 体重入力欄
weight_label = tk.Label(text='体重')
weight_label.pack()
weight_entry = tk.Entry(justify='right')
weight_entry.pack()

# 身長入力欄
height_label = tk.Label(text='身長')
height_label.pack()
height_entry = tk.Entry(justify='right')
height_entry.pack()

# 計算結果
bmi_label = tk.Label(text='BMI計算結果')
bmi_label.pack()

bmi_result = tk.StringVar()
bmi_label = tk.Label(text='', textvariable=bmi_result)
bmi_label.pack()


def calc_bmi():
    """ BMI 計算 """
    weight = int(weight_entry.get())
    height = int(weight_entry.get()) / 100
    bmi = weight / (height * height)

    global bmi_result
    bmi_result.set(str(bmi))


# 計算ボタン
button = tk.Button(text='計算', command=calc_bmi)
button.pack()

# メインループ開始
root.mainloop()

"""
今回は雰囲気を掴むためのプログラミングなので細かい解説は割愛しますが、
Pythonの学習を続けるとコードが理解できるようになるはずです。

ところで、プログラミング上達のコツとして、既存のコードを自分で改変してみる、というものが挙げられます。
頭の体操がてら次の演習にチャレンジしてみてください。
"""


"""
演習

先程のBMIのアプリを改造して、平方根を計算する以下のようなアプリを作成してください。
"""

# import math
# import tkinter as tk

root = tk.Tk()
root.title("平方根を求めるツール")
root.geometry('200x100')

# 入力欄
num_label = tk.Label(text='平方根を求める数')
num_label.pack()
num_entry = tk.Entry(justify='right')
num_entry.pack()

# 計算結果
ans_label = tk.Label(text='平方根計算結果')
ans_label.pack()

result = tk.StringVar()
num_sqrt_label = tk.Label(text='', textvariable=result)
num_sqrt_label.pack()


def calc_sqrt():
    num = int(num_entry.get())
    num_sqrt = math.sqrt(num)
    result.set(str(num_sqrt))


button = tk.Button(text='計算', command=calc_sqrt)
button.pack()

root.mainloop()


print("--- 初めてのプログラミング編 turtle グラフィックスに挑戦してみよう---")


"""
タートルグラフィックス

Pythonには標準でturtle(タートル)と呼ばれる
プログラミング学習用のグラフィックライブラリが用意されています。
turtleで簡単なグラフィックに挑戦してみましょう。

まずは以下のコードを動かしてみてください。
"""

import turtle

t = turtle.Turtle()
t.right(90)
t.forward(100)
t.left(90)
t.backward(100)



"""
コードの解説は後ほどします。
2本線が引かれただけのものですが、
学習をすすめると以下のような複雑なグラフィックが簡単に描画できるようになります。


Pythonの対話モード

なお、turtleを使用する場合、対話モードで実行したほうが楽かもしれません。
Pythonの実行方法には2種類あります。1つめはこれまで練習してきたとおり、
Pythonスクリプトファイルを実行する方法です。もう1つはpythonコマンドによる対話モードによる実行です。

コマンドラインでpythonと打ち込んでみてください。以下のように対話モードが開始されます。
「>>>」の後ろに任意のPythonコードを入力することが可能です。

また、終了する際は「quit()」と入力します。コードの動作がよくわからなくなってきた場合は
一旦終了して最初から開始することをおすすめします。

対話モードはスクリプトを書かずにPythonの動作を確認することができ、非常に便利ですが、
抵抗がある方はこれまで通りスクリプトを作成しても構いません。

以降のコードでturtleを使用したコードを対話モードではなく従来どおりスクリプトで実行する場合、
以下のコードを末尾に付加するようにしてください。

turtle.done()
"""


"""
turtleの基本的な使い方

turtleの基本的な使い方

turtleは基本的に、以下のフローで使用することになります。

    turtleをインポートする
    turtleオブジェクトを生成する
    turtleオブジェクトのメソッドを順次使用して描画する

少し難しく書いているため最初の例と併せて説明します。
turtleをインポートとは、以下の通りimport文を使用します。

import turtle

turtleオブジェクトを生成とは、以下の通りturtle()を使用することを指しています。

t = turtle.Turtle()

メソッドを順次使用して描画、とは以下のように「t.メソッド(引数)」を羅列していくことを指しています。

t.right(90)
t.forward(100)
t.left(90)
t.backward(100)

上のコードの意味についてより細かく説明します。

t.rignt(90)で右回りに90度回転させています。
初期状態がx軸方向に0度なので、右回りに90度回転させると下向きになります。

t.forward(100)で長さ100だけ線を引いています。
t.leftで90度左回りに回転、さらにt.backward(100)で
向いた方向と逆向きに長さ100だけ線を引いています。
"""
"""
turtleの基本的なメソッド

基本的なメソッドには以下のようなものがあります。
覚える必要はなく、必要に応じて参照するようにしましょう。
method                        意味
pendown()            ペンを下ろす（動くと線が引かれる）
penup()              ペンをあげる（動いても線が引かれない）
forward(距離)        現在の方向に引数で指定した距離進む
home()               原点(0, 0)に移動し開始時の方向に向ける
right(角度)          引数で指定した角度だけ右に回転する
left(角度)           引数で指定した角度だけ左に回転する
setposition(x, y)    引数で指定した位置 (x, y) に移動する
speed(1～10)         スピードを 1 から 10 までの範囲の整数に設定する
pencolor(色)         ペンの色を指定した色に設定する
pensize(太さ)         ペンの太さを指定したサイズに設定する

その他にも色々あるのですが、興味がある方は以下のリンクを参照してください。

turtle --- タートルグラフィックス


星型を描いてみよう

では、以上の基本的な使用方法を踏まえて星型を描いてみましょう。
星型の1つの角の角度は36度なので回転角に144度を指定します。
"""

from turtle import *

forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)
right(144)
forward(100)


"""
実行すると星型が描画されます。

このコード、同じ処理が5回も繰り返されていますね。どうすれば良いでしょうか？少し考えてみてください。

以前学習したfor文を使用すると、以下のように書き換えることができます。
"""

# import turtle

t = turtle.Turtle()
for i in range(5):
    t.forward(100)
    t.right(144)


"""
演習

先程のコードを改変して、以下のような複雑な星型を出力してみましょう。
（ヒント：繰り返し回数を増やし、繰り返し処理時に長さを少しずつ変えています。）
"""

import turtle

t = turtle.Turtle()
t.speed(10)

for i in range(25):
    t.forward(100 + 5 * i)
    t.right(144)

"""
補足 色を変えてみる

最後に、遊びとして補足です。pencolorメソッドでペンの色を指定することが可能です。
事前にturtle.colormode(255)を指定するとr, g, bを数値で指定することが可能となります。
先程のコードでfor文中で色コードを少しずつ変え、
繰り返し回数を増やすと序盤に紹介したグラデーションの星型を描画することができます。
"""

import turtle

turtle.colormode(255)

t = turtle.Turtle()
t.speed(10)
for i in range(50):
    r = 255 - i * 2
    g = i * 2
    b = 128 + i * 2
    t.pencolor(r, g, b)
    t.forward(100 + 5 * i)
    t.right(144)

turtle.done()

