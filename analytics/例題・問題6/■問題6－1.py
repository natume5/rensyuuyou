# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題6－1
(1)　10個の数字を入力する反復の中で，
前回入力した数より倍以上大きな数を入力したら終了するようなプログラムを作りなさい．

(2)　10個の数字を入力する反復の中で，
前回入力した負の数と同じ数を入力したら終了するようにしましょう
（1,-1,4,-4,5 と入力した時点では，前回入力した負の数は-4です）．
（ヒント：xが負のときだけ，yにxを代入しましょう．）
"""


# (1)
counter = 10


y = int(input("数値を入力して下さい。"
              "前回入力した数より倍以上大きな数を入力したら終了します。:(1回目):"))


while True:
    try:
        x = int(input("数値を入力して下さい。"
                      "前回入力した数より倍以上大きな数を入力したら終了します。:(2回目):"))
        counter = counter - 1
        y = x
        if counter == 0:
            print("終了します。")
            break
        elif y >= x * 2:
            print("前回入力した数より倍以上の数が入力されたので終了します。")
            break
except KeyboardInterrupt:
    print("終了します。")


# (2)
counter = 10


y = int(input("数値を入力して下さい。"
              "前回入力した負の数と同じ数を入力したら終了します。:(1回目):"))


try:
    while True:
        x = int(input("数値を入力して下さい。"
                      "前回入力した負の数と同じ数を入力したら終了します。:(2回目):"))
        counter = counter - 1
        if counter == 0:
            print("終了します。")
            break
        elif x <= 0:
            x = y
            if y == x:
                print("前回入力した負の数と同じ数が入力されたので終了します。")
                break
except KeyboardInterrupt:
    print("終了します。")

"""
y = int(input("数値を入力して下さい。前回入力した数より倍以上大きな数を入力したら終了します。:(1回目):"))
x = int(input("数値を入力して下さい。前回入力した数より倍以上大きな数を入力したら終了します。:(2回目):"))
x = int(input("数値を入力して下さい。前回入力した数より倍以上大きな数を入力したら終了します。":(3回目):"))
print("前回入力した数より倍以上の数が入力されたので終了します。")

list=[int(x) for x in input().split()]
cnt=0
for i in range(10):
    if list[i]<100:
        cnt+=1
print("100以上の個数は"+str(10-cnt)+"個")
print("100未満の個数は"+str(cnt)+"個")
"""
