#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　特殊メソッド---")


"""
特殊メソッド

Pythonのクラスでは、特殊メソッドと呼ばれるアンダーバー2つで囲まれた特定の名前のメソッドを実装すると、
ある処理を実行した際にそのメソッドが自動的に呼び出されます。たとえば__init__がそれに該当しますね。
オブジェクト生成時に自動的に呼びだされます。


基本的な特殊メソッドの紹介

かなりの種類があるためここでは簡単に紹介するにとどめます。
また、次ページ以降で紹介するディスクリプタや演算の定義で使用するものも特殊メソッドの一種です。

__repr__

オブジェクト情報を表す文字列を返します。

__str__

オブジェクトを文字列に変換して返します。

__bool__(self)

オブジェクト真理値の評価を返します。


__str__と__repr__

特殊メソッドの__str__と__repr__を実装したクラスのサンプルを見てみましょう。
"""

class User():
	"""
	ユーザークラス
	"""

	def __init__(self, name="", age=0):
		self.name = name
		self.age = age

	def say_hello(self):
		print('Hello, my name is ' + self.name)

	def __str__(self):
		return 'User:' + self.name

	def __repr__(self):
		return str({'name': self.name, "age": str(self.age)})

user = User('Kuro', 30)

print(user)    # print(str(user))と同じ
# User:Kuro

print(repr(user))    # {'name': 'Kuro', 'age': '30'}

"""
strの引数にUser型のオブジェクトを指定すると、__str__で実装した内容の文字列表現が取得できました。
そして、前述の通りprint関数は内部的にstrを呼び出すため、
コード中のコメントの通りprint(str(user))としても同様の結果を得ることができます。

また、repr関数を使用すると__repr__で返される値を得ることができます。
なお、__str__を実装せずに__repr__のみ実装すると、str関数実行時に__repr__の値が取得されます。
このため、__str__は__repr__の簡易版と捉えても良さそうです。

独自にクラス定義をする場合、デバッグやロギングの効率が上がるため
__repr__若しくは__str__を実装するようにしたほうがよいでしょう。


__bool__

__bool__を実装すると、bool関数を実行した際のオブジェクトの真理値を設定することができます。
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

# 実行結果
# 点p1は真と評価されました
# 点p2は真と評価されました

"""
上のコードでは2次元平面上の座標を表すCoordinateクラスを実装しています。
点の座標がともに0、つまり原点以外は真と評価されます。
実際、コード後方にて原点p0、それ以外のp1、p2の真理値を評価していますが、
原点の場合は偽と評価されることが確認できます。
"""


print("--- Python入門　ディスクリプタ---")


"""
ディスクリプタとは

特殊メソッド__get__、__set__、__delete__のうちいずれかのメソッドが定義されたオブジェクトを
ディスクリプタと呼びます。ディスクリプタをメンバにもつオブジェクトに対し、
そのメンバにアクセスしたときの挙動をカスタマイズすることが可能となります。
ディスクリプタそのものに対するアクセス時に__get__、__set__、__delete__
が実行されるわけではない点に注意してください。

まずはサンプルとしてディスクリプタを実装したサンプルを紹介します。
以下のコードでは、属性textをもったクラスMyDescriptorにディスクリプタを実装しています。
参照、更新、削除した際の挙動がカスタマイズされています。
"""
"""
class MyDescriptor:
	""""ディスクリプタクラス""""

	def __init__(self, text):
		self.text = text

	def __get__(self, instance, owner):
		return '* ' + self.text

	def __set__(self, instance, text):
		self.text = text + '!'

	def __delete__(self, instance):
		del self.text
		print('text属性が削除されました')

class Sample:
	""""属性にディスクリプタを持つ""""
	descriptor = MyDescriptor('sample')

obj = Sample()
print(obj.descriptor)    # * sample

obj.descriptor = 'sample2'
print(obj.descriptor)    # * sample2

del obj.descriptor    # text属性が削除されました

print(obj.descriptor)    # AttributeError


ディスクリプタのメソッド

ではここから先程のサンプルを上から順に解説していきます。
__get__

メンバを参照した際の挙動を定義します。
上のサンプルでは、Sampleクラスのdescriptorメンバにアクセスした際に__get__が呼び出されています。
このことにより、アクセスした結果に対し、先頭に*が付加されるようになっています。


__set__

メンバを更新した際の挙動を定義します。
上のサンプルでは、Sampleクラスのdescriptorメンバを更新した際に__set__が呼び出されています。
このことにより、設定した内容に対し、末尾に!が付加されるようになっています。


__delete__

メンバを削除した際の挙動を定義します。
上のサンプルでは、Sampleクラスのdescriptorメンバを削除した際に__delete__が呼び出されています。
このことにより、削除時にメッセージが表示されるようになっています。
"""


print("--- Python入門　__new__メソッド---")


"""
__new__

特殊メソッドの__new__は、インスタンスの初期化前に「インスタンスを生成するために」処理が実行されます。
実装する際、__new__メソッドの第1引数はclsを指定しますが、クラスオブジェクトです。
また、戻り値にそのクラスのインスタンスを指定した場合、そのインスタンスの___init__メソッドが呼びだされます。

サンプルで動作を確認してみましょう。
"""

class MyClass:
	def __new__(cls):
		print('__new__')
		print(cls)

	def __init__(self):
		print('__init__')

	def __str__(self):
		return 'test'


obj = MyClass()
print(obj)    # None

"""
__new__()メソッドが呼び出されていますが、インスタンスを返していないため、オブジェクトが生成されず、
__init__()メソッドが呼び出されていない点に注目してください。
また、__new__()メソッドの引数は、クラスオブジェクトであることが解ると思います。


