#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　クラスの基本---")


"""
クラス定義とインスタンス化
クラス定義

まずはクラス定義の書き方から説明しましょう。class文を使用します。後ほど具体的な説明をしますので、
まずはクラスとはこういうものなのだと思ってください。

クラスの定義
class クラス名(継承元クラス名):
    """" クラスのドキュメンテーション """"
    def メソッド1(self, ...):
        処理
        ：

    def メソッド2(self, ...):
        処理
        ：

class文の後にクラス名と継承元クラス名を記述し、
:(コロン)の後に一段落インデントしてブロック内にクラス定義を記述します。
なお、継承元クラス名は省略可能です。空のクラスを作りたい場合は関数と同様に以下のようにpassを記述します。

class Sample:
    pass


クラスのインスタンス化

次に、クラスからオブジェクトを生成する方法について説明します。
前のページでも解説したとおり、オブジェクトを生成することをインスタンス化とも呼びます。以下の文となります。

オブジェクトの生成
変数 = クラス名()


クラスの構成要素

クラス定義とインスタンス化について説明しました。ここから具体例を交えてクラスの構成要素について説明します。

まずは、クラス定義とインスタンス化のサンプルを見てみましょう。
平面座標を表すには2つの数値(x, y)を扱う必要があります。
また、平行移動などもできると便利そうですね。そういった変数や機能をクラスにひとまとまりにしてみます。
なお、このオブジェクトがもつデータを属性と呼ぶ場合があります。
例えば、オブジェクトOは属性として変数x, yを持つ、といった使い方をします。
"""

class Coordinate:
	"""座標クラス"""

	def __init__(self):
		"""初期化"""
		self.x = 0
		self.y = 0

	def move(self, x, y):
		"""平行移動"""
		self.x += x
		self.y += y

	def show_coordinate(self):
		"""座標を表示する"""
		print(self.x, self.y)

	def __str__(self):
		"""文字列表現を返す"""
		return "({0},{1})".format(self.x, self.y)

# クラスの利用サンプル
cood = Coordinate()    # インスタンスを生成する
cood.x = 100    # xに代入
cood.y = 200    # yに代入
cood.show_coordinate()    # メゾットを利用する

print(cood)    # 文字列表現を取得する

"""
構成要素を確認してみましょう。


インスタンス変数

オブジェクト内部で保持する変数をインスタンス変数と呼びます。
(サンプルコードの6,7行目) インスタンス変数はメンバ変数と呼ばれることもあります。

Pythonには変数のアクセス修飾子はありません。
基本的にはすべてpubulicであるため、Javaのように属性毎のgetter、setterの実装はあまり見かけられません。

内部からアクセスする場合は、self.変数名でアクセスします。(サンプルコードの16行目)

外部からアクセスする場合は、オブジェクト.変数名でアクセスします。(サンプルコードの25, 26行目)


メソッド

既に用語としての定義はしましたが、クラスの属性として定義されている関数のことをメソッドと呼びます。
(サンプルコードの14行目)メソッドは必ずselfという引数を持ち、
インスタンス変数を参照する際はself.変数名の書式でアクセスします。


コンストラクタ

インスタンス生成時にクラスに__init__という名前のメソッドが定義されていると、
これが自動的に呼びだされます。(サンプルコードの4行目)通常、
インスタンス初期化処理（インスタンス変数の初期化など）を記述します。


__str__

オブジェクトの文字列表現を返します。(サンプルコードの18行目)必ずしも実装する必要はないのですが、
print出力する際に適切な文字列表現があったほうが開発がスムーズに進むかと思います。
（JavaのtoStringメソッドに相当します。）


補足 デストラクタ

生成時に実行される__init__とは逆に、__del__という名前のメソッドを定義すると、
オブジェクトが削除される際にそのメソッドが自動で実行されますが、以下の理由より使用は推奨しません。

    いつデストラクタが呼び出されるかわからない
    デストラクタが呼び出される保証がない
    上記理由より予想しない動作をすることがあり、設計が難しい

"""


print("--- Python入門　オブジェクトへの属性追加---")


"""
生成後の属性追加と削除

Pythonでは独自クラスから生成したインスタンスは属性を外部から追加したり削除することができます。


class Sample:

	def __init__(self):
		self.x = 100

obj = Sample()
obj.y = 200    # Sample型にyを追加することが出来る
print(obj.y)

del obj.x    # xを消すことも出来る
print(obj.x) # AttributeError: 'Sample' object has no attribute 'x'

上のコードでは、インスタンス変数にxをもつSample型のオブジェクトを生成していますが、
その後、属性yを追加したりdel文元々あったxを削除したりしています。


空のクラス

先程の属性追加は空のクラスに対しても行うことが可能です。
少し変わった使い方ですが、関数の戻り値で小さなオブジェクトにセットして返したい時などに利用することがあります。
"""

class Sample:
	pass    # 空のクラス

obj = Sample()    # 空のクラスをインスタンス化する
obj.x = 100
obj.y = 200
print(obj.x, obj.y)    # 100 200


print("--- Python入門　クラスオブジェクト---")


