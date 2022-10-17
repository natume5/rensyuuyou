#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- クラスの継承 ---")


print("--- 継承 ---")


"""
オブジェクト指向プログラミングをサポートする言語では、
大抵継承と呼ばれる機能が実装されています。
あるクラスを定義する際に親となるクラスを指定すると、
そのクラスの機能をまるごと引き継ぐことが可能となりますが、
この機能のことを継承と呼びます。


クラス定義と継承

Pythonで既存クラスを継承したクラスを定義する場合は、
class文の後方に丸括弧で親クラスを指定します。
なお、これまでのように親クラスを指定しない場合、
objectクラスを継承したクラスとなります。
サンプルを見てみましょう。Base、Subという2つのクラスを定義しますが、
SubはBaseクラスを継承するものとします。
"""

class Base:
	""" 親クラス """

	def func1(self):
		print('func1')

class Sub(Base):
	""" 子クラス """

	def func2(self):
		print('func2')


obj = Sub()    # 子クラスをインスタンス化
obj.func1()     # func1
obj.func2()    # 親クラスのメソッドも実行可能    func2

"""
上のサンプルでは、継承によりSubクラスのfunc2に加え、
親クラスのfunc1も呼び出すことができていることを確認することができます。


親クラスのメソッドの呼び出し

親クラスのメソッドを呼び出す際は、super()を使用します。
"""

class Base:
	def func1(self):
		print('func1っつ')

class Sub(Base):
	def func2(self):
		super().func1()    # 親クラスのメソッドを呼び出し
		print('func2っつ')

obj = Sub()
obj.func2()
# func1
# func2

"""
__init__とsuper

super()を使用すると初期化子__init__を使用して
インスタンスの属性を設定することができます。
以下のサンプルは、ユーザを表すUserクラスに対し、
それを継承した社員を表すEmployeeクラスを定義しています。
Userは属性としてname、ageを持ち、
Employeeは属性として部署departmentを持つものとします。
"""

class User:
	"""
	ユーザークラス
	"""

	def __init__(self, name="", age=0):
		self.name = name
		self.age = age

	def say_name(self):
		print('私の名前は' + self.name + 'です。')

class Employee(User):
	"""
	社員クラス
	"""

	def __init__(self, name, age, department):
		super().__init__(name, age)
		self.department = department

	def say_department(self):
		print('私の部署は' + self.department + 'です。')

e = Employee('Suzuki', 45, '営業部')
e.say_name()    # 私の名前はSuzukiです。
e.say_department()    # 私の部署は営業部です。

"""
上のサンプルでサブクラスの方に__init__で
インスタンス変数departmentが追加されています。


オーバーライド

また、派生クラスで親クラスのメソッドをオーバーライドすることもできます。
先程のEmployeeのsay_nameメソッドをカスタマイズしてみます。
"""

class Employee(User):
	"""
	社員クラス
	"""

	def __init__(self, name, age, department):
		super().__init__(name, age)
		self.department = department

	def say_name(self):
		print('名前は' + self.name + '、所属部署は' + self.department + 'です。')

e = Employee('Suzuki', 45, '営業部')
e.say_name()    # 名前はSuzuki、所属部署は営業部です。

"""
このサンプルのように親クラスのメソッドを上書きする操作のことを
オーバーライドと呼びます。
"""


print("--- 多重継承継承 ---")


"""
Pythonでは複数のクラスを継承することができ、これを多重継承と呼びます。
多重継承をする場合は、親クラスをカンマ区切りで指定します。
"""

class Base1:
	def func1(self):
		print('func1')

class Base2:
	def func2(self):
		print('func2')

class Sub(Base1, Base2):
	def func(self):
		super().func1()
		super().func2()

obj = Sub()
obj.func()
# func1
# func2

"""
言語によってはアンチパターンとして扱われることもある多重継承ですが、
再利用として非常に有用な手段でもあるため
Pythonの様々なライブラリで活用されています。
Java等の単一継承言語育ちの方はMixinについて知っておくと
利用や設計する際に一役買うかと思います。
"""



