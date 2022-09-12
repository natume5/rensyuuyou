#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座---")
print("--- Python入門　クラスメソッドとスタティックメソッド---")


import math


class Coordinate:
	"""座標クラス"""

	def __init__(self):
		"""初期化"""
		self.x = 0
		self.y = 0

	def show_coordinate(self):
		"""座標を表示する"""
		print(self.x, self.y)

	@staticmethod
	def calc_dist(cood1, cood2):
		"""座標の距離を計算します"""
		x = cood1.x - cood2.x
		y = cood1.y - cood2.y
		return math.sqrt((math.pow(x, 2) + math.pow(y, 2)))


cood1 = Coordinate()    # インスタンスを生成する
cood1.x, cood1.y = 100, 100

cood2 = Coordinate()    # インスタンスを生成する
cood2.x, cood2.y = 200, 200

dist = Coordinate.calc_dist(cood1, cood2)    # スタティックメゾットを実行
print(dist)

"""
例えば上のサンプルでは、座標クラスに座標間の距離を計算するメソッドを実装していますが、
オブジェクトの状態に依存する機能ではないため、スタティックメソッドとして実装されています。
このように、スタティックメソッドの挙動としてはクラスに属さないただの関数と同じなのですが、
なんらかの方針で関数をクラスに属させたい場合に使用します。
"""


print("--- Python入門　クラスの継承---")


"""
継承

オブジェクト指向プログラミングをサポートする言語では、大抵継承と呼ばれる機能が実装されています。
あるクラスを定義する際に親となるクラスを指定すると、そのクラスの機能をまるごと引き継ぐことが可能となりますが、
この機能のことを継承と呼びます。

クラス定義と継承

Pythonで既存クラスを継承したクラスを定義する場合は、class文の後方に丸括弧で親クラスを指定します。
なお、これまでのように親クラスを指定しない場合、objectクラスを継承したクラスとなります。

サンプルを見てみましょう。Base、Subという2つのクラスを定義しますが、SubはBaseクラスを継承するものとします。
"""

class Base:
	"""親クラス"""

	def func1(self):
		print('func1')


class Sub(Base):
	"""子クラス"""

	def func2(self):
		print('func2')


obj = Sub()     # 子クラスをインスタンス化
obj.func1()
obj.func2()    # 親クラスのメゾッドも実行可能

"""
上のサンプルでは、継承によりSubクラスのfunc2に加え、
親クラスのfunc1も呼び出すことができていることを確認することができます。

親クラスのメソッドの呼び出し

親クラスのメソッドを呼び出す際は、super()を使用します。
"""

class Base:
	def func1(self):
		print('func1')

class Sub(Base):
	def func2(self):
		super().func1()    # 親クラスのメゾッドを呼び出し
		print('func2')

obj = Sub()
obj.func2()


"""
__init__とsuper

super()を使用すると初期化子__init__を使用してインスタンスの属性を設定することができます。
以下のサンプルは、ユーザを表すUserクラスに対し、それを継承した社員を表すEmployeeクラスを定義しています。
Userは属性としてname、ageを持ち、Employeeは属性として部署departmentを持つものとします。
"""

class User:
	"""
	ユーザークラス
	"""

	def __init__(self, name="", age=0):
		self.name = name
		self.age = age

	def say_name(self):
		print('私の名前は' + self.name + "です。")


class Employee(User):
	"""
	社員クラス
	"""

	def __init__(self, name, age, department):
		super().__init__(name, age)
		self.department = department

	def say_department(self):
		print("私の部署は" + self.department + "です。")


e = Employee("Suzuki", 45, "営業部")
e.say_name()    # 私の名前はSuzukiです。
e.say_department()    # 私の部署は営業部です。

"""
上のサンプルでサブクラスの方に__init__でインスタンス変数departmentが追加されています。


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
		print("名前は" + self.name + "、 所属部署は" + self.department + "です。")


e = Employee("Suzuki", 45, "営業部")
e.say_name()    # 名前はSuzuki、所属部署は営業部です。

"""
このサンプルのように親クラスのメソッドを上書きする操作のことをオーバーライドと呼びます。


多重継承

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

"""
言語によってはアンチパターンとして扱われることもある多重継承ですが、
再利用として非常に有用な手段でもあるためPythonの様々なライブラリで活用されています。
Java等の単一継承言語育ちの方はMixinについて知っておくと利用や設計する際に一役買うかと思います。
"""


