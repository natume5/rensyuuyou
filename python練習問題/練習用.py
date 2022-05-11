#!/usr/bin/python
# -*- coding: Shift-JIS -*-
# Magic comment


import calendar
import math
import matplotlib.pyplot as plt


print(1 + 1) 
1 + 1

x_values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June']
y_values = [100, 130, 80, 150, 140, 130]

plt.bar(x_values, y_values)
plt.plot()


plt.show()

print(100 * 55 + 40 * 8)
print((100 * 5) + (40 * 8))
print(10 * 20)
print(5 % 3)
print(10 % 2)
print(-100)
print(100 + -99)
print(100 + (-99))
print(10 ** 3)


# 実数(float型)
0.1
100.0

# 整数とfloat型
(10 + 20)
(10 + 10.0)
(2 / 3)
(3 / 3)

# 整数除算
(3 / 2)
(3 // 2)
(3.0 // 2.0)
print((100 * 5) + (40 * 8) + (80 * 5) + (60 * 10) + (90 * 20) + (110 * 10))

# 変数と代入文
variable = 50
print(50 + 1)
variable = 50
print(variable + 1)
momo = 100 * 5
mikan = 40 * 8
nashi = 80 * 5
kiwi = 60 * 10
suika = 90 * 20
kaki = 110 * 10
goukei = momo + mikan + nashi + kiwi + suika + kaki
print(goukei)

# 変数名
variable = 1
variable_123 = 1
# 123_variable → NG (数字で始まっている)
# vari＄able → NG (記号は変数名として使えない)
# raise → NG (「raise」という単語はpythonで特別な意味を持つので使えない)
print(1 + 2) # ここはコメント
# この行はまるまるコメントです

# 引数
abs(-200)

# 戻り値

# 関数と演算子
a = abs(100 + 200) / 2   # 150.0
print(a)

# 関数と変数
minus_value = 100 * -1
abs(minus_value)    # 100

abs(100 * -1)    # 100 * -1 = -100

abs_value = abs(10)    # 20
print(abs_value * 2)    # abs(10) * 2 と同じ 20

# 関数の列
# abs()関数
abs(100)    # 100

abs(100 * -1)    # -100

# round()関数
# round(数値, 有効桁数)
round(1.12, 1)    # 1.1

# mini()関数とmax()関数
min(10, 20, 5, 30)    # 5
min(4, 8, 2, 20, 5, 6, 2, 9)    # 2
max(10, 20, 5, 30)    # 30

# import文
# import モジュール名
# import math    # mathモジュールを使用する
# モジュール名.関数名()
# import math
math.sqrt(2.0)

# import calendar    # calendarモジュールを使用する
calendar.prmonth(2020, 12)    # 2020年の12月のカレンダーを表示する


# 文字列
print(123)
print(456)
print("Python Programming!")
print('Python Programming!')


# 文字と数字の違い
print(123 * 456)    # 56088
# "123" * "456"    # エラー


# print関数
print(42)    # 42
print(1, 2, 3)    # 1 2 3

# 文字列とprint()関数
print("もも5つと、みかん8つで", 100 * 5 + 40 * 8, "円になります。")
# もも5つと、みかん8つで820円になります。


# input()関数
input("好きな文字を入力してください")
string = input("文字列を入力してください:")
print("文字列", string, "が入力されました。")


# 文字列の演算子と数値
print(123 + 456)
print("123" + "456")
# 123 + "456"    数値と文字列を足すとエラーになり、加算することはできない。

# 文字列の数値化
text = "123"
print(int(text))

text1 = "123"
text2 = "456"
print(text1, "と", text2, "を足すと", int(text1) + int(text2), "になります。")

text = "123.4"
float(text)
# int("Hello")    数値以外の文字は、数値にはできない。エラーになる。

# 数値の文字列化
num = 123
str(num)    # "123"
height = 172    # heightに172を代入する
print("私の身長は" + str(height) + "cmです。")


# メゾット
text = "Lower Letters"     # 変数textに文字列"Lower Letters"を代入
uppered_text = text.upper()    # upper()メゾットで大文字を作成
print(uppered_text)    # LOWER LETTERS
# メゾットの呼び出し方　データ.メゾット名(引数1, 引数2, 引数3....)

# 文字列のfindメゾット
text = "The shells she sells are sea-shells, I'm sure."
text.find("sea")    # 25

# メゾットと関数
# メゾットとデータ
# data = 10000
# data.upper()    エラー 数字に大文字も小文字もない

data = 0.5
data.as_integer_ratio()    # (1, 2)

# data = "abracadabra"
# data.as_integer_ratio()    # 数値データ専用メゾットで、文字列データを使おうとするとエラーになる

# 練習問題
text = input("何か入力して下さい。")    # 変数textに文字を入力
lower_text = text.lower()    # 入力した文字列を小文字に変換
print(text, "を小文字に変換すると", lower_text, "になります。")


# 比較演算子
100 > 10    # True
10 > 100    # False
10 < 100    # True　10は100より小さい
100 < 100    # False　100は100以上
10 <= 100    # True 　10は100
100 <= 100    # True　100は100と等しい
100 == 100    # True　100は100と等しい
99 == 100    # False  99と100は等しくない
99 != 100     # True  99と100は等しくない
100 != 100    # False  100は100と等しい

# 文字列の比較
"123" < "456"     # True
"python" < "Python"    # True
"Python-1" < "Pthon-a"    # True


# if文による条件分岐
a = 100    # 変数aに100を設定する

if a == 100:    # aが100と等しければ、print()関数を実行する
	print("100点満点！")

# if文の書き方
"""if a == 100:
    処理1
    処理2
    処理3
^^^^
スペースを4文字入力
"""

# 条件式がFalseとなる場合
a = 99    # 変数aに99を設定する

if a == 100:    # aが100と等しければ、print関数を実行
	print("100点満点！")

# else節
"""
if 条件式:
	処理1
	処理2
	・・・
else:
	処理3
	処理4
	・・・
"""

a = 100    # 変数aに100を設定する

if a == 100:    # aが100と等しければ、print()関数を実行
	print("100点満点！")
else:
	print("失格！")


a == 0
if a == 100:
	print("100点満点！")
else:
	print("失格！")


# 比較以外の条件式
print("123は数字ですか？", "123".isdecimal())
print("abcは数字ですか？", "abc".isdecimal())


string = input("文字列を入力して下さい。:")
if string.isdecimal():
	print(string, "は数字です。")
else:
	print(string, "は数字ではありません。")


# elif節
print("123はアルファベットですか？", "123".isalpha())
print("abcはアルファベットですか？", "abc".isalpha())
# isalpha()メゾットはアルファベットだけでなく、ひらがなやカタカナもアルファベットとして判定する。


"""
if 条件式1:
	処理1
	・・・
elif 条件式2:
	処理2
	・・・
elif 条件式3:
	処理3
	・・・
else:
	処理n
	・・・
"""


string = input("文字を入力して下さい。:")

if string.isdecimal():
	print(string, "は数字です。")
elif string.isalpha():
	print(string, "はアルファベットです。")
# isalpha()メゾットはアルファベットだけでなく、ひらがなやカタカナもアルファベットとして判定する。
else:
	print(string, "は数字でもアルファベットでもありません。")


# ブール型と論理演算子
print(1 > 2)
print("abc" == "abc")

true_value = True
print("true_value は", true_value)

false_value = False
print("false_value は", false_value)


# and演算子
age = 11    # 例として、11歳 身長130cmとする
height = 130

if (10 <= age) and (120 <= height):
	print("お乗りいただけます")
else:
	print("ご遠慮ください。")


age = 11    # 例として、11歳 身長110cmとする
height = 110    # この行を130から110cmに変更

if (10 <= age) and (120 <= height):
	print("お乗りいただけます")
else:
	print("ご遠慮ください。")


# 論理積
# or演算子
age = int(input("年齢を入力して下さい。:"))    # 年齢を90歳とする

if (age <= 10) or (80 <= age):
	print("10歳以下の方と80歳以上の方はご遠慮ください")
else:
	print("お乗りいただけます。")


# 論理和
# C = A or B
# not演算子
# not (age < 10)
age = 20    # 年齢は20

if not (age < 10):
	print("お乗りいただけます")
