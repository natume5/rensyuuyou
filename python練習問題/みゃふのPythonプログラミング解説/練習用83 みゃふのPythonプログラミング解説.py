#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- 関数の応用（関数オブジェクト、クロージャ、ラムダ式） ---")


"""
Pythonを日常的に使っている方でも、クロージャやラムダ式に関してしっかりと熟知している！
と豪語できる方はもしかしたら少ないのではないでしょうか？
これらの技術はうまく使えば高い効力を発揮しますが、
書き方が特殊で直感的に理解しにくいというデメリットもあります。
そこでここでは関数オブジェクトやクロージャ、ラムダ式をわかりやすく解説します。
難しい関数の使い方も利用できるようになりましょう(^^♪
"""


print("--- 関数オブジェクト---")


"""
クロージャやラムダ式の前に、関数オブジェクトについて解説します。
関数は数値や文字列と同じように変数に代入することができる「オブジェクト」というものです。
なので、例えば関数の引数に関数を指定する、といった使い方も可能です。
まずは、関数オブジェクトの基本的な使い方を見ていきましょう。
"""

def hello():
	print('Hello!')

hello_func = hello    # 関数オブジェクト作成
hello_func()    # Hello!

"""
hello()という関数を定義して、それをhello_func変数に代入しています。
このhello_funcが関数オブジェクトです。
関数オブジェクトを使う場合は変数に()をつけることで使えます。


関数に引数がある場合

先ほどの最もシンプルな例では引数のない関数オブジェクトを作成しましたが、
引数がある場合どうなるかを見ていきましょう。
関数オブジェクトの具体的な使い方も同時に解説したいので、
今回は「上野動物園の個人入園料」を計算できる簡易ツールを作ってみました。

このページをを見る限り、一般は600円、65歳以上の方は300円、中学生は200円となっています。
それ以外の方は無料なので今回は除外します。
"""

# 計算
def calc(func, num=1):
	return func(num)

# 一般
def ippan(num):
	return num * 650

# 65歳以上
def older_65(num):
	return num * 300

def middle_student(num):
	return num * 200

group = {'ippan': 2, 'older_65': 2, 'middle_student': 1}

total_price = 0
for people in group:
	total_price += calc(eval(people), group[people])

print(f'合計{total_price}円です。')    # 合計2100円です。

"""
ちょっと長いコードになってしまいましたが、やっていることは複雑ではありません。
上から一つずつ見ていきましょう。

まずはこちら

#計算
def calc(func, num = 1):
    return func(num)

calcという料金を計算する関数です。1つ目の引数に関数オブジェクト、2つ目の引数に人数を渡します。

funcには「一般」「65歳以上」「中学生」のどれかの計算関数が渡される想定です。
この3つの関数は引数を持っているので、func()にnum(人数)を渡しています。
これが引数のある関数オブジェクトの使い方です。

次にこちらの3つの関数

#一般
def ippan(num):
    return num * 650

#65歳以上
def older_65(num):
    return num *  300

#中学生
def middle_student(num):
    return num * 200

それぞれの人に応じて、人数分の料金を計算して返却する関数です。
この関数が先ほどのfuncの1つ目の引数に渡されます。

最後にこちら

group = {
    "ippan" : 2,
    "older_65" : 2,
    "middle_student" : 1
}

total_price = 0
for people in group:
    total_price += calc(eval(people), group[people])

print(f"合計{total_price}円です。")

groupは上野動物園に行った人と人数を表現しています。
今回は一般が2人、65歳以上が2人、中学生が1人です。
total_priceには全員分の合計金額が入ります。
次にforでgroupをループさせながら、total_priceに金額を計上していきます。
ここが最も重要なところですね。
eval()は引数に渡した文字列をPythonの式として評価する関数です。
引数のpeopleにはそれぞれippan、older_65、middle_studentという文字列が入ってくるので、
ループするごとに対応した関数を呼び出しています。
group[people]はgroupの辞書から値(人数)を取得しています。
これをcalc()に渡して料金を計算し、最後にprint()で出力しています。
関数オブジェクトを使うことで、条件に応じて異なる関数を呼び出したり、
関数の引数に関数を使うといった高度なことが可能であることがお分かりいただけたかと思います。
"""


print("--- クロージャ---")


"""
次にクロージャについて解説します。
クロージャとは「関数の中で関数を定義する」ことで、次のように使います。
"""

def enclosure_func(a):
	b = 2
	def closure_func(c):
		return a + b + c
	return closure_func

func = enclosure_func(1)
print(func(3))

"""
結論としては1 + 2 + 3の結果を出力しています。
まずenclosure_funcという関数を引数1つで定義しています。
この関数の中でb変数を初期化しています。
次にclosure_funcという関数を「enclosure_func内で定義しています」。
これがクロージャです（ちなみに外側の関数をエンクロージャと言います）。
closure_funcは a + b + cの結果を返却しています。
ここで重要なのは「関数の外にあるaやbを関数内で使用できる」点です。
クロージャにはこういった特徴があります。
最後に外側の関数がクロージャを返却しています。
次にfuncにenclosure_funcを格納し、関数オブジェクトを作成しています。
最後にfuncに3を渡して結果を出力しています。funcに渡した3はclosure_funcの引数になります

ちなみにクロージャはこのように使うこともできます。

num = enclosure_func(1)(3) #enclosure_func(1)が先に評価される
print(num)

また、クロージャはエンクロージャ内にいくつも作ることができます。
例えば先ほどの上野動物園の個人入園料計算ツールは、次のように書くこともできます。
"""

def calc(people):
	if people == 'ippan':
		def ippan(num):
			return num * 650
		return ippan
	elif people == 'older_65':
		def older_65(num):
			return num * 300
		return older_65
	else:
		def middle_student(num):
			return num * 200
		return middle_student

group = {'ippan': 2, 'older_65': 2, 'middle_student': 1}

total_price = 0
for people in group:
	total_price += calc(people)(group[people])

print(f'合計{total_price}円です。')

"""
calc()は引数のpeopleに応じて返却する関数が変わっています。
先ほどはeval()を使って呼ぶ関数を動的に変更していましたが、
このコードはクロージャを使って似たようなことを表現しています。
"""


print("--- ラムダ式 ---")


"""
最後にラムダ式について解説します。
ラムダ式に関してはこちらの記事で基本的な使い方を紹介しています。

ここではmap()でラムダ式を使ってみましょう。map()はリストなどから要素を1つずつ取り出し、
引数に指定した関数に渡して実行します。
例えば次のコードです。
"""

def convert(n):
	if n % 2 == 0:
		return 0
	else:
		return 1

nums = [16, 35, 21, 2, 51, 9, 0, 11, 98]
conv_nums = list(map(convert, nums))
print(conv_nums)    # [0, 1, 1, 0, 1, 1, 0, 1, 0]

"""
数値をconvert()に渡して、偶数の場合0、奇数の場合1に変換しています。
このconvert()はラムダ式を使って次のように書けます。
"""

nums = [16, 35, 21, 2, 51, 9, 0, 11, 98]
conv_nums = list(map(lambda n: 0 if n % 2 == 0 else 1, nums))
print(conv_nums)    # [0, 1, 1, 0, 1, 1, 0, 1, 0]

"""
lambdaで三項演算子を使い、convert()を1行で表現しています。
lambdaを使えばインスタントな関数を簡単に作成できるので、
何度も使うような関数でないのならこれで十分です。
"""