print("--- Python入門　プライベートメンバ---")


"""
慣習的な命名規則によるプライベートメンバ

アクセス修飾子とは、生成されたオブジェクトのメンバ（変数やメソッド）
に対して外部からの参照や更新を制御するための修飾子のことです。
オブジェクト指向プログラミングが可能な言語の多くでサポートされている機能なのですが、
以前のページで書いたとおり、Pythonにはアクセス修飾子がありません。
そのかわり、慣習的にアンダースコアで始まる名前 (例えば_xなど)のメンバは、プライベートなメンバとみなします。
ただし、あくまでも「そうみなす」というだけなので外部からのアクセス自体は可能です。

以下、他の言語に馴染みのない方向けにアクセス修飾子に関して補足します。

以下のコードでは、User型の変数name、_ageを直接更新しています。
_ageはprivateとみなしますが、外部から更新されています。
"""

class User:
	"""
	ユーザークラス
	"""

	def __init__(self, name="", age=0):
		self.name = name    # nameは公開
		self.age = age    # ageはprivateとみなす


user = User('Yamada', 45)
user.name = 'Yosida'
user._age = 39    # 普通に外部から更新可能

"""
一方、以下はJavaのコードです。
同様の処理ですが、privateと書かれているメンバを外部から参照したり更新したりすることができません。


public class User {
	
	  public String name;
	  private int age;

	  public User(String name, int age){
		  this.name = name;
		  this.age = age;
	  }

}

public class Main {
	public static void main(String[] args) {
		User user = new User("Yamada", 45);
		user.name = "Yoshida";
		user.age = 39;
	}
}

上のコードはUserクラスにname、ageが設定されています。
nameはpublicというアクセス修飾子が設定されており、外部から参照・更新することが可能です。
実際、16行目でnameをYoshidaに更新しています。
一方、ageはprivateという外部からの更新を不許可にするアクセス修飾子が設定されており、
17行目の更新でコンパイルエラーが発生します。大規模開発を行う際、
他の開発者が外部から勝手にオブジェクトの状態を更新するような事故が多々発生するのですが、
アクセス修飾子を適切に設定することにより、こういった不具合を防ぐことができます。


__変数名による隠蔽

ただしPythonのクラスは「アンダースコア2つで始まり、末尾がアンダースコア1つ以下」となる変数名の場合、
その変数に対して外部からアクセスするとAttributeErrorを発生させることができます。
この仕組みにより実質的なプライベートなメンバを設定することが可能です。
"""
"""
class Sample():
	def __init__(self):
		self.a = 0
		self._b = 0
		self.__c = 0
		self.__d_ = 0
		self.__e__ = 0


obj = Sample()
a = obj.a    # アクセス可能
b = obj._b    # アクセス可能
c = obj.__c    # AttributeError発生
d = obj.__d_    # AttributeError発生
e = obj.__e__    # アクセス可能
"""
"""
上のサンプルでは、a、_bはアクセス可能です。_bはアンダースコアから始まっていますが、アクセスできてしまう点に注意してください。
また、__c、__d_は外部からアクセスすると、AttributeErrorが発生します。

ただし、2つ以上のアンダースコアで終わるメンバはプライベートメンバとはなりません。
（__init__などは特殊メソッドと呼ばれています。別ページにて解説します。）
このため、__e__は名前の末尾がアンダースコア2つで終わるのでアクセス可能です。

とはいえ、前述の通り、完全なプライベート変数は存在しません。実は以下の方法よりアクセスできてしまいます。

c = obj._Sample__c # アクセスできてしまう

この原理はマングリングと呼ばれ、詳しくは公式ドキュメントの以下を参照してください。

    https://docs.python.org/3/tutorial/classes.htmlより引用
    クラスのプライベートメンバについて適切なユースケース(特にサブクラスで定義された名前との衝突を避ける場合)があるので、
    マングリング(name mangling) と呼ばれる、限定されたサポート機構があります。
     __spam (先頭に二個以上の下線文字、末尾に一個以下の下線文字) という形式の識別子は、
     _classname__spam へとテキスト置換されるようになりました。ここで classname は、
     現在のクラス名から先頭の下線文字をはぎとった名前になります。このような難号化 (mangle) は、
     識別子の文法的な位置にかかわらず行われるので、クラス定義内に現れた識別子全てに対して実行されます。

    名前のマングリングは、サブクラスが内部のメソッド呼び出しを壊さずにメソッドをオーバーライドするのに便利です。 
"""


