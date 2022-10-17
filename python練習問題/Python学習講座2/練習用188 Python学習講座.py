#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 例外処理 ---")


print("--- 例外と例外処理 ---")


"""
プログラム実行には様々な前提があります。
例えば、割り算を計算する場合、分母は0以外でなければなりません。
ところが、こういった前提が満たされない例外的な事態が発生した場合、
エラーとなりプログラムが中断されます。
こういった状態的な事態を「例外が発生した」と故障します。
前述のとおり例外が発生した場合はプログラムが中断されますが、
プログラムの規模が大きくなると即時プログラムを中断すると
様々な問題が発生します。
軽微なものであったらプログラムを続行させたり、
プログラムの中断までに原因をログ出力したり、
安全に終了するための措置をとる必要があります。
この発生した例外に対して何らかの処理をすることを例外処理と呼びます。
また、この例外を捉えることを例外の捕捉と呼びます。
"""


print("--- 例外処理の基本 ---")


"""
Pythonの例外処理は例外が発生する可能性のある箇所をtryブロックに囲み、
exceptで例外の種類を指定して補足します。
以下のコードは0で割り算した場合に発生する例外ZeroDivisionErrorを捕捉し、
除数がゼロである旨を表示しています。
"""

x = 1000
y = 0

try:
	z = x / y
	print(z)
except ZeroDivisionError:
	print('除数に0が指定されました')
# 除数に0が指定されました

"""
上のサンプルでは0除算の例外のみ補足できますが、
以下のように例外の種類を省略すると、全ての例外が補足されます。
"""

try:
	z = x / y
	print(z)
except:
	print('除数に0が指定されました')
# 除数に0が指定されました

"""
ただし、この書き方は例外捕捉の意図が不明確であるため
一般的に推奨されていません。
"""


print("--- 例外オブジェクトの利用 ---")


"""
例外を補足した際にasで例外オブジェクトを変数として指定し、
情報を取得することができます。

except 例外クラス as 変数名

例えば例外オブジェクトの情報を参照したい場合は以下のように書きます。
"""

try:
	z = x / y
	print(z)
except ZeroDivisionError as e:
	print("除数に0が指定されました")
	print(type(e), str(e))
# 除数に0が指定されました
# <class 'ZeroDivisionError'> division by zero


"""
様々な例外と継承関係

例外は上で紹介したZeroDivisionErrorに様々な種類が用意されています。
また、例外クラスは継承関係をもっています。
BaseExceptionクラスがすべての例外の親クラスとなります。
次ページで説明する独自例外クラスを
実装する際の親となるものがExceptionクラスです。
代表的な組込みの例外の継承関係を以下に示します。

BaseException ←全ての例外の親クラス
+-- SystemExit
+-- KeyboardInterrupt
+-- GeneratorExit
+-- Exception　←独自例外の親クラス
+-- StopIteration ← イテレータを使用した際に、次の値が無いのにnextした場合に発生
+-- ArithmeticError
| +-- OverflowError ← オーバーフローした場合に発生
| +-- ZeroDivisionError ← 0で除算した場合に発生
|
+-- AssertionError ← アサートエラー
+-- AttributeError ← 存在しない属性を参照した際に発生
+-- ImportError ← インポートに失敗した際に発生
+-- LookupError
| +-- IndexError ← シーケンスに対し存在しないインデックスでアクセスした場合に発生
| +-- KeyError ← 辞書位に対し存在しないキーでアクセスした場合に発生
+-- NameError
| +-- UnboundLocalError
+-- OSError ←システム関連のエラー
| +-- FileExistsError　←　すでに存在するファイルやディレクトリを作成しようとした場合に発生
| +-- FileNotFoundError　←　要求されたファイルやディレクトリが存在しない場合に発生
| +-- PermissionError　←　ファイルアクセス時に十分な権限がない場合に発生
| +-- TimeoutError ←　システム関数がタイムアウトした場合に発生
+-- RuntimeError ← 他のどのカテゴリにも属さないエラーや不明なエラー
+-- SyntaxError ← 文法エラー
| +-- IndentationError ← 不正なインデントがある場合に発生
| +-- TabError ← タブとスペースを一貫しない方法でインデントに使っている場合に発生
+-- TypeError　← 組み込み演算、もしくは関数が適切でない型のオブジェクトに対して適用された場合に発生
+-- ValueError ← 組み込み演算や関数が、正しい型だが適切でない値を受け取った場に発生
+-- Warning ← 警告

捕捉対象に親例外を指定すると、継承した例外も捕捉することが可能です。
例えば、先ほどのサンプルコードではZeroDivisionErrorを使って
例外を補足していましたが、（良し悪しはさておき）
かわりにArithmeticErrorやExceptionを使用することも可能です。
同じ理屈でExceptionを指定すると大抵の例外を捕捉することができます。
Pythonの例外は上で紹介したとおり組み込みで多数提供されているため、
公式ドキュメントを参照して適切なものを選ぶようにしてください。
"""


print("--- 複数の例外を補足する ---")


"""
exceptのブロックを列挙することで複数の例外を捕捉することが可能です。
以下のサンプルでは、辞書に格納された変数x、yで割り算を計算しています。
この処理で発生しうる例外として辞書に値が存在しない、
除数が0などが挙げられますが、それらを複数記述して補足しています。
"""

param = {'x': 1000, 'z': 0}

try:
	x = param['x']
	y = param['y']
	z = x / y
	print(z)

except KeyError as e:    # 辞書に存在しない場合の例外を補足
	print('処理に必要なデータが存在しません')

except ZeroDivisionError as e:    # 0除算を補足
	print('除数に0が指定されました')

except:    # 全ての例外を補足
	print('原因不明のエラーが発生しました')
# 処理に必要なデータが存在しません


print("--- else / finally ---")


"""
for文と同様に、tryブロック中で例外が発生しなかった場合、
elseブロック内部の処理が実行されます。
また、tryブロック中での例外発生有無にかかわらず
finallyブロックが実行されます。
"""

try:
	z = x / y
	print(z)

except ZeroDivisionError as e:
	print("1")

else:
	print('2')

finally:
	print('3')
# 1
# 3

"""
例えば、上記コードでyの値が0の場合は例外が発生するため1と3が出力されます。
また、yの値が0以外の場合は例外が起こらず2と3が出力されます。
"""
