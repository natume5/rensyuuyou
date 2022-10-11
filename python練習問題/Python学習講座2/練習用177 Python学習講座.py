#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- クラス変数 ---")


print("--- クラス変数とは ---")


"""
Pythonのクラスにはclass文直下に変数を定義することが可能で、
これをクラス変数と呼びます。
後述しますがインスタンスの共通値や
静的な値をクラスに属させるような使い方をします。

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
上のサンプルでは、平面座標を表すクラスCoordinateについて、
クラス変数x, yが実装されています。
それぞれの値をprint関数で確認しています。
"""


print("--- クラス変数とインスタンス化 ---")


"""
ここから少し難しくなります。
クラスをインスタンス化してもクラス変数にアクセスできるのですが、
インスタンスにクラス変数と同じ名前の変数で代入すると属性が新たに上書きされ、
インスタンスからはクラス変数にアクセスできなくなります。
挙動が複雑なので注意してください。
"""

class Sample:
	val = []

# インスタンスを２つ生成
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
こういった性質から、通常クラス変数をインスタンスからも参照する場合は
イミュータブルなものを使用します。
"""


print("--- クラス変数の使い所 ---")


"""
クラス変数は以下の用途で使用することが多いかと思います。

共通初期値

先程の解説の通り、インスタンスを生成するとインスタンスを介して
クラス変数にアクセスできます。
このため、インスタンスに所定の属性と初期値が設定されのと
同じように扱うことができます。
ただし、前述の通り参照先はインスタンス変数ではなくクラス変数であるため、
初期値はイミュータブルなものが望ましいです。

静的な値をクラスに属させる

