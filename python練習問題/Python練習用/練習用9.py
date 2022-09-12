#!/usr/bin/python
# -*- coding: UTF-8 -*-


import random
import math


# 関数を活用する
"""
これまで、この講座のサンプルプログラムは、「スイカ割りゲーム」も含め、
あまり 関数 を定義せず、単純にプログラムを記述していました。

本来、これはあまり望ましいことではありません。ここでは、スイカ割りゲームをさらに リファクタリングし、
プログラムを関数に分割してみましょう。

現在、スイカ割りゲームはこんな感じになっています。

import random
import math

BOARD_SIZE = 5  # ボードの初期サイズ

def calc_distance(pos1, pos2):
    # ２点間の距離を求める
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)


suika_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))  # スイカの位置
player_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE)) # プレイヤーの位置

# スイカとプレイヤーの位置が異なる間、処理を繰り返す
while (suika_pos != player_pos):

    # スイカとプレイヤーの距離を表示する
    distance = calc_distance(suika_pos, player_pos)
    print("スイカへの距離:", distance)

    # キー入力に応じて、プレイヤーを移動する
    c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
    current_x, current_y = player_pos

    if c == "n":
        current_y = current_y - 1
    elif c == "s":
        current_y = current_y + 1
    elif c == "w":
        current_x = current_x - 1
    elif c == "e":
        current_x = current_x + 1

    player_pos = (current_x, current_y)

print("スイカを割りました！")
"""


# 初期位置の作成
"""
元のプログラムでは、スイカとプレイヤーの初期位置を次のように生成しています。

suika_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))  # スイカの位置
player_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE)) # プレイヤーの位置

この処理では、

(random.randrange(0, 5), random.randrange(0, 5))

という、全く同じ式でタプルを作成しています。同じことを2度書くのは無駄ですし、
将来、この部分を修正する時のミスの元にもなります。
また、(random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE)) 
のような式の羅列だけでは、どんなことをやっているのか、わかりにくいです。

そこで、この処理は、指定した範囲で座標を生成する 関数 として定義してしまいましょう。

座標を生成する関数は generate_position という名前にします。
生成する座標の範囲は、size という名前の 引数 で指定できるようにしましょう。


def generate_position(size):
    # 0以上size未満の範囲で、x座標とy座標を生成する
    x = random.randrange(0, size)  # x座標
    y = random.randrange(0, size)  # y座標
    
    return (x, y)

generate_position(3)  # (0, 0)~(2, 2) の範囲で座標を生成
generate_position(100)  # (0, 0)~(99, 99) の範囲で座標を生成


関数 generate_position(size) を呼び出すと、
指定した 0 から size-1 までの範囲でx座標とy座標を生成し、結果をタプルとして返します。
いろいろな値を size に指定して、実際に呼び出してみましょう。


関数を定義しておけば、こんなふうに手軽に呼び出して、関数がちゃんと書けているか試せるのでとても便利です。

generate_position(size) を使うと、さきほどの

suika_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE))  # スイカの位置
player_pos = (random.randrange(0, BOARD_SIZE), random.randrange(0, BOARD_SIZE)) # プレイヤーの位置

の部分は、次のように書き換えられます。

suika_pos = generate_position(BOARD_SIZE)  # スイカの位置
player_pos = generate_position(BOARD_SIZE) # プレイヤーの位置

関数を利用して処理を行うことで、スイカとプレイヤーで同じ処理を2度書くのではなく、
どちらの座標も generate_position(size) を利用して設定できるようになりました。

このように、関数を利用すると、

    無駄な繰り返しを避ける
    generate_position というわかりやすい関数名がついているので、何を行っているのかすぐに理解できる

などのメソットがあります。
"""