print("--- Python入門　プロパティ---")


"""
属性へのアクセス

これまで見てきたように、Pythonで属性にアクセスする際は [オブジェクト名.メンバ名] の形式で記述しました。
ですが、例えば「参照するときはカッコを付けたい」「更新するときはチェックをしたい」「削除処理を禁止したい」など、
アクセスする際に処理を挿入するような要件がでてくるかもしれません。
この時、専用のsetter、getter、deleterを作成すると問題は解決しますが、
毎回それらの専用メソッドを呼びださなければ効果がでません。
また、クラスを利用する側がかならずそれらのメソッドを利用してくれる保証もありません。
"""

class Sample:

	def __init__(self):
		self.text = 'sample'

	def get_text(self):
		return '({0})'.format(self.text)

	def set_text(self, text):
		if text is None:
			self.text = ""
		else:
			self.text = text

	def delete_text(self):
		pass

# いちいち専用メゾッド経由でアクセスしなければならない・・・・
obj = Sample()

print(obj.get_text())

obj.set_text(None)

obj.delete_text()


"""
プロパティ

これでは、せっかくのgetter、setterなしで気軽にアクセスできるPythonの特徴が活きてきません。
ところが、Pythonには通常のアクセスの記述をしつつ専用メソッド経由で処理を行うプロパティとよばれる組込みデコレータがあります。
上のコードをプロパティを用いて書きなおしてみましょう。
"""

class Sample:

	def __init__(self):
		self.__text = 'sample'

	@property
	def text(self):
		return "({0})".format(self.__text)

	@text.setter
	def text(self, text):
		if text is None:
			self.__text = 'None'
		else:
			self.__text = text

	@text.deleter
	def text(self):
		pass

# 通常のアクセス方法が利用できる！！
obj = Sample()
print(obj.text)

obj.text = None
print(obj.text)

del obj.text
print(obj.text)

"""
通常のアクセスで専用メソッド経由で処理がされるようになりました。以下にプロパティをまとめます。
プロパティ 	          役割
@property 	      getter
@属性名.setter 	  setter
@属性名.deleter 	  deleter


プロパティの注意点

上のコードですが、疑問に思われた点はないでしょうか？
そう、修正したコードはアンダースコアを2つつけたプライベートなメンバ名になっています。
setterを利用する際はかならずプライベートなメンバにしないと、無限再帰処理に入る、という問題が発生します。
仮にプライベートにしない場合、先ほどの処理のsetter部分は以下のようになります。

self.text = text

ここでまたにsetterが呼び出され、さらにsetterが呼び出され、、、というループに入ってしまいますので注意してください。
"""


print("--- Python入門　クラスデコレータ---")


"""
型オブジェクト（クラスオブジェクト）の復習

型オブジェクト（クラスオブジェクト）で説明したとおり、Pythonではクラスもただのオブジェクトですので、
変数にセットして関数の引数や戻り値として扱うことができます。
"""

def add_member(cls):
	"""型オブジェクト(クラスオブジェクト)に対し属性を追加する"""

	cls.x = 'sample'

	return cls

class Sample:
	"""何もしないクラス"""
	pass

NewSampleCls = add_member(Sample)    # Sampleクラスから新たなクラスを作成する
obj = NewSampleCls()    # 新たなクラスをインスタンス化する
print(obj.x)    # Sampleクラスにはなかった属性xが取得できる

"""
add_member関数は、型オブジェクトに対し、属性xを追加する関数です。
また、Sampleクラスには属性がありません。
ここでSampleクラスをadd_member関数に渡すと、属性xを持つクラスが新たに作成されます。

実際にインスタンス化してみると、属性xを持つことが確認できます。


クラスデコレータ

勘の良い方ならもうお気づきかもしれません。
そう、クラスデコレータは関数デコレータのクラス版、つまりクラスの機能を追加・変更するデコレータです。
上のコードをデコレータを使った記述に変えてみましょう。
"""

def add_member(cls):
	"""型オブジェクト(クラスオブジェクト)に対し属性を追加する"""

	cls.x = 'sample'

	return cls

@add_member
class Sample:
	"""何もしないクラス"""
	pass


obj = Sample()    # Sampleクラスをインスタンス化する
print(obj.x)    # Sampleクラスにはなかった属性xが取得できる

"""
関数デコレータと同様に、元のクラスに変更を加えることなく機能追加をすることができました。
"""