print("--- codecampより ---")
print("--- 【Python入門】クラスの継承についてやさしく解説 ---")


"""
継承、オブジェクト指向を実行する上で欠かせない機能ですね。
今回は、Pythonの継承についてご紹介。
恐らく継承を学習される方は、ある程度Pythonを体験していると思いますので、
コードメインの記事としました。
コードのコピペ、アレンジを経て、継承マスターにお役立て下さい。


継承とは

継承（Inheritance）は、クラスの中でよく使われる機能の一つで、
クラス機能を再利用したり追加できるとてもパワフルな機能。 
TensorFlowやFlaskといったフレームワーク系でもよく使われていますね。 
今回は、

    簡単な継承機能
    スーパークラスを使った継承機能
    継承の継承
    ちょっと実践的な継承
    複数のクラスをまとめて継承

といった継承の基礎的な部分をコード中心にご紹介していきます。
Pythonの継承を体験【簡単編】
"""

class Fish:
	def __init__(self, name, build='ほね', eyelids=False):
		self.name = name
		self.build = build
		self.eyelids = eyelids

	def swim(self):
		print('こちらの魚は泳ぎます。')

	def swim_back(self):
		print('こちらの魚は後ろ向きにも泳ぎます。')

class Medaka(Fish):
	pass

"""
こちらではクラスの簡単な継承をご紹介。 
上記コードの下から2行目で親クラスの Fish を継承しています。

class Medaka(Fish):

class 新規クラス名（継承したいクラス名）:

という書き方で継承機能を表現できます。
新規クラス名のことを「子クラス」と呼びますね。
最終行の pass は、「親クラスそのままを」という意味。
上記コードで実際にオブジェクトを作成して、メソッドを実行してみますね。
"""

no0 = Fish('魚１号（親クラス）')
print(no0.name)
print('骨格:', no0.build)
print('まぶた:', no0.eyelids)
no0.swim()
no0.swim_back()

no1 = Medaka('魚2号（子クラス）')
print(no1.name)
print('骨格:', no1.build)
print('まぶた:', no1.eyelids)
no1.swim()
no1.swim_back()
# 魚１号（親クラス）
# 骨格: ほね
# まぶた: False
# こちらの魚は泳ぎます。
# こちらの魚は後ろ向きにも泳ぎます。
# 魚2号（子クラス）
# 骨格: ほね
# まぶた: False
# こちらの魚は泳ぎます。
# こちらの魚は後ろ向きにも泳ぎます。

"""
子クラスの Medakaクラスには pass しか書かれていないのに、
親クラスのパラメーターやメソッドを継承していることが分かります。
せっかくなので、ただ親クラスを利用するだけでなく、
親クラスの内容を上書きする方法もご紹介してみますね。以下のコードを追加。
"""

class Fish:
	def __init__(self, name, build='ほね', eyelids=False):
		self.name = name
		self.build = build
		self.eyelids = eyelids

	def swim(self):
		print('こちらの魚は泳ぎます。')

	def swim_back(self):
		print('こちらの魚は後ろ向きにも泳ぎます。')

class Medaka(Fish):
	pass

class Kingyo(Fish):
	def __init__(self, name, build='ほね', eyelids=False):
		self.name = '金魚ちゃん' + name + 'だよ'
		self.build = build + ' かな'
		self.eyelids = eyelids

no2 = Kingyo('魚3号(子クラス)')
print(no2.name)
print('骨格:', no2.build)
print('まぶた:', no2.eyelids)
no2.swim()
no2.swim_back()
# 金魚ちゃん魚3号(子クラス)だよ
# 骨格: ほね かな
# まぶた: False
# こちらの魚は泳ぎます。
# こちらの魚は後ろ向きにも泳ぎます。

"""

    親クラスの内容を上書きすべく Kingyo クラスを設定。
    親クラスの初期化データをコピーして、データを追加。
    その結果、継承元のデータを上書きして出力。

次は、親クラスに機能追加できる スーパークラス super() を確認していきます。
"""


