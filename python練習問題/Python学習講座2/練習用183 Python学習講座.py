#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 特殊メソッド ---")


print("--- 特殊メソッド ---")


"""
Pythonのクラスでは、特殊メソッドと呼ばれる
アンダーバー2つで囲まれた特定の名前のメソッドを実装すると、
ある処理を実行した際にそのメソッドが自動的に呼び出されます。
たとえば__init__がそれに該当しますね。
オブジェクト生成時に自動的に呼びだされます。
"""


print("--- 基本的な特殊メソッドの紹介 ---")


"""
かなりの種類があるためここでは簡単に紹介するにとどめます。
また、次ページ以降で紹介するディスクリプタや演算の定義で使用するものも
特殊メソッドの一種です。

__repr__

オブジェクト情報を表す文字列を返します。

__str__

オブジェクトを文字列に変換して返します。

__bool__(self)

オブジェクト真理値の評価を返します。
"""


print("--- __str__と__repr__ ---")


"""
特殊メソッドの__str__と__repr__を実装したクラスのサンプルを見てみましょう。
"""

class User():
	"""
	ユーザークラス
	"""

	def __init__(self, name='', age=0):
		self.name = name
		self.age = age

	def say_hello(self):
		print('Helloo, my name is ' + self.name)

	def __str__(self):
		return 'User:' + self.name

	def __repr__(self):
		return str({'name': self.name, 'age': str(self.age)})

user = User('Kuro', 30)

print(user)    # print(str(user))と同じ
# User:Kuro

print(repr(user))
# {'name': 'Kuro', 'age': '30'}

"""
strの引数にUser型のオブジェクトを指定すると、
__str__で実装した内容の文字列表現が取得できました。
そして、前述の通りprint関数は内部的にstrを呼び出すため、
コード中のコメントの通りprint(str(user))としても
同様の結果を得ることができます。
また、repr関数を使用すると__repr__で返される値を得ることができます。
なお、__str__を実装せずに__repr__のみ実装すると、
str関数実行時に__repr__の値が取得されます。
このため、__str__は__repr__の簡易版と捉えても良さそうです。
独自にクラス定義をする場合、
デバッグやロギングの効率が上がるため
__repr__若しくは__str__を実装するようにしたほうがよいでしょう。
"""


print("--- __bool__ ---")


"""
__bool__を実装すると、bool関数を実行した際の
オブジェクトの真理値を設定することができます。
サンプルを見てみましょう。
"""

class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __bool__(self):
		if self.x or self.y:
			return True
		else:
			return False

p0 = Coordinate(0, 0)
p1 = Coordinate(100, 200)
p2 = Coordinate(0, 200)

if p0:
	print('点p0は真と評価されました')

if p1:
	print('点p1は真と評価されました')

if p2:
	print('点p2は真と評価されました')

# 点p1は真と評価されました
# 点p2は真と評価されました