もう1つの使い方として静的な定数値をクラスに属させたい場合に使用します。
以下は単価と数量をもつ注文を表すクラスですが、
消費税を定数としてクラス変数に持っています。
"""

class Order:
	""" 注文クラス """

	CONSUMPTION_TAX = 0.100

	def __init__(self, unit_price, quantity):
		self.unit_price = unit_price
		self.quantity = quantity

	def calc_total_price(self):
		total_price = (self.unit_price * self.quantity) * (1 +
		Order.CONSUMPTION_TAX)
		return total_price

# インスタンスを生成して処理をする
O = Order(100, 10)
print(O.calc_total_price())    # 1100.0

# 定数を取り出して利用する場合
print(Order.CONSUMPTION_TAX)    # 0.1

"""
インスタンス化して処理する以外に
クラスが管理する定数として使用したい場合に使用します。
"""


print("--- クラス変数の注意点 ---")


"""
色々癖の多いクラス変数ですが、最後にもう1つ注意点があります。
クラス変数もインスタンスの変数のように更新可能なのですが、
インスタンス化した際に参照されてしまう共通変数であるため、
更新すると全てのインスタンスから参照した値が切り替わります。
"""

class Sample:
	val = 100

s1 = Sample()
print(s1.val)    # 100

Sample.val = 200

s2 = Sample()
print(s2.val)    # 200
print(s1.val)    # 200

"""
上のサンプルはクラス変数を更新していますが、
インスタンス化のタイミングに依らず変数の値が変わっています。
個人的にはクラス変数を更新するような実装は避けるようにしています。
"""




print("--- AI Academy Mediaより ---")
print("--- Python クラス変数 と インスタンス変数 の違い ---")



print("--- クラス変数とは ---")


"""
クラス変数とは、すべてのインスタンス間で共通した値をもつ変数です。
クラス変数は以下のように、クラス内に定義することで作成できます。
"""

class SampleClass:
	class_val = 'クラス変数'

"""
クラス変数にアクセス（情報を取り出す）するには以下のようにします。
"""

class SampleClass:
	class_val = 'クラス変数'

print(SampleClass.class_val)    # クラス変数


print("--- クラス変数にアクセスする① ---")


"""
クラス変数にアクセスするにはクラス名.クラス変数と記述します。
クラス変数を変更すると、そのクラスからインスタンス化された
全てのインスタンスのクラス変数が変更されます。
"""

class SampleClass:
	class_val = 'クラス変数'

print(SampleClass.class_val)    # クラス変数

# クラス変数を変更する
SampleClass.class_val = '変更2'
print(SampleClass.class_val)    # 変更2


print("--- クラス変数にアクセスする② ---")


"""
クラス変数にアクセスするにはクラス名.クラス変数以外にも
インスタンス.クラス変数でもアクセスが可能です。
"""

class SampleClass:
	class_val = 'クラス変数'

sample = SampleClass()
print(sample.class_val)    # クラス変数にアクセス  クラス変数


"""
しかし、この記述方法ではクラス変数を直接書き換える事は出来ません。
"""

class SampleClass:
	class_val = 'クラス変数'

sample = SampleClass()

sample.class_val = "クラス変数2"
print(sample.class_val)    # クラス変数2
print(SampleClass.class_val)    # クラス変数

"""
また、インスタンス.__class__.クラス変数として、
クラス変数にアクセスする事もでき、
この時にクラス変数の値を書き換えたい場合は以下のよう記述する事が出来ます。
"""

sample.__class__.class_val = 'クラス変数の値を書き換える'
print(SampleClass.class_val)    # クラス変数の値を書き換える
print(sample.class_val)    # クラス変数2

"""
インスタンス.__class__.クラス変数の書き方で値を上書きした場合、
別のインスタンスのクラス変数の値は全て共通した値を持ちます。
"""

class SampleClass:
	class_val = 'クラス変数'

sample = SampleClass()
sample2 = SampleClass()

sample.__class__.class_val = 'クラス変数の値を書き換える'

print(SampleClass.class_val)    # クラス変数の値を書き換える
print(sample.class_val)    # クラス変数の値を書き換える
print(sample.class_val)    # クラス変数の値を書き換える

"""
クラス変数以外に次のセクションで説明する
インスタンス変数と呼ばれる変数もあります。
インスタンス変数とは今の段階では
そのインスタンスだけで利用できる属性とお考えください。
"""


print("--- インスタンス変数とは ---")


"""
インスタンス変数は、個々のインスタンスに格納される変数のことです。
インスタンス変数のサンプルプログラムを例に理解を深めていきましょう。
ここではUserクラスを作っていきます。
"""

class User:
    # 実行順②
    def __init__(self, name):    # インスタンス化されて渡ってくる値を受ける変数を定義します
        # インスタンス変数（属性の初期化）
        self.name = name     # 実行順③
        print("コンストラクタが呼ばれました")     # # 実行順④

    def hello(self):
        print("Hello " + self.name)
        
user = User("Sample User")    # userというインスタンスを生成しています。　実行順①

"""
今回定義したUserクラスのコンストラクタはnameという引数を取り、
その引数で変数であるself.name
（この変数のことをインスタンス変数と呼びます）を初期化しています。
インスタンス変数は、個々のインスタンスに格納される変数のことですので、
ここでは5行目のnameがインスタンス変数です。
8行目に定義したhelloメソッド内9行目で、
selfの後ろに属性名nameを書いていますが、
このように.インスタンス変数名と書くことで、
インスタンス変数の作成及びアクセスができます。
"""


print("--- インスタンス変数にアクセスする ---")


"""
インスタンス変数にアクセスするには、インスタンス名.インスタンス変数と記述します。
"""

class User:
    # 実行順②
    def __init__(self, name):    # インスタンス化されて渡ってくる値を受ける変数を定義します
        # インスタンス変数（属性の初期化）
        self.name = name     # 実行順③
        print("コンストラクタが呼ばれました")     # # 実行順④

    def hello(self):
        print("Hello " + self.name)
        
user = User("Sample User")    # コンストラクタが呼ばれました
py = User('python')    # コンストラクタが呼ばれました

user.hello()    # Hello Sample User
py.hello()    # Hello python




print("--- Tech Lifeより ---")
print("--- Pythonのクラス変数とインスタンス変数の使い分けについて ---")


print("--- クラス変数とインスタンス変数 ---")


"""
pythonはオブジェクト指向言語で、プロパティにデータを格納することができる。
プロパティには、クラス変数とインスタンス変数がある。
ここでは、クラス変数とインスタンス変数の違いについて説明する。
"""


print("--- クラス変数について ---")


"""
クラス変数は、クラスが所有する変数で
作成されたすべてのインスタンス間で共有される。
コードを実行して、クラスが読み込まれたされた際にクラス変数が宣言される。
以下のように定義する


