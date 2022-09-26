#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 関数の基本 ---")


print("--- 関数とは ---")


"""
ここまでPythonの様々な変数や制御文について学習してきました。
変数と制御文だけで比較的複雑な処理を作成できるようになるのですが、
処理が大きくなると様々な問題が出てきます。

同じ処理を何回も書く必要がある
処理の記述が散らばる
こういった問題は関数を使用することで解決することができます。
関数とは処理をひとつのブロックにまとめたもので、
1回作れば何度も同じ処理を呼び出すことができます。
また、一連の処理をまとまって記述することができるため可読性を向上させることができます。
関数は引数と呼ばれる入力値に対して処理を行い、
戻り値という値を呼び出し元に返すことができます。
"""


print("--- 基本的な関数の定義と呼び出し ---")


"""
それではPythonの関数を使ってみましょう。Pythonの関数の定義はdef文を使用します。

関数定義
def 関数名(引数):
    処理
    return 戻り値

def文の後ろに関数名を記述し、必要であれば引数を記述します。
def文の次の行からインデントをつけてブロック内に処理内容を記述します。
戻り値が必要である場合はreturnを記述します。
Pythonの引数の記法は様々あるので、次回以降詳しく解説します。
それでは実際に関数を作成してみましょう。
以下のサンプルは2数の和を計算して返す関数です。
"""

def sample_function(x, y):
	z = x + y
	return z

"""
また、作った関数を呼び出す場合は以下のように記述します。

関数の呼び出し
戻り値を格納する変数 = 関数名(引数)

では、先程作成した関数を使ってみましょう。
以下のサンプルでは5行目で引数に1,2を指定してsample_functionを呼び出しています。
また、計算結果である戻り値を変数zに格納しています。
"""

def sample_function(x, y):
	z = x + y
	return z

z = sample_function(1, 2)
print(z)    # 3

"""
なお、returnのない関数は戻り値にNoneが設定されます。
以下の関数は戻り値がなく、Noneが返されzに格納されることが確認できます。
"""

def sample_function(x, y):
	print(x + y)

z = sample_function(1, 2)
print(z)    # 3
# None


print("--- 何もしない関数 ---")


"""
テスト等で処理の記述がない関数を定義したい場合がありますが、
その場合は制御文で学習したpassを使用します。
"""

def sample_function(x, y):
	# 処理なし
	pass


print("--- 関数呼び出しの注意点 ---")


"""
単一のスクリプトの場合、上から処理が実行されるため、関数を呼び出す処理は、
関数の後に記述してください。
例えば、以下のように関数の記述の前に呼び出し処理を実行すると、
NameErrorが発生します。

z = sample_function(1, 2)
print(z)
 
def sample_function(x, y):
    z = x + y
    return z
実行すると、以下のエラーが発生します。

$ python sample.py
Traceback (most recent call last):
  File "sample.py", line 2, in <module>
    z = sample_function(1, 2)
NameError: name 'sample_function' is not defined
"""
