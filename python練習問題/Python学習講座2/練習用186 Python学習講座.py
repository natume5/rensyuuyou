#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 演算の定義 ---")


print("--- オブジェクトの演算 ---")


"""
Pythonの文字列は等価演算子(==)で比較をしたり、
足し算(+記号)で結合することができます。
一方で引き算(-記号)を利用するとTypeErrorが発生します。
これは、strクラスで等価演算や足し算が文字列結合で定義されていて、
引き算が定義されていないために起きています。
"""

x = 'aaa'
y = 'bbb'

print(x == y)    # False
print(x != y)    # True
print(x + y)    # aaabbb

"""
print(x - y)    # TypeErrorが発生
自前でクラスを作成する際に、
このstrのように演算を定義すると
オブジェクト同士の演算を行うことが可能となります。
演算は専用の特殊メソッドを実装することにより定義できます。
"""


print("--- 比較演算 ---")


"""
比較演算子に対応する特殊メソッドは以下の通りです。

比較演算子 	特殊メソッド
< 	        __lt__
<= 	        __le__
== 	        __eq__
!= 	        __ne__
> 	        __gt__
>= 	        __ge__

比較演算子に対応する特殊メソッドの実装例を見てみましょう。
以下のサンプルでは、2つのインスタンス変数valとtextを持つ自作クラス
Sampleに対して比較演算を定義しています。
いずれの演算もvalのみ使用しています。
"""

class Sample:
	def __init__(self, val, text):
		self.val = val
		self.text = text

	def __lt__(self, other):
		return self.val < other.val

	def __le__(self, other):
		return self.val <= other.val

	def __eq__(self, other):
		return self.val == other.val

	def __ne__(self, other):
		return self.val != other.val

	def __gt__(self, other):
		return self.val > other.val

	def __ge__(self, other):
		return self.val >= other.val

obj1 = Sample(100, 'aaa')
obj2 = Sample(200, 'aaa')

print(obj1 < obj2)    # True
print(obj1 <= obj2)    # True
print(obj1 == obj2)    # False
print(obj1 != obj2)    # True
print(obj1 > obj2)    # False
print(obj1 >= obj2)    # False


print("--- 数値演算 ---")


"""
同様に数値演算も対応する特殊メソッドにより定義することができます。

比較演算子 	   特殊メソッド
+ 	           __add__
- 	           __sub__
* 	           __mul__
/ 	           __truediv__
// 	           __floordiv__
% 	           __mod__
divmod() 	   __divmod__
** 	           __pow__
< < 	       __lshift__
> > 	       __rshift__
& 	           __and__
^ 	           __xor__
| 	           __or__ 

上に挙げた以外にも累積代入文や単項演算子に対応する特殊メソッドもあります。
全量は多くなるため、足し算と引き算のサンプルを以下に掲載します。
以下のサンプルでは、平面座標を表すクラスに対し、
足し算と引き算を定義しています。
"""

class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		""" 座標の足し算を行う """
		x = self.x + other.x
		y = self.y + other.y

		return Coordinate(x, y)

	def __sub__(self, other):
		""" 座標の引き算を行う """
		x = self.x - other.x
		y = self.y - other.y

		return Coordinate(x, y)

	def __str__(self):
		return "coordinate: ({0}, {1})".format(self.x, self.y)

c1 = Coordinate(1000, 2000) 
c2 = Coordinate(300, 400) 
print(c1 + c2)    # coordinate: (1300, 2400)
print(c1 - c2)    # coordinate: (700, 1600)

"""
生成したオブジェクトに対し+と-で演算できることが確認できます。
"""