print("--- スーパークラス super() を使った継承を体験 ---")


"""
親クラスのメソッドを子クラスでも使いつつ、
新たにパラメーターやメソッドを追加する場合は、
スーパークラス super() が便利。 
簡単なスーパークラスの事例を以下にご紹介します。
"""

class Cat(object):
	def __init__(self, name):
		self.name = name

class SuperCat(Cat):
	def __init__(self, name, function):
		super(SuperCat, self).__init__(name)
		self.function = function

sample1 = Cat('ちゃちゃ')    # オブジェクトの作成
sample2 = SuperCat('ごん', '飛ぶ')    # オブジェクトの作成
sample3 = SuperCat('みーな', 'もぐる')    # オブジェクトの作成
print(sample1.name)    # ちゃちゃ   メソッドの実行
print(sample2.name, sample2.function)    # ごん 飛ぶ   メソッドの実行
print(sample3.name, sample3.function)    # みーな もぐる   メソッドの実行

"""
まずスーパークラスが登場するのは子クラスで、
親クラスから継承したいパラメーターを指定します。 
上記コードの場合は、7行目の

super(SuperCat, self).__init__(name)

ですね。 name を継承。 
後は特別な処理はなく、メソッドやオブジェクトを作成して、
親クラスを利用した子クラスができあがり。
実際にスーパークラスのコードを書いていると、
「継承の継承ってできるのかな？」と思ったりしませんか？ 
継承の継承、試してみましたので以下をご参考下さい。
"""


print("--- 継承の継承・・・を体験 ---")


"""
ある基準となる機能へ段階的に機能を追加したい場合、
「継承の継承」で実現できます。
"""

class Cat(object):
	def __init__(self, name):
		self.name = name

class SuperCat(Cat):
	def __init__(self, name, function):
		super(SuperCat, self).__init__(name)
		self.function = function

class GotCat(SuperCat):
	def __init__(self, name, function, magic):
		super(GotCat, self).__init__(name, function)
		self.magic = magic

	def power(self):
		self.magic = 'マジックパワー！！' + self.function * self.magic

sample1 = Cat('ちゃちゃ')
sample2 = SuperCat('ごん', '飛ぶ')
sample3 = GotCat('だい', '癒す', 5)
print(sample1.name)
print(sample2.name, sample2.function)
sample3.power()
print(sample3.name, sample3.magic)
# ちゃちゃ
# ごん 飛ぶ
# だい マジックパワー！！癒す癒す癒す癒す癒す
"""
段階的にクラスが継承されて、
それに合わせてメソッドも継承されていることが分かります。 
ちなみに継承の継承なので「孫クラス」という位置づけになりますが、
「孫クラス」という言葉は流通していません。
それでは次に、少し実践的な事例をご紹介しますね
"""


print("--- ちょっと実践的な継承事例 ---")


"""
これまではとりあえず継承やスーパークラスの雰囲気をお伝えしてきました。 
これからご紹介するのは、私がPythonの継承学習で参考になったコードです。
Pythonのチュートリアル動画としてはヒットの 
18万回以上の再生回数を記録している動画を元にしています。
参考動画：YouTube／Corey Schaferさん
"""

class Employee:
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = first + '.' + last + '@email.com'
		self.pay = pay

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

