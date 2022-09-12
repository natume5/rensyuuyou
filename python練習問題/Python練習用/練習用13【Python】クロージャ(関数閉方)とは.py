#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("---【Python】クロージャ(関数閉方)とは---")


"""
クロージャの説明

クロージャ(関数閉方)とは外側の変数を記憶した関数です。
"""
# 例1
def func():
	x = 3
	def add3(y):
		return y+x
	return add3

f = func()
print(f(4))    # 7

"""
func 関数は add3 関数を定義してそれを返します。
add3 関数は外側で定義された x を関数内で使用しています。
add3 関数をクロージャ、func 関数をエンクロージャといいます。
x は本来であれば func関数を抜けたところで消滅するfunc 関数におけるローカル変数です。
クロージャを生成したことで x が add3 関数内に記憶されて f(4) で呼び出した時に x が加算されます。
"""
# 例2
def func(name):
	def add_msg(message):
		return "Hi " + name + ": " + message
	return add_msg

f = func("Tanaka")
print(f("how are you?"))     # Hi Tanaka:how are you?

"""
例2は add_msg 関数がクロージャで name 変数を記憶したものが func 関数から生成されています。
"""
# 例2の続き
print(f.__code__.co_freevars[0], f.__closure__[0].cell_contents)    # name Tanaka

"""
関数 f に記憶されている変数名とその値を確認できます。
尚、クロージャには当然2個以上の変数も記憶できるので、エンクロージャの環境を記憶すると説明されることがあります。
"""


"""
自由変数 と 束縛(バインド)

Pythonの自由変数とはある関数内でローカル変数と自身の引数以外で使われている変数です。
例1で x は add3 の中において 自由変数 です。
同様に例2で name は add_msg にとって 自由変数です。

束縛とは名前を定義することです。
n = "Tanaka" とすれば この代入対象の識別子 n は 束縛されます。
関数を定義すれば関数名が束縛されますし、クラスを定義すればクラス名が束縛されます。
import文ではモジュール名が束縛されます。
つまり名前が何らかのオブジェクトに紐付けされることです。
また自由変数がクロージャ内に記憶されることをクロージャに束縛されると言います。


束縛された変数の更新
"""
# 例3
def func():
	x = 3
	def value(v):
		nonlocal x
		x = v
	def add(y):
		return y+x
	x = 5
	return value, add

v, f = func()
print(f(4))    # 9 = 5 + 4
v(10)    # xの値が5→10に変更される
print(f(4))    # 14 = 4 + 10

"""
束縛された変数の値を後から更新する必要がある場合は Python 3 で導入された nonlocal で宣言します。
例3では自由変数 x を nonlocal で宣言しておくことで後から
 value 関数を経由して add 関数内でも束縛されている x を更新しています。
"""
# 例3 の続き
print(v.__closure__[0].cell_contents is f.__closure__[0].cell_contents)    # True
"""
クロージャvで束縛されている変数 x とfで束縛される変数 x は同一オブジュエクトであることが判ります。
"""


"""
静的(レキシカル)スコープ

クロージャは静的スコープの言語で成り立ちます。
静的スコープとは変数の名前解決がソースコード上で成立するものいいます。
C, Python, Javascriptなどは静的スコープの言語です。
逆に動的スコープとは変数の名前解決が実行時のコースタックにて行われます。
Emacs Lisp, bash シェルスクリプト, powershell などは動的スコープです。
PerlやLispでは定義時に静的スコープか動的スコープかを選択できます。
"""


print("---【Python入門】クロージャの使い方をなんとなく理解する---")

"""
Pythonの関数に関連してクロージャというものがあります。
ちょっと入門者からすると話がわかりにくくなるようなものがどんどん出てきますね。

クロージャは、関数内関数に似てるようにも見えます。
参照環境を伴ったような関数、あるいはその関数への参照のことを指すというような言い方をしたりします。
関数内の変数を扱う時、その関数が宣言された時のもの（スコープ）
によって実行されるというような説明もできると思います。関数の外と関連させる感じでしょうか。
ちょっと具体的にコードを見た方が早いですね。

さっそくクロージャについてみていきましょう。
ちょっとPythonの中でも高度な話になると思うので、
こんな使い方があるという雰囲気だけ今の時点では掴んでおきましょう。
"""
"""
クロージャを理解する

クロージャというものがどんなものか簡単に理解するために、まず関数内関数のコードを見ておきましょう。

次のような関数内関数のコードを用意してみます。
"""
def outer_function(a, b):
	def inner_function():
		return a + b
	return inner_function()