"""
クラスはオブジェクト

Pythonでは関数もオブジェクトとして扱えますが、クラスでさえもオブジェクトの一種として扱えます。
クラスをオブジェクトとして扱う場合はクラスオブジェクトや型オブジェクトと記述することにします。
それではクラスをオブジェクトとして変数に代入する例を確認してみましょう
"""

class Coordinate:
	"""座標クラス"""

	def __init__(self):
		"""初期化"""
		self.x = 0
		self.y = 0

	def show_coordinate(self):
		"""座標を表示する"""
		print(self.x, self.y)

# クラスを普通にインスタンス化する
cood = Coordinate()    # 普通にインスタンスを生成する
cood.x = 100    # メンバxに代入
cood.y = 200    # メンバyに代入
cood.show_coordinate()    # メゾットを利用する

# クラスをオブジェクトとして扱う
C = Coordinate    # Coordinateクラスのオブジェクトとして変数Cに代入する
cood2 = C()    # Cからクラスを生成する
cood2.x = 300
cood2.y = 600
cood2.show_coordinate()

"""
上のコードでは、平面座標の1点を表すクラス、Coordinateを独自に定義しています。
15行目から19行目まではこれまでどおり、普通にクラスからオブジェクトを生成しています。
一方、21行目から25行目ではクラスを一旦変数Cに代入し、Cからオブジェクトを生成しています。
このようにクラスをオブジェクトを別の変数に代入してからインスタンス化することが可能です。
もちろん引数にしたり戻り値にすることも可能です。
"""


print("--- Python入門　クラス変数---")


"""
クラス変数とは

Pythonのクラスにはclass文直下に変数を定義することが可能で、これをクラス変数と呼びます。
後述しますがインスタンスの共通値や静的な値をクラスに属させるような使い方をします。

クラス変数
class クラス名:
    クラス変数1
    クラス変数2
    ：

また、クラス変数はクラス名と変数名をドットでつないで参照することが可能です。

クラス変数へのアクセス
クラス名.クラス変数名

例をみてみましょう。
"""

class Coordinate:
	x = 0
	y = 0


print(Coordinate.x, Coordinate.y)    # 0 0

"""
上のサンプルでは、平面座標を表すクラスCoordinateについて、クラス変数x, yが実装されています。
それぞれの値をprint関数で確認しています。


クラス変数とインスタンス化

ここから少し難しくなります。
クラスをインスタンス化してもクラス変数にアクセスできるのですが、
インスタンスにクラス変数と同じ名前の変数で代入すると属性が新たに上書きされ、
インスタンスからはクラス変数にアクセスできなくなります。挙動が複雑なので注意してください。
"""

class Sample:
	val = []


# インスタンスを2つ生成
s1 = Sample()
s2 = Sample()

# valを更新
s1.val.append(100)
s2.val.append(200)

# 全て同じクラス変数を参照しているので同じ結果が出力される
print(Sample.val)    # [100, 200]
print(s1.val)    # [100, 200]
print(s2.val)    # [100, 200]

# s2に対してクラス変数と同じ変数を設定してみる
s2.val = []
s2.val.append(300)

# s2はインスタンス変数を参照している
print(Sample.val)    # [100, 200]
print(s1.val)    # [100, 200]
print(s2.val)    # [300]

"""
上のコードでは、リストをクラス変数としてもつクラスSampleを定義しています。
生成したインスタンスからもクラス変数が参照できていることが確認てきます。
一方で、代入することにより新たにインスタンス変数が設定されています。
こういった性質から、通常クラス変数をインスタンスからも参照する場合はイミュータブルなものを使用します。


クラス変数の使い所

クラス変数は以下の用途で使用することが多いかと思います。

共通初期値

先程の解説の通り、インスタンスを生成するとインスタンスを介してクラス変数にアクセスできます。
このため、インスタンスに所定の属性と初期値が設定されのと同じように扱うことができます。
ただし、前述の通り参照先はインスタンス変数ではなくクラス変数であるため、初期値はイミュータブルなものが望ましいです。


静的な値をクラスに属させる

もう1つの使い方として静的な定数値をクラスに属させたい場合に使用します。
以下は単価と数量をもつ注文を表すクラスですが、消費税を定数としてクラス変数に持っています。
"""

class Order:
	"""注文クラス"""

	CONSUMPTION_TAX = 0.1

	def __init__(self, unit_price, quantity):
		self.unit_price = unit_price
		self.quantity = quantity

	def calc_total_price(self):
		total_price = (self.unit_price * self.quantity) * (1 + Order.CONSUMPTION_TAX)
		return total_price

# インスタンスを生成して処理する
o = Order(100, 10)
print(o.calc_total_price())

# 定数を取り出して利用する場合
print(Order.CONSUMPTION_TAX)

"""
インスタンス化して処理する以外にクラスが管理する定数として使用したい場合に使用します。


クラス変数の注意点

色々癖の多いクラス変数ですが、最後にもう1つ注意点があります。
クラス変数もインスタンスの変数のように更新可能なのですが、
インスタンス化した際に参照されてしまう共通変数であるため、
更新すると全てのインスタンスから参照した値が切り替わります。
"""