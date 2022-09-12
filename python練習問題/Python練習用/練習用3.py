#!/usr/bin/python
# -*- coding: UTF-8 -*-

# continueの例
counter = 1    # 現在、何回目かを記録する変数

while counter <= 10:
	text = input("なにか数値を入力してください")

	# if 入力された文字が''なら
	if text == '':
		print("入力が無効です。何か数値を入力してください。")
		# ループの先頭に戻る。
		continue

	# 入力された文字が'999'なら
	if text == '999':
		# ループを中断する
		print("中断します。")
		break

	number = int(text)    # 入力した文字列を数値に変換する
	print(counter, "回目:", number * number)     # 入力した数値の2乗を表示する
	counter = counter + 1    # counterの値に1加算する

print("終了しました。")


# 関数の定義
momo = input("桃は何個買いますか？桃は1個100円です。")    # 桃の個数を入力
num_momo = int(momo)    # 入力した文字列を、整数に変換

mikan = input("みかんは何個買いますか？みかんは1個40円です。")    # みかんの個数を入力
num_mikan = int(mikan)    # 入力した文字列を、整数に変換

total_momo = num_momo * 100
total_mikan = num_mikan * 40
total = total_momo + total_mikan

print("桃", num_momo, "個と、みかん", num_mikan, "個で、", total, "円です。")


# 独自に関数を作る
abs(-100)    # 100
# 関数の定義
"""
def 関数名(引数1, 引数2, ・・・):    # def=define(定義)
	処理1
	処理2
	・・・
"""
"""
def fruit_price(number_of_momo, number_of_mikan):
	・・・
"""


# 関数本体
"""
def 関数名(引数1, 引数2, ・・・):
	処理
^^^^
スペースを4文字入力
"""
"""
def fruit_price(number_of_momo, number_of_mikan):
	total__momo = number_of_momo * 100
"""
"""
def fruit_price(number_of_momo, number_of_mikan):
	total_momo = number_of_momo * 100
	total_mikan = number_of_mikan * 40
"""
"""
def fruit_price(number_of_momo, number_of_mikan):
	total_momo = number_of_momo * 100
	total_mikan = number_of_mikan * 40
	total = total_momo + tota_mikan
"""

# 関数の戻り値
"""
def fruit_price(number_of_momo, number_of_mikan):
	total_momo = number_of_momo * 100
	total_mikan = number_of_mikan * 40
	total = total_momo + tota_mikan

fruit_price(10, 20)
"""

# return文
"""
def fruit_price(number_of_momo, number_of_mikan):
	# 桃とみかんの合計金額を計算する
	total_momo = number_of_momo * 100
	total_mikan = number_of_mikan * 40
	total = total_momo + tota_mikan

	return total	
"""

# 関数の呼び出し
# 関数の定義
def fruit_price(number_of_momo, number_of_mikan):
	# 桃とみかんの合計金額を計算する
	total_momo = number_of_momo * 100
	total_mikan = number_of_mikan * 40
	total = total_momo + total_mikan

	return total


# 桃5個、みかん10個の値段を計算
total = fruit_price(5, 10)
print("桃5個と,みかん10個で", total, "円です。")


def fruit_price(number_of_momo, number_of_mikan):
	# 桃とみかんの合計金額を計算する
	total_momo = number_of_momo * 100
	total_mikan = number_of_mikan * 40
	total = total_momo + total_mikan

	return total


# 桃5個、みかん10個の値段を計算
total = fruit_price(100, 200)
print("桃100個と,みかん200個で", total, "円です。")


# ローカル変数とグローバル変数
"""
def fruit_price(number_of_momo, number_of_mikan):
	total_momo = number_of_momo * 200    # total_momoはローカル変数
	total_mikan = number_of_mikan * 40    # total_mikanはローカル変数
	total = total_momo + total_mikan    # totalはローカル変数
"""

# グローバル変数
"""
ローカル変数以外の、関数の外部で代入された変数は、全てグローバル変数になる。
関数の定義では、こんなプログラムを書きました。
momo = input("桃は何個買いますか？")     # ももの個数を入力する
num_momo = int(momo)    # 入力した文字列を、整数値に変換する
ここで、変数momoやnum_momoは、関数の内部ではなく、関数の外部で代入されていますので、
全てグローバル変数になる。
"""

# 関数とグローバル変数
# global_value はグローバル変数
global_value = 100

def test_global(arg):
	# ローカル変数argとグローバル変数global_valueの積
	return arg * global_value

print(test_global(10))    # 10 * 100


global_value = 200

def test_global(arg):
	# ローカル変数argとグローバル変数global_valueの積
	return arg * global_value

print(test_global(10))    # 10 * 200


# モジュールスコープとローカルスコープ
"""
Pythonプログラムのうち、関数以外の部分は、モジュールスコープと言います。
逆に、関数内の部分を、ローカルスコープと言います。
モジュールスコープで代入された変数はグローバル変数となり、
ローカルスコープで代入された変数はローカル変数になる。
"""
def func1(name):
	print("Hello", name, "this is func1.")

def func2():
	func1("func2")

func2()


import time

def print_time():
	# モジュールスコープでimportしたtimeモジュールを利用
	now = time.asctime()
	print("It is", now)

print_time()