# プレイヤーの移動処理
"""
ゲームのループ処理の中では、次のようにキー入力を受け取り、入力に応じてプレイヤーの位置を移動しています。

# キー入力に応じて、プレイヤーを移動する
c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
if c == "n":
    player_y = player_y - 1
elif c == "s":
    player_y = player_y + 1
elif c == "w":
    player_x = player_x - 1
elif c == "e":
    player_x = player_x + 1

この、入力文字に応じてプレイヤーを移動させる部分、けっこう処理が長くて、
ループの中に入ってると読みにくくて邪魔ですね。ここも、関数にしてしまいましょう。

プレイヤーの座標を移動させる関数は、次のように書けます。関数名は move_position としましょう。

def move_position(direction, pos):
    # direction にしたがって、posを移動する
    
    current_x, current_y = pos
    
    if direction == "n":
        current_y = current_y - 1
    elif direction == "s":
        current_y = current_y + 1
    elif direction == "w":
        current_x = current_x - 1
    elif direction == "e":
        current_x = current_x + 1

    return (current_x, current_y)

関数 move_position(direction, pos) は引数として direction と pos を指定します。
direction は、移動方向を指示する文字を指定し、pos には現在の位置を示すタプルを指定します。

pos から direction にしたがって移動した座標のタプルが、関数の戻り値となります。

引数と現在位置を指定して、実際に呼び出してみましょう。

move_position('n', (1, 1)) # (1, 1) から、北に移動

(1, 0)

move_position('e', (3, 4)) # (3, 4) から、東に移動

(4, 4)
"""


# スイカ割りゲーム全体を関数化
"""
ここまでの修正をまとめると、次のようになります
"""


print("スイカ割ゲーム！")
BOARD_SIZE = 5    # ボードの初期サイズ

def generate_position(size):
    # 0以上size未満の範囲で、x座標とy座標を生成する
    x = random.randrange(0, size)    # x座標
    y = random.randrange(0, size)    # y座標

    return(x, y)

def calc_distance(pos1, pos2):
    # 2点間の距離を求める
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]

    return math.sqrt(diff_x**2 + diff_y**2)

def move_position(direction, pos):
    # direction にしたがって、posを移動する

    current_x, current_y = pos

    if direction == "n":
        current_y = current_y - 1
    elif direction == "s":
        current_y = current_y + 1
    elif direction == "w":
        current_x = current_x - 1
    elif direction == "e":
        current_x = current_x + 1

    return (current_x, current_y)

suika_pos = generate_position(BOARD_SIZE)    # スイカの座標
player_pos = generate_position(BOARD_SIZE)    # プレイヤーの座標

# スイカとプレイヤーの位置が異なる間、処理を繰り返す
while (suika_pos != player_pos):

    # スイカとプレイヤーの距離を表示する
    distance = calc_distance(player_pos, suika_pos)
    print("スイカの距離:", distance)

    # キー入力に応じて、プレイヤーを移動する
    c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
    player_pos = move_position(c, player_pos)

print("スイカを割りました！")


"""
スイカ割りゲームを構成する機能が関数として独立し、プログラムの全体の実行の流れが明確になり、
どの部分がどんな役割をは果たしているのか、簡単にわかるようになりました。

ゲームを構成する部品は関数化しましたが、ゲーム本体はまだ関数となっていません。
ここもすべて関数にしてしまいましょう。関数名は suika_wari とします。
"""

BOARD_SIZE = 5  # ボードの初期サイズ


print("スイカ割ゲーム！その2！！")
def generate_position(size):
    # 0以上size未満の範囲で、x座標とy座標を生成する
    x = random.randrange(0, size)  # x座標
    y = random.randrange(0, size)  # y座標
    
    return (x, y)

def calc_distance(pos1, pos2):
    # ２点間の距離を求める
    diff_x = pos1[0] - pos2[0]
    diff_y = pos1[1] - pos2[1]
    
    return math.sqrt(diff_x**2 + diff_y**2)

def move_position(direction, pos):
    # direction にしたがって、posを移動する
    
    current_x, current_y = pos
    
    if direction == "n":
        current_y = current_y - 1
    elif direction == "s":
        current_y = current_y + 1
    elif direction == "w":
        current_x = current_x - 1
    elif direction == "e":
        current_x = current_x + 1

    return (current_x, current_y)


def suika_wari():
    suika_pos = generate_position(BOARD_SIZE)  # スイカの座標
    player_pos = generate_position(BOARD_SIZE) # プレイヤーの座標

    # スイカとプレイヤーの位置が異なる間、処理を繰り返す
    while (suika_pos != player_pos):

        # スイカとプレイヤーの距離を表示する
        distance = calc_distance(player_pos, suika_pos)
        print("スイカへの距離:", distance)

        # キー入力に応じて、プレイヤーを移動する
        c = input("n:北に移動 s:南に移動 e:東に移動 w:西に移動")
        player_pos = move_position(c, player_pos)

    print("スイカを割りました！")




