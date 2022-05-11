#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("---Pythonで関数を定義・呼び出し（def, return）---")


"""
Pythonにおいて関数の定義と呼び出し（実行）を行う方法について説明する。

    Pythonにおける関数の定義・呼び出しの基本
    引数の基本的な使い方
        位置引数: 位置で指定
        キーワード引数: キーワードで指定
        位置専用引数とキーワード専用引数
    デフォルト引数: デフォルト値を設定（呼び出し時に省略可能）
    可変長引数: 任意の数の引数を指定
    呼び出し時にリストや辞書を展開（アンパック）して引数に指定
    戻り値（返り値）を指定: return
        returnの基本
        Noneを返す関数
        複数の戻り値を指定
"""
"""
Pythonにおける関数の定義・呼び出しの基本

Pythonにおいて、関数はdefブロックで定義する。括弧()内に引数、returnで戻り値を指定する。

def 関数名(引数1, 引数2, ...):
    処理
    return 戻り値

呼び出すときは以下の通り。

関数名(引数1, 引数2, ...)

実際の例。
"""
def add(a, b):
	x = a + b
	return x

x = add(3, 4)
print(x)    # 7

"""
引数とreturnによる戻り値は必要なければ省略できる。
"""
def hello():
	print("Hello")

print(hello())    # Hello

"""
引数および戻り値についての詳細は以下で説明する。

なお、Pythonのコーディング規約PEP8ではdefブロックの前後は2行ずつ空けることが推奨されているが、
サンプルコードでは便宜上1行しか空けていない。
"""


"""
引数の基本的な使い方

引数は関数名()のカッコ内にカンマ区切りで指定して定義する。
例は引数をそのまま出力するだけの関数。f文字列を使っている。
"""
def func(a, b, c):
	print(f'a={a}, b={b}, c={c}')

"""
呼び出し時には引数の位置（順番）またはキーワード（引数名）によって値が渡される。
"""


"""
位置引数: 位置で指定

呼び出し時に指定した値は位置（順番）に従って関数に渡される。
"""
func(1, 10, 100)     # a=1, b=10, c=100

"""
呼び出し時に指定する引数と定義した引数の数が一致しないとエラー（TypeError）となる。

# func(1)
# TypeError: func() missing 2 required positional arguments: 'b' and 'c'

# func(1, 10, 100, 1000)
# TypeError: func() takes 3 positional arguments but 4 were given
"""


"""
キーワード引数: キーワードで指定

呼び出し時に引数名=値として値を渡すこともできる。この場合は任意の順番で指定可能。
"""
func(b=10, c=100, a=1)    # a=1, b=10, c=100

"""
すべての引数をキーワードで指定する必要はなく、位置で指定したあとキーワードで指定することもできる。
ただし、キーワードで指定した以降の引数はすべてキーワードで指定しないとエラー（SyntaxError）となる。

func(1, c=100, b=10)
# a=1, b=10, c=100

# func(a=1, 10, 100)
# SyntaxError: positional argument follows keyword argument
"""


"""
位置専用引数とキーワード専用引数
位置専用引数（Python3.8以降）

関数定義時の引数に/を用いると、/より前の引数が位置専用引数となる。

位置専用引数をキーワードで指定するとエラー（TypeError）となる。
/より後ろの引数は位置でもキーワードでも指定可能。
"""
def func_pos_only(a, b, /, c):
    print(f'a={a}, b={b}, c={c}')
"""
# func_pos_only(a=1, b=10, c=100)
# TypeError: func_pos_only() got some positional-only arguments passed as keyword arguments: '
"""
func_pos_only(1, 10, 100)    # a=1, b=10, c=100
func_pos_only(1, 10, c=100)		# a=1, b=10, c=100
"""
func(a, b, c, /)のように最後に/を用いて関数を定義すると、すべての引数が位置専用引数となる。

位置専用引数はPython3.8で導入された構文で、それより前のバージョンでは使えない。
"""


"""
キーワード専用引数

関数定義時の引数に*を用いると、*より後ろの引数がキーワード専用引数となる。

キーワード専用引数はキーワードで指定しないとエラー（TypeError）となる。
*より前の引数は位置でもキーワードでも指定可能。キーワードは任意の順番で指定できる。
"""
def func_kw_only(a, b, *, c):
	print(f'a={a}, b={b}, c={c}')
"""
# func_kw_only(1, 10, 100)
# TypeError: func_kw_only() takes 2 positional arguments but 3 were given
"""
func_kw_only(1, 10, c=100)    # a=1, b=10, c=100

func_kw_only(1, c=100, b=10)    # a=1, b=10, c=100

"""
func(*, a, b, c)のように最初に*を用いて関数を定義すると、すべての引数がキーワード専用引数となる。
"""


"""
位置専用引数とキーワード専用引数の組み合わせ

/と*を同時に用いることもできる。/より前は位置専用引数、*より後はキーワード専用引数となる。
/と*の間の引数は位置でもキーワードでも指定可能。
"""
def func_pos_kw_only(a, /, b, *, c):
	print(f'a={a}, b={b}, c={c}')

"""
# func_pos_kw_only(1, 10, 100)
# TypeError: func_pos_kw_only() takes 2 positional arguments but 3 were given

# func_pos_kw_only(a=1, b=10, c=100)
# TypeError: func_pos_kw_only() got some positional-only arguments passed as keyword arguments: 'a'
"""
func_pos_kw_only(1, 10, c=100)    # a=1, b=10, c=100