class Person:
name = 'Hoge' # クラス変数

また、アクセスする場合には以下のようにクラス名.変数名とすればよい。

Person.name

上の例では、Personクラスにnameをクラス変数として持たせている。

Example

    クラス変数へのアクセス、変更
"""

class Coffee:
	name = 'Espresso'

print(Coffee.name)    # クラス変数にアクセス(Espressoと表示)  Espresso
Coffee.name = "Americano"    # クラス変数を変更
print(Coffee.name)    # Americanoと表示  Americano

"""
また、インスタンスを作成してから、

instance.variable

として、クラス変数にアクセスすることもできる。
ただしこの方法では、クラス変数を直接書き換えることはできない

instance.variable = "〇〇"

として値を書き換えた場合、
クラス変数とは別のメモリ上の位置にデータが格納される

Example

    インスタンスからクラス変数へアクセス
"""

class Coffee:
	name = 'Espresso'

c1 = Coffee()    # インスタンス作成
print(c1.name)    # Espresso
c1.name = 'Americano'    
# 値を変更(クラス変数Coffee.nameとは異なるメモリ上に格納される)
print(c1.name)    # Americano
print(Coffee.name)    # Espresso

"""
また、

instance.__class__.変数名

としてもクラス変数にアクセスすることができる。
Example

    インスタンスからクラス変数へアクセス
"""

class Coffee:
	name = 'Espresso'

c1 = Coffee()    # インスタンス作成
print(c1.__class__.name)    # Espresso
c1.__class__.name = 'Americano'    # クラス変数の値を変更
print(c1.__class__.name)    # Americano
print(Coffee.name)    # Americano


print("--- インスタンス変数について ---")


"""
インスタンス変数は、クラスから作成されたインスタンスが持っている変数である。
属しているインスタンスに応じて、インスタンス変数の値は異なる。
また、インスタンス変数はメソッド内に記述して利用する。
"""

class Order:
	def __init__(self, name, price):
		self.name = coffee_name
		self.price = price

"""
上の例では、nameとpriceがインスタンス変数である。
インスタンス変数は以下のように利用する

Example

    インスタンス変数へアクセス
"""

class Human:
	msg = 'Hello'    # クラス変数です。インスタンス間で共有される

	def __init__(self, name, age):
		self.name = name
		self.age = age
		# インスタンス変数、コンストラクタ呼び出しの時に初期化

	def print_msg(self):
		print("{} name = {}, age = {}".format(self.msg, self.name, self.age))

taro = Human('Taro', 20)
jiro = Human('Jiro', 18)

print(taro.msg)    # クラス変数msgにアクセス、「Hello」と表示
print(jiro.msg)    # クラス変数msgにアクセス、「Hello」と表示

print(taro.name)    # インスタンス変数nameにアクセス、「Taro」と表示
print(jiro.name)    # インスタンス変数nameにアクセス、「jiro」と表示

print(Human.msg)    # クラス変数は、クラス名.変数名でアクセス可能  Hello
Human.msg = 'Hi!!'    # クラス変数を変更

print(taro.msg)    # クラス変数msgは共有されており、変更されたため「Hi!!」と表示
print(jiro.msg)    # クラス変数msgは共有されており、変更されたため「Hi!!」と表示

taro.__class__.msg = 'Goodbye'
# クラス変数は、インスタンス名.__class__.変数名でアクセス可能

print(taro.msg)
# クラス変数msgは共有されており、変更されたため「GoodBye」と表示
print(jiro.msg)
# クラス変数msgは共有されており、変更されたため「GoodBye」と表示


print("--- クラス変数とインスタンス変数についてまとめ ---")


"""
以上
クラス変数は、クラスの直下に定義され
すべてのインスタンスから参照すると同じ値を得ることができる。
このようにクラス変数はインスタンス間で共有される。
インスタンス変数は、インスタンス毎に設定してそれぞれ値を入れることができる。

クラス変数 	

    オブジェクト同士で共有する変数
    メソッドの内部でなく、クラスの直下に記載


インスタンス変数 	

    インスタンスごとに別々に利用する変数
    メソッドの内部に記載
"""









