#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 否定
# B = not A
# while文によるループ
# while文
"""
while 条件式1:
	処理1
	処理2
	処理3
	・・・
"""

# while文の例
text = ""    # textに初期値として""を設定する

while text != "finish":    # textが"finish"ではない間、処理を繰り返す
	# 文字を入力する
	text = input("finishと入力して下さい。:")    # textに文字を読み込む
	print(text, "と入力されました。")


print("終了しました。")


# ループが止まらなくなってしまったら
"""
while True:
    text = input()
    print(text)
"""


# break文による中断

counter = 1    # 現在 何回目かを記録する変数

while counter <= 5:    # counterの値が5いかなら繰り返す
	text = input("数字を入力してください:")
	number = int(text)    # 入力した文字列を数値に変換
	print(counter, "回目", number * number)    # 入力した数値の2乗を表示
	counter = counter + 1    # counterの値に1加算する


print("終了しました")


# ループ途中での脱出

counter = 1    # 現在、何回目かを記録する変数

while counter <= 5:    # counterの値が5以下なら繰り返す
    text = int(input("数字を入力して下さい。"))

    # 入力された文字が'999'なら
    if text == '999':
        # ループを中断する
        print("中断します。")
        break
    
    number = int(text)    # 入力した文字列を数値に変換する
    print(counter, "回目:", number * number)    # 入力した数値の2乗を表示する
    counter = counter + 1    # counterの値に1加算する


print("終了しました。")


# 代入文と等号
B = 200    # Bを200に設定
A = B + 3    # Aの値をB + 3 = 200に設定
print(A)

B = 300
print(A)

A = B + 3    # 新しいBの値(=300)で、もう一度Aを代入する
print(A)


# AはA+1と等しい？？？
A = 1000
A = A + 1
A = A + 1
A = A + 1
A = A + 1
# A = A + 1という代入文を実行すると、その度にAの値は1づつ増加するので、Aの値は1004になる。


# continue文
i = 0
while i < 10:
	i = i + 1

	if (i % 2) == 1:    # iを2で割った余りが1の時
		continue

	print(i, 'is even.')    # 値を出力