func_pos_kw_only(1, c=100, b=10)    # a=1, b=10, c=100

"""
*より前に/を使うとエラー（SyntaxError）。

# def func_pos_kw_only(a, *, b, /, c):
#     print(f'a={a}, b={b}, c={c}')
# SyntaxError: invalid syntax

"""


"""
デフォルト引数: デフォルト値を設定（呼び出し時に省略可能）

関数定義時に引数名=デフォルト値とすると引数のデフォルト値を設定できる。

デフォルト値を設定しておくと呼び出し時に引数の指定を省略可能。別の値を指定すれば当然その値が使われる。
"""
def func_default(a, b, c=100):
	print(f'a={a}, b={b}, c={c}')

func_default(1, 10)    # a=1, b=10, c=100

func_default(1, 10, 200)    # a=1, b=10, c=200

"""
関数定義時にデフォルト引数を通常の引数（デフォルト値を指定していない引数）
の前に置くとエラー（SyntaxError）になる。

# def func_default(a=1, b, c=100):
#     print(f'a={a}, b={b}, c={c}')
# SyntaxError: non-default argument follows default argument

リストや辞書をデフォルト値とした場合は関数呼び出し時と常に同じオブジェクトが使われるので注意が必要。
"""


"""
可変長引数: 任意の数の引数を指定

関数定義時に引数名に*と**をつけると可変長引数となり、呼び出し時に任意の数の引数を指定できる。

慣例として*args, **kwargsという名前が使われることが多いが、*と**が頭についていれば他の名前でも問題ない。
*args: 複数の引数をタプルとして受け取る

*をつけると複数の引数がタプルとして受け取られる。
"""
def func_args(*args):
    print(args)

print(func_args(1, 10))    # (1, 10)

print(func_args(1, 10, 100, 1000))    # (1, 10, 100, 1000)


"""
**kwargs: 複数のキーワード引数を辞書として受け取る

**をつけると複数のキーワード引数が辞書として受け取られる。
"""
def func_kwargs(**kwargs):
    print(kwargs)

print(func_kwargs(a=1, b=10))    # {"a": 1, "b": 10}

print(func_kwargs(c=1, b=10, d=1000, a=100))    # {"c": 1, "b": 10, "d": 1000, "a": 100}

"""
位置引数との組み合わせや、*argsと**kwargsとの組み合わせ時は順番に注意が必要。
"""


"""
呼び出し時にリストや辞書を展開（アンパック）して引数に指定
リストやタプルを展開して指定

関数呼び出し時にリストやタプルに*をつけて指定すると、
要素が展開（アンパック）され順番に位置引数として指定される。
要素数と引数の数が一致していないとエラー（TypeError）になる。
"""
def func(a, b, c):
    print(f'a={a}, b={b}, c={c}')

l = [1, 10, 100]
print(func(*l))    # a=1, b=10, c=100

"""
l = [1, 10]
# func(*l)
# TypeError: func() missing 1 required positional argument: 'c'
"""


"""
辞書を展開して指定

関数呼び出し時に辞書に**をつけて指定すると、要素のキーが引数名、
値が引数の値として展開されてキーワード引数として指定される。
引数名と一致するキーが無かったり、一致しないキーがあったりするとエラー（TypeError）になる。
"""
d = {"a": 1, "b": 10, "c": 100}
print(func(**d))    # a=1, b=10, c=100

"""
d = {'a': 1, 'b': 10, 'x': 100}
# func(**d)
# TypeError: func() got an unexpected keyword argument 'x'
"""


"""
戻り値（返り値）を指定: return
returnの基本

関数の戻り値（返り値）はreturn文で指定する。
"""
def func_return(a, b):
    return a + b

x = func_return(3, 4)
print(x)     # 7

print(type(x))    # <class 'int'>

"""
戻り値の型は引数および関数の処理に依存する。
"""
x = func_return(0.3, 0.4)
print(x)    # 0.7

print(type(x))    # <class "float">


"""
Noneを返す関数

関数においてreturnは必須ではなく、何らかの処理を実行するだけで値を返す必要がなければ省略できる。

returnを省略した関数はNoneを返す。
defブロックに何も書かないとエラーになるのでサンプルコードでは何もしないpassを使っている。
"""
def func_none():
    # do something
    pass

x = func_none()
print(x)    # None

"""
returnのあとの値を省略した場合もNoneが返される。
"""
def func_none2():
    return

x = func_none2()
print(x)    # None

"""
もちろん、明示的にreturn Noneと書いてもよい。
"""
def func_none3():
    return None

x = func_none3()
print(x)    # None


"""
複数の戻り値を指定

return文のあとに複数の値をカンマ区切りで指定するとタプルが返される。
"""
def func_return_multi(a, b):
    return a + b, a * b, a / b

x = func_return_multi(3, 4)
print(x)    # (7, 12, 0.75)

print(type(x))    # <class 'tuple'>

"""
それぞれの値をアンパックして別々の変数に代入することも可能。
"""
x, y, z = func_return_multi(3, 4)
print(x)    # 7

print(y)    # 12

print(z)    # 0.75

