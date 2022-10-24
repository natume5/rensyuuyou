#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- モジュール ---")


print("--- 外部モジュールのimport ---")


"""
外部モジュールのimport

これまで既に何度か登場しましたが、
標準ライブラリなどのモジュールを使用する際はimport文を使用します。
例えば、標準ライブラリのmathモジュールを使用する場合、
以下のようにimportします。
"""

import math

print(math.pi)    # 3.141592653589793

"""
mathモジュールの一部、例えば円周率の定数piだけ使用したい場合は
from文と合わせて以下のように記述することもできます。
また、この場合はmath.を書かずに使用することができます。
"""

from math import pi

print(pi)    # 3.141592653589793

"""
asによる別名

さらに、importしたモジュールが長い場合、asで別名を付けることができます。
例えばnumpyという数値計算モジュールでランダムな点を生成する場合、
以下のように記述します。
"""

import numpy

x = numpy.random.rand(50)
y = numpy.random.rand(50)

"""
モジュールを利用するたびにnumpyと書かなければなりませんが、
これにasで以下のように短い名前をつけることができます。
"""

import numpy as np

x = np.random.rand(5)
y = np.random.rand(5)
print(x, y)
# [0.23154078 0.87389131 0.49097312 0.76053339 0.43955295]
#  [0.45375763 0.70490487 0.9624096  0.43334842 0.78591361]

"""
モジュールと同名のクラス

Pythonのモジュールimportで初学者が少し混乱するのが
モジュール名と同じ名前のクラスや関数がある場合です。
たとえば、標準ライブラリのdatetimeモジュールには
datetimeという型が存在します。
利用する場合、以下のようにimportします。
"""

import datetime
# datetimeモジュールのdatetimeをインポート

dt_obj = datetime.datetime(2017, 12, 22)
# datetime型のオブジェクトを生成する

"""
また、fromを使うと以下のように書き換えることができます。
"""

from datetime import datetime
# datetimeモジュールのdatetimeをインポート

dt_obj = datetime(2017, 12, 22)
# datetime型のオブジェクトを生成する


print("--- 独自モジュールの作成 ---")


"""
次に独自にモジュールを作成して使用みましょう。
拡張子がpyとなるPythonスクリプトを作成し、別のスクリプトから呼び出します。

単一モジュールのimport

まずはmod1.pyという名前の簡単なモジュールを作成します。

# mod1.py
def func1():
    print('func1')

同じディレクトリにrun.pyという実行スクリプトを作成します。

# run.py
import mod1
mod1.func1() # mod1.pyのfunc1関数が呼び出される。


パッケージ化

もう少しモジュールの数を増やしてそれらをまとめたパッケージを作ってみましょう。
先ほど作ったrun.pyと同じディレクトリ内にmypkg
というパッケージディレクトリを作成します。mypkgの中に、
mod2.py、mod3.pyというモジュールを作成してみましょう。

# ./mypkg/mod2.py
def func2():
    print('func2')

# ./mypkg/mod3.py
class MyClass():
    def method3(self):
        print('method3')

さらに、パッケージには_init__.pyという空ファイルを配置します。
これはディレクトリがパッケージであることを示す目印となります。

階層は以下のようになります。

$ tree
.
├── mod1.py
├── mypkg
│   ├── __init__.py
│   ├── mod2.py
│   └── mod3.py
└── run.py

最後にモジュール伸び出しのrun.pyを以下のように記述します。
"""

import mod1
from mypkg import mod2, mod3

mod1.func1()
mod2.func2()
mod3.MyClass().method3()
# func1
# func2
# method3
"""
実行してみると、それぞれのモジュールを呼び出すことが確認できます。


__init__.pyの活用

さて、先ほど空のファイルだった__init__.pyですが、
以下のように修正してみましょう。

# ./mypkg/__init__.py
from . import mod2
from . import mod3   

すると、run.py側では、以下のように呼び出すこともできます。

import mod1
import mypkg

mod1.func1()
mypkg.mod2.func2()
mypkg.mod3.MyClass().method3()

mypkgをimportすると、配下のものもimportされていることが確認できますね。
"""