class Programmer(Employee):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Manager(Employee):
	raise_amt = 1.50

	def __init__(self, first, last, pay, employees=None):
		super().__init__(first, last, pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('雇っているエンジニア:', emp.fullname(), 'さん')
			print('対応言語:', emp.prog_lang)

dev_1 = Programmer('Tanaka', 'Tarou', 50000, 'Python')
dev_2 = Programmer('Oshima', 'Takayuki', 60000, 'PHP')
mgr_1 = Manager('Adam', 'Jozee', 60000)

print(mgr_1.fullname())
print(mgr_1.email)
print('基本年収($):', mgr_1.pay)
mgr_1.apply_raise()
print('年間の役職手当($):', mgr_1.pay)

mgr_1.add_emp(dev_1)
mgr_1.print_emps()
# Adam Jozee
# Adam.Jozee@email.com
# 基本年収($): 60000
# 年間の役職手当($): 90000
# 雇っているエンジニア: Tanaka Tarou さん
# 対応言語: Python 

"""
ちょっと長いコードですが、何が処理されているか検討つきますでしょうか？
上記コードは労働者のステータスを管理するプログラムで、
クラス Employee を雛形にプログラマーとマネージャーを管理。
親クラスの Employee に名前とメールアドレス、
そして最初の子クラス Programmer で対応言語、
もう一つの子クラスで Manager の雇用状況を表現。
こちらのコードでは、プログラマの対応言語やマネージャーの年収が
入力されていますが、データベースなどと連携できると活用範囲が広がりそうですね。
"""


print("--- 複数の継承クラスをまとめて利用 ---")


"""
最後に複数のPythonファイルからクラスの継承機能を引用する例をご紹介します。 
今回は、本稿でご紹介した fish.py と Inheritance_Inheritance.py 
の2つのPythonファイルからクラス継承するPythonプログラムを作成してみました。 
尚、fish.py と Inheritance_Inheritance.py 
のファイル内のオブジェクト作成行は、なしにして実行しました。


ファイル名　Add.py

from Inheritance_Inheritance import GodCat
from fish import Medaka

class Main(GodCat, Medaka):
    def __init__(self):
        super(Main, self).__init__()

cat1 = GodCat('だい','癒やす',5)
cat1.power()
print(cat1.name,cat1.magic)

fish1 = Medaka("メダカ1号")
print(fish1.name)


class CatCat(GodCat):
    def __init__(self, name, function, magic, change):
        super(CatCat, self).__init__(name, function, magic)
        self.change = change + 'に変身だにゃー'

cat2 = CatCat('こんきち','はねる','2','みけねこ')
print(cat2.name, cat2.change)


冒頭の from ●● import ●● 文で外部ファイル＆外部クラスを読み込み。 
そして後は外部クラスを利用してオブジェクトを作成し、メソッドの実行となります。
また外部クラスに機能を追加する場合も今までと同じで、
継承を用いた記述でプログラムを実行可能。 
上記ではクラス GodCat を継承し、 CatCat という子クラスを作成していますね。
尚、当然のことですがインポートしていない外部クラスは利用できません。
"""



print("--- MinatoLogより ---")
print("--- Python入門【クラスの継承】 ---")


"""
Pythonでは、既存のクラスの機能を引き継いだまま、
新しい機能を追加したり、変更して新しいクラスを作成することができます。
このようなクラスの作成方法をクラスの継承といいます。
今回はPythonでのクラスの継承について、
プログラミング初心者にも分かりやすく解説します。
"""


print("--- クラスの継承 ---")


"""
クラスの継承とは

クラスの継承とは、あるクラスをベースとして、そのメソッドや変数を引き継いだまま、
新たなクラスを定義する方法です。
ベースとなる親のクラスをスーパークラス、
スーパークラスを継承した子クラスをサブクラスといいます。
それでは、クラスの継承について、
実際にプログラミングを行いながら確認していきます。

クラスの継承

class サブクラス名(スーパクラス名):
　クラス内の処理

以下の例では、Carクラスを継承したToyotaCarクラスを定義しています。
ToyotaCarクラスでは、コンストラクタやメソッドを定義していませんが、
スーパクラスのコンストラクタやdrive()メソッドがそのまま利用できます。
"""

class Car:
	def __init__(self, name, speed=60):
		self.name = name
		self.speed = speed

	def drive(self):
		print(f'{self.name}が時速{self.speed}kmで走行します。')

class ToyotaCar(Car):
	pass

car1 = ToyotaCar('ハリアー', 80)
car1.drive()    # ハリアーが時速80kmで走行します。

"""
上の例では、サブクラスでは何も定義しませんでしたが、
通常はサブクラスで新たな変数やメソッドを追加して利用することになります。
以下の例では、Carクラスを継承したTeslaCarクラスを定義しています。
TeslaCarクラスでは、スーパークラスのdrive()メソッドも実行でき、
新たに定義したauto_drive()メソッドも実行可能であることが確認できます。
"""

class Car:
	def __init__(self, name, speed=60):
		self.name = name
		self.speed = speed

	def drive(self):
		print(f'{self.name}が時速{self.speed}kmで走行します。')

class TeslaCar(Car):
	def auto_drive(self):
		print(f'{self.name}が時速{self.speed}kmで自動運転モードで走行します。')

car1 = TeslaCar('Model S', 80)
car1.drive()    # Model Sが時速80kmで走行します。
car1.auto_drive()    # Model Sが時速80kmで自動運転モードで走行します。

"""
メソッドのオーバーライド

先程の例では、クラスを継承し、サブクラスに新たなメソッド追加しました。
しかし、スーパクラスで定義されている機能を上書きしたいというケースもあります。
その様な場合は、メソッドのオーバーライドを行うことで、
スーパクラスの処理を上書きできます。
以下の例では、CarクラスのサブクラスFerrariCarクラスを定義しています。
FerrariCarクラスではCarクラスのdrive()メソッドをオーバーライドしています。
"""

class Car:
	def __init__(self, name, speed=60):
		self.name = name
		self.speed = speed

	def drive(self):
		print(f'{self.name}が時速{self.speed}kmで走行します。')

class FerrariCar(Car):
	def drive(self):
		print(f'レーシングモードで時速{self.speed * 2}kmで走行します。')

car1 = FerrariCar('Model S', 100)
car1.drive()    # レーシングモードで時速200kmで走行します。
car2 = TeslaCar('Model S', 80)
car2.drive()    # Model Sが時速80kmで走行します。

"""
コンストラクタのオーバーライド

通常のメソッドだけではなく、コンストラクのような特殊メソッドもオーバーライドできます。
以下の例では、FerrariCarクラスでコンストラクタ__init__()をオーバーライドして、
mode変数の初期化処理を追加しています。
また、Pythonではsuper()という関数を利用することで、
スーパークラスの処理を呼び出すことができます。
super().init(name, speed)では、
スーパークラスCarクラスの__init__()を呼び出しています。
このようにsuper()を利用すると、
クラスの継承を行うたびにスーパークラスで定義している共通する処理を
わざわざ再度記述する必要がないため、効率的に開発を行えるようになります。
"""

class FerrariCar(Car):
	def __init__(self, name, speed=100, mode='SPORT'):
		super().__init__(name, speed)
		self.mode = mode

car1 = FerrariCar('Model S', 100, 'RACE')
print(car1.name, car1.speed, car1.mode)
# Model S 100 RACE

"""
多重継承

Pythonでは、多重継承を行うことができます。
多重継承は文字通り、複数のクラスを継承することです。
サブクラスでは、複数のスーパークラスの特徴を受け継ぐことができます。
以下の例では、RobotクラスとAirPlaneクラスを継承した
HyperRobotクラスを定義しています。
HyperRobotクラスは二つのスーパクラスが持っている機能を
両方とも受け継いでいるため、
attack()メソッドとfly()メソッドの両方を利用できます。
"""

class Robot():
	def attack(self):
		print('ビームを打ちます')

class AirPlane():
	def fly(self):
		print('空を飛びます')

class HyperRobot(Robot, AirPlane):
	pass

robot1 = HyperRobot()
robot1.attack()    # ビームを打ちます
robot1.fly()    # 空を飛びます


print("--- まとめ ---")


"""
今回はクラスの継承について解説しました。
クラス継承は既存のクラスの機能を引き継いだまま、
新しい機能を追加したり、変更して新しいクラスを定義する方法です。
クラスの継承を利用することで、効率的に開発が行えるため、
実際の開発でも頻繁に利用します。
クラスの継承の使い方については、しっかり覚えておきましょう。
"""



print("--- CodeGraffitiより ---")
print("--- 【Python入門】クラスの継承、メソッドのオーバーライドとsuper ---")


"""
Pythonのクラスについて学んでいますが。
部品の設計図とも言われるクラスを作ると、
なんども関数を定義しなくても、クラスからオブジェクトを作って利用すれば、
手間もかからずコードがスッキリもしました。
そこで、新たに別のクラスを作った場合、
メソッドをまた定義すると場合によっては
他のクラスと同じメソッドが必要になったりすることがあります。
それをまた一から定義するのはとても非効率です。
そこで、別のクラスのメソッドを他のクラスで使えるとなると便利ですよね。
クラスはそれをすることができます。
使いたい別のクラスを指定して、
使いたい機能を追加したり書き換えたりすることで新しいクラスを作ることができます。これをクラスの継承と言います。
一度作ったクラスは別のクラスで再利用することができる方法とも言えますね。
ここではPytonのクラス継承についてみていきたいと思います。
"""


print("--- クラスの継承 ---")


"""
新しくクラスを作るとき、すでにある別のクラスを再利用してクラスを継承するとき、
この別の元からあるクラスのことを親、スーパークラス、基底クラスと呼びます。
新しくつくるクラスのことは、子、サブクラス、派生クラスと呼びます。
クラスの継承の書き方はこのような形になります。

class 子クラス名(親クラス名):
    pass # クラス定義

具体的にコードを作ってクラスの継承を見て行きましょう。
次のように親クラスとそれを継承した子クラスのコードを書いてみました。
（ホンダの車をコード例に使ってます。特に他意はありません。
ただ私がホンダ党なだけです）
"""

class HondaCar():    # 親クラス
	def drive(self):
		print('車を走らせます。')

	def motor_drive(self):
		print('モーターで車を走らせます。')

class CivicCar(HondaCar):    # 子クラス
	pass

honda_car = HondaCar()
honda_car.drive()    # 車を走らせます。

civic_car = CivicCar()
civic_car.drive()    # 車を走らせます。

"""
親クラスには２つのメソッドを定義しています。
selfを入れるのを忘れないようにしましょう。
子クラスは丸括弧の中に親クラスを継承するように記入しています。
ただし、メソッドは定義せずにpassを置いています。
親クラスをオブジェクト化して、drive()メソッドを実行するコードと、
子クラスをオブジェクト化してdrive()メソッドを実行するコードを
最後に置いています。
このコードを実行してみましょう。
メソッドが実行されていますが、
上側（親クラス）が実行されているのは当然ですよね。
これまでと一緒です。
下側（子クラス）が実行されているのは不思議ですよね。
子クラスにはpassを置いて何も行わなないとしか
定義していないにも関わらずメソッドが実行されています。
これがクラスを継承したことでできることです。
親クラスを継承することで、親クラスに定義されているメソッドを
子クラスで利用することができるのです。
このコードに次のようなもう一つ子クラスを作ってみます。
"""

class HondaCar():    # 親クラス
	def drive(self):
		print('車を走らせます。')

	def motor_drive(self):
		print('モーターで車を走らせます。')

class CivicCar(HondaCar):    # 子クラス
	pass

class NsxCar(HondaCar):
	def track_mode(self):
		print('サーキット走行モードで走らせます！')

nsx_car = NsxCar()
nsx_car.drive()    # 車を走らせます。
nsx_car.motor_drive()    # モーターで車を走らせます。
nsx_car.track_mode()    # サーキット走行モードで走らせます！

"""
３つ目のクラスも１つ目のクラスを継承させて、
一つだけこのクラスに特有のメソッドを定義しています。
コードを実行してみます。

継承した親クラスのメソッドと、クラス内に定義したメソッドが
実行されているのがわかります。
このようにすることで、基本となる機能を一番最初のクラス（親クラス）に定義して、
子クラスでその機能を継承していくことができます。
そしてここでは３つ目のクラス（子クラス）
にはそれ特有の機能を定義して加えていくことができるということになっています。
こうすると、コードがスッキリしているのがわかりますね。
これをクラスの継承無しで同じ結果になるように書いてみるとこうなってしまいます。
"""

class HondaCar():
	def drive(self):
		print('車を走らせます。')

	def motor_drive(self):
		print('モーターで車を走らせます。')

class CivicCar():
	def drive(self):
		print('車を走らせます。')

class NsxCar():
	def drive(self):
		print('車を走らせます。')

	def motor_drive(self):
		print('モーターで車を走らせます。')

	def track_mode(self):
		print('サーキット走行モードで走らせます！')

"""
上のコードと比較して見るとわかると思いますが、
コードが増えますし、同じメソッドをあちこち定義しないといけないので
とても非効率ですよね。
これがクラス継承との違いになります。
"""


print("--- メソッドのオーバーライド ---")


"""
新しいクラスである子クラスは親クラスの機能を全て継承します。
その継承した機能を変更して利用したい場合は
メソッドを上書きして使うことができます。
これをメソッドのオーバーライドと言います。
これまで使ってきたコードを利用して見てみましょう。
"""

class HondaCar():
	def drive(self):
		print('車を走らせます。')

	def motor_drive(self):
		print('モーターで車を走らせます。')

class CivicCar(HondaCar):
	def drive(self):    # メソッドのオーバーライド
		print('車を燃費良く走らせます。')

class NsxCar(HondaCar):
	def drive(self):    # メソッドのオーバーライド
		print('車をスポーティに走らせます。')
	
	def track_mode(self):
		print('サーキット走行モードで走らせます！')

civic_car = CivicCar()
civic_car.drive()    # 車を燃費良く走らせます。

nsx_car = NsxCar()
nsx_car.drive()    # 車をスポーティに走らせます。

"""
親クラスと同じメソッド名を定義して異なる結果を表示するコードに変えています。
ここがオーバーライドした部分です。
このコードを実行して、オーバーライドしたメソッドを呼び出してみましょう。

クラスを継承していますが、親クラスと同じメソッドを呼び出しても
オーバーライドすれば親とは違う結果を得ることができるということがわかりますね。
"""


print("--- superで親クラスのメソッドを取得 ---")


"""
このコードをさらに使って行きます。親クラスに初期化メソッドを定義します。
engineというデフォルト引数を与えています。ここではNoneとしています。
こうすると引数を利用して継承先のクラスをインスタンス化してオブジェクトにすれば、
クラス変数として利用することができます。
"""

class HondaCar():
	def __init__(self, engine=None):    # 初期化メソッドでengine名を引数として設定
		self.engine = engine

	def drive(self):
		print('車を走らせます。')

	def motor_drive(self):
		print('モーターで車を走らせます。')

class CivicCar(HondaCar):
	def drive(self):
		print('車を燃費良く走らせます。')

class NsxCar(HondaCar):
	def drive(self):
		print('車をスポーティーに走らせます。')

	def track_mode(self):
		print('サーキット走行モードで走らせます')

civic_car = CivicCar('1.5L VTEC TURBO')    # engine名を設定
print(civic_car.engine)    # 1.5L VTEC TURBO

nsx_car = NsxCar('3.5L V6 DOHC ツインターボ+3モーター')    # engine名を設定
print(nsx_car.engine)    # 3.5L V6 DOHC ツインターボ+3モーター

"""
二つの子クラスにエンジン名をそれぞれ代入してオブジェク化しています。
それをクラス変数にドット（.）でアクセスしてeigine名を出力しています。

これは親クラスの初期化メソッドを継承して利用してるということになります。
ここでCivicCarクラスに初期化メソッドを定義してみます。
"""

class HondaCar():
	def __init__(self, engine=None):
		self.engine = engine

	def drive(self):
		print('車を走らせます。')

	def motor_drive(self):
		print('モーターで車を走らせます。')

class CivicCar(HondaCar):
	def __init__(self, engine='1.5L VTEC TURBO', color='黒'):    # 初期化メソッド
		self.engine = engine
		self.color = color

	def drive(self):
		print('車を燃費良く走らせます。')

class NsxCar(HondaCar):
	def drive(self):
		print('車をスポーティーに走らせます。')

	def track_mode(self):
		print('サーキット走行モードで走らせます！')

civic_car = CivicCar()
print(civic_car.engine)    # 1.5L VTEC TURBO
print(civic_car.color)    # 黒

nsx_car = NsxCar('3.5L V6 DOHC ツインターボ+3モーター')
print(nsx_car.engine)    # 3.5L V6 DOHC ツインターボ+3モーター

"""
コードが長くなったので、CivicCarクラスのところ部分だけ抜き出してみます。

class CivicCar(HondaCar):
    def __init__(self, engine="1.5L VTEC TURBO", color="黒"):  # 初期化メソッド
        self.engine = engine
        self.color = color
    def drive(self):
        print("車を燃費良く走らせます。")

初期化メソッドでengineに値を入れて、さらにcolorとして色を定義してみました。
engine、colorの値をそれぞれselfで保持しています。

こうなるのはいいのですけども、
この初期化によって親クラスの初期化メソッドも全部上書きすることになるので、
selfで値を保持するコードを再度書いてしまうことになります。
engineの部分は親クラスの初期化と全く同じことを書いていますよね。
これを避ける為に、この部分で親クラスの初期化を呼び出すということができます。
これを親クラスの要請と言ったりしますが、superを使って書き換えることができます。
"""

class HondaCar():
	def __init__(self, engine=None):
		self.engine = engine

	def drive(self):
		print('車を走らせます。')

	def motor_drive(self):
		print('モーターで車を走らせます。')

class CivicCar(HondaCar):
	def __init__(self, engine='1.5L VTEC TURBO', color='黒'):
		super().__init__(engine)    # 親クラスの要請
		self.color = color

	def drive(self):
		print('車を燃費良く走らせます。')

class NsxCar(HondaCar):
	def drive(self):
		print('車をスポーティーに走らせます。')

	def track_mode(self):
		print('サーキット走行モードで走らせます！')

civic_car = CivicCar()
print(civic_car.engine)    # 1.5L VTEC TURBO
print(civic_car.color)    # 黒

nsx_car = NsxCar('3.5L V6 DOHC ツインターボ+3モーター')
print(nsx_car.engine)    # 3.5L V6 DOHC ツインターボ+3モーター

"""
このクラスの部分だけ書き換えています。
super()で親クラスを示して、ドット（.）で初期化メソッドを呼んで、
ここにengineを渡しています。
そして、このクラスだけのクラス変数（ここではcolor）
を付け加えているということになっています。
ここではあまりコードに違いがないですが、親クラスの初期化メソッドが、
このengineの部分でもっといろんな処理を行なっている
コードになっているとしたならば、書き換え前のコードにももっと
同じコードを書かなくてはいけないことになってしまいます。
そういう手間をsuperを使った親クラスの要請によって避けることができ、
さらにそのクラスでの独自の独自変数を定義することができるわけです。
このsuperによる親クラスへの要請を使った
全体のコードをあらためて書いておくとこうなります。

superを使う前のコードと同じ結果になっています。
このようにsuper()を使って親クラスのメソッドを呼び出すことができます。
"""


print("--- まとめ ---")


"""
Pythonのクラスは、別のクラスから全ての機能を利用することができます。
これをクラスの継承と言います。
元のクラスを親クラス、スーパークラス、基底クラスと呼び、
機能を引き継いで新しく作ったクラスを子クラス、サブクラス、
派生クラスと呼びます。
継承することで、子クラスでは定義していなかったメソッドを
親クラスの機能を利用して使うことができます。
もちろん、子クラス独自のメソッドを合わせて定義することができます。
継承した親クラスのメソッドを子クラスで使う時に、
同じメソッド名で定義し直すこともできます。
同じメソッド名でも別の動きをさせるように上書きすることができるわけです。
これをメソッドのオーバーライドと言います。
子クラスで初期化メソッドを定義する時、
親クラスと同じような初期化メソッドの内容を書かなくてはならないことがあります。
この手間を避ける為に、superを利用して親クラスの初期化メソッドを
呼び出すことで、そこに値を渡すことができます。
そして独自のメソッドも定義することができます。
"""