イミュータブルクラスの継承

通常、先程のサンプルのような実装はせず、__new__ではインスタンスを生成しそれを返します。
使いどころの1つとして、イミュータブルなクラスを継承する場合が挙げられます。
イミュータブルなクラスを継承した場合、以下のような記述ができません。

class MyClass(イミュータブルクラス):
    def __init__(self, value):
        self.value = value

__init__処理の時点で既にイミュータブルなインスタンスが生成されているため、
selfを書き換えることはできないからです。
このため、以下のサンプルように__new__を利用することでこの問題を回避することができます。
"""

class MyStr(str):

	def __new__(cls, text):
		print('__new__')
		return super().__new__(cls, text)

	def __init__(self, text):
		print('__init__')

	def __str__(self):
		return "***** " + super().__str__()


obj = MyStr('my_str')
print(obj)

"""
イミュータブルなクラスstrを継承したクラスを記述していますが、
__new__で親クラスのインスタンスを生成したものを返しています。
（本来、上記サンプルで__init__は不要なのですが、
__new__の後に__init__が呼び出されていることを確認するために記述しています。）
"""


print("--- Python入門　演算の定義---")


"""
オブジェクトの演算

Pythonの文字列は等価演算子(==)で比較をしたり、足し算(+記号)で結合することができます。
一方で引き算(-記号)を利用するとTypeErrorが発生します。
これは、strクラスで等価演算や足し算が文字列結合で定義されていて、
引き算が定義されていないために起きています。

x = 'aaa' 
y = 'bbb'

print(x == y) # Falseが出力される
print(x != y) # Trueが出力される
print(x + y) # aaabbbが出力される
print(x - y) # TypeErrorが発生

自前でクラスを作成する際に、
このstrのように演算を定義するとオブジェクト同士の演算を行うことが可能となります。
演算は専用の特殊メソッドを実装することにより定義できます。


比較演算

比較演算子に対応する特殊メソッドは以下の通りです。
比較演算子 	特殊メソッド
< 	__lt__
<= 	__le__
== 	__eq__
!= 	__ne__
> 	__gt__
>= 	__ge__

比較演算子に対応する特殊メソッドの実装例を見てみましょう。
以下のサンプルでは、2つのインスタンス変数valと
textを持つ自作クラスSampleに対して比較演算を定義しています。
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

"""
数値演算

同様に数値演算も対応する特殊メソッドにより定義することができます。
比較演算子 	特殊メソッド
+ 	__add__
- 	__sub__
* 	__mul__
/ 	__truediv__
// 	__floordiv__
% 	__mod__
divmod() 	__divmod__
** 	__pow__
< < 	__lshift__
> > 	__rshift__
& 	__and__
^ 	__xor__
| 	__or__

上に挙げた以外にも累積代入文や単項演算子に対応する特殊メソッドもあります。
以下の公式ドキュメントを参照してください。
3.3.7. 数値型をエミュレーションする

全量は多くなるため、足し算と引き算のサンプルを以下に掲載します。
以下のサンプルでは、平面座標を表すクラスに対し、足し算と引き算を定義しています。
"""

class Coordinate:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, other):
		"""座標の足し算を行う"""
		x = self.x + other.x
		y = self.y + other.y

		return Coordinate(x, y)

	def __sub__(self, other):
		"""座標の引き算を行う"""
		x = self.x - other.x
		y = self.y - other.y

		return Coordinate(x, y)


	def __str__(self):
		return "coordinate({0}, {1})".format(self.x, self.y)

c1 = Coordinate(1000, 2000) 
c2 = Coordinate(300, 400)
print(c1 + c2)    # coordinate(1300, 2400)
print(c1 - c2)    # coordinate(700, 1600)


print("--- Python入門　変数の型を判定する その2 type関数---")


"""
type関数

type関数は引数で指定したオブジェクトのクラス（=型オブジェクト）を返します。
"""

class Sample():
	pass

# オブジェクトを生成
s = Sample()

# sオブジェクトの型を取得する
s_type = type(s)
print(s_type)    # <class '__main__.Sample'>

"""
この他にも動的にクラスを生成することもできるのですが、応用的な内容であるため別途説明します。


type関数とisinstance関数

前述のとおり、type関数を使用して戻り値の一致を判定することで変数の型の判定が可能なのですが、
型の比較では継承関係が考慮されません。つまり、サブクラスと親クラスは別の型として判定されます。
以下のサンプルコードは、親子関係にある2つのクラス、Sample1とSample2からオブジェクトを生成し、
型を比較しています。
"""

class Sample1():
	"""適当なクラス"""
	pass

class Sample2(Sample1):
	"""Sample1を親とするクラス"""
	pass

obj1 = Sample1()    # Sample1型のオブジェクトを生成する
obj2 = Sample2()    # Sample2型のオブジェクトを生成する

# Typeを使用した場合、Sample2型はSample1型とはみなされない
print(type(obj1) == Sample1)    # True
print(type(obj1) == Sample2)    # False
print(type(obj2) == Sample1)    # False
print(type(obj2) == Sample2)    # True

print(isinstance(obj1, Sample1))    # True
print(isinstance(obj1, Sample2))    # False
print(isinstance(obj2, Sample1))    # True
print(isinstance(obj2, Sample2))    # True

"""

"""
