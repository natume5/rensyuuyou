#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- bool(真理値)型 ---")


print("--- Pythonのbool(論理)型 ---")


"""
bool型とは真理値、つまり真偽を表す変数の型です。
Pythonのbool型は一般的なプログラミング言語と同様、
以下の真偽2値が用意されています。

値 	    意味
True 	真
False 	偽


論理演算

Pythonのbool型はor、and、notというキーワードで論理演算することが可能です。
それぞれ、論理和、論理積、否定となります。
（論理演算についてご存知でない方はページ下の補足を参照してください。）

ではサンプルです。
"""

b1 = True
b2 = False

b3 = b1 or b2    # 論理和
print(b3)    # Trueが出力される

b4 = b1 and b2    # 論理積
print(b4)    # Falseが出力される

b5 = not b1    # 否定
print(b5)    # Falseが出力される

"""
それぞれ論理演算された結果が出力されます。

また、Pythonは複数の変数に対して論理演算を並べて記述することが可能です。
"""

b1 = True
b2 = False
b3 = True


b = b1 and b2 and b3
print(b)    # False

b = b1 or b2 and b3
print(b)    # True

"""
複数の論理演算を行う場合、演算子の優先順位は高い順にnot、and、orとなります。
ただし、可読性の観点から以下のように括弧をつけることをおすすめします。

b = b1 or (b2 and b3)
"""


print("--- 比較演算子とbool型 ---")


"""
数値の比較演算子の演算結果はbool型となります。
サンプルを見てみましょう。
"""

x = 100
y = 200

b1 = (x < y)    # 100 < 200は正しいので真
print(b1)    # Trueが出力される

b2 = (y < x)    # 100 > 200は誤りなので偽
print(b2)    # Falseが出力される

"""
比較演算子を括弧でくくっていますが、なくても正常に動作します。
ただし可読性が落ちますのでやはりこちらも
演算の優先順位を表すために括弧をつけることをおすすめします。
"""


print("--- TIPS ---")


"""
Pythonのbool型はint型のサブクラスとして定義されています。
このため、int型に変換することが可能です。
また、int型で用意されている各種メソッドも利用することができます。
"""

b1 = True
b2 = False

print(int(b1))    # 1が出力される
print(int(b2))    # 0が出力される


print("--- 補足　論理演算とは ---")


"""
プログラミング初学者向けに論理演算の初歩に関する補足をします。
真と偽を表す論理値に対し、否定、論理和、論理積３種類の演算が定義されています。
今後学習する、条件分岐（条件によって処理を変化させる制御のこと）等で活躍します。

否定

否定とは、変数が真の場合は偽に、偽の場合は真に変換する演算です。

bool値 	not演算結果
True 	False
False 	True


論理和

論理和は２つの論理変数に対し、一方でもTrueであれば結果をTrueとして返す演算です。

変数1 	変数2 	or演算結果
True 	True 	True
True 	False 	True
False 	True 	True
False 	False 	False

「２つ条件があり、そのうちひとつでも条件を満たしている場合」を表したい場合に使用します。


論理積

論理積は２つの論理変数に対し、両方ともTrueであれば結果をTrueとして返す演算です。

変数1 	変数2 	and演算結果
True 	True 	True
True 	False 	False
False 	True 	False
False 	False 	False

「２つ条件があり、両方条件を満たしている場合」を表したい場合に使用します。
"""