print(outer_function(2, 3))    # 5

"""
これを実行してみます。引数a、bに「2」「3」を入れてouter_function()を呼び出してみましょう。
外側の関数に与えられた引数を使って、内側の関数が実行されて値が返されているのがわかります
"""


"""
クロージャのコードを書いてみる

クロージャは、このコードを次のように変更します。
"""
def outer_function(a, b):
	def inner_function():
		return a + b
	return inner_function

"""
違いがわかるでしょうか。
returnの返り値がinner_function()で関数を呼び出すのではなく、
inner_functionと丸括弧を使わずにオブジェクトが書かれています。

これを上と同様の引数で実行してみましょう。ファイル名はclosure.pyにしてAtomで実行しています。
"""
print(outer_function(2, 3))    # <function outer_function.<locals>.inner_function at 0x10d86b7b8>

"""
計算の値が返されずに、関数のオブジェクトの位置が返されているのがわかります。
inner_functionの情報が返されているのですが、これはまだ関数が実行されていない状態です。

この実行されていない状態を記憶してあとで使うことができるというようなことがクロージャではできるということです。
ここではこのinner_functionがクロージャになります。

これを出力するという実行には次のように行います。
"""
def outer_function(a, b):
	def inner_function():
		return a + b
	return inner_function

outer = outer_function(2, 3)
r = outer()
print(r)

"""
outer_function()を呼び出してouterという変数に入れています。
ここまではやっていることは同じですね。これに丸括弧()をつけて変数rに代入しています。
ここではじめてinner_functionが実行されます。これをrに代入してprintで出力しています。
実際に実行するとこうなります。

値が計算されて出力されているのがわかりますね。
"""


"""
もう一つコードを書いてみる

もう一つ例を作ってみましょう。四角の面積を計算するコードを書いてみます。
幅（width）と高さ（height）を掛け算すれば計算できるのはわかると思います。
それを次のように書いてみました。
"""
def area_calculation_func(width):
	def area_calculation(height):
		return width * height

	return area_calculation
"""
引数に幅（width）を与える関数area_calculation_func()を定義し、
その中に高さ（height）を引数に使って面積を計算する関数area_calculation()を定義しています。
返り値は関数ではなく丸括弧を外したarea_calculationを返していて、クロージャのコードになっています。

これを次のコードで実行してみます
"""
# widthが25と50の場合を計算
ac1 = area_calculation_func(25)
ac2 = area_calculation_func(50)

# heightを10として面積を求める
print(ac1(10))    # 250
print(ac2(10))    # 500

"""
まず幅に値を与えています。2つ幅の値を与えて、あとで両方の計算ができるようにしているという形です。

そして、これを高さが同じ場合に、この2つはどうなるかという処理をprintで行っているわけです。

実際に実行してみましょう。

２種類の幅を入れてac1、ac2としてarea_calculation_funcを保存しています。
このac1、ac2に丸括弧()をつけて呼びだすことではじめて計算が実行されます。
ここでは高さの値を入れてそれぞれ計算して出力されているのがわかります。
"""


print("---Pythonの基礎③(関数応用：クロージャ/デコレータ/ラムダなど)---")
"""
クロージャー

・後ほど実行したい関数などで利用
・関数のオブジェクトをリターンする
"""
def outer(a, b):
	def inner():
		return a + b

	return inner

print(outer(1, 2))
"""
// 結果　inner関数のオブジェクト
<function outer.<locals>.inner at 0x00000246129DE700>
"""
f = outer(1, 2)
r = f()
print(r)     # 3


def circle_area_func(pi):
	def circle_area(radius):
		return pi * radius * radius

	return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))    # 314.0
print(ca2(10))    # 314.1592
