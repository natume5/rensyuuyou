# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
●例題５－５
for(while)文の中にfor(while)文を書くこともできる．
 これは反復（ループ）の入れ子と呼ばれる．
Pythonでは，字下げ（インデント）が重要なので，構文は以下のようになる．
for x in range(初期値，終了値，ステップ)：

　　for y in range(初期値，終了値，ステップ)：

　　　　繰り返したい文

while文でも同様である．

例題：

1から5までの整数 xxx と 8 から16までの整数 yyy の和の表を作成せよ．

以下のような出力を得たいのだが， print()関数で出力すると，自動的に改行されてしまう．

9 10 11 12 13 14 15 16 17

10 11 12 13 14 15 16 17 18

11 12 13 14 15 16 17 18 19

12 13 14 15 16 17 18 19 20

13 14 15 16 17 18 19 20 21

改行しないで（かつ空白を入れて）出力したいときには，
print(出力したい数, end=' ') と書く． これは，end= の後に書いた文字が，
改行コードの代わりに，出力に付加されることを表す．
すると全部つながって

9 10 11 12 13 14 15 16 17 10 11 12 13 14 15 16 17 18
 11 12 13 14 15 16 17 18 19 12 13 14 15 16 17 18 19
  20 13 14 15 16 17 18 19 20 21

と出力されてしまうので，
内側のforループが終わったあとに print() と改行を行うための出力をいれる．

for x in range(1, 6):
    for y in range(8, 17):
        print(x+y, end=' ')
    print()

9 10 11 12 13 14 15 16 17
10 11 12 13 14 15 16 17 18
11 12 13 14 15 16 17 18 19
12 13 14 15 16 17 18 19 20
13 14 15 16 17 18 19 20 21
"""


for x in range(1, 6):
    for y in range(8, 17):
        print(x + y, end=' ')
    print(str.rjust)
