#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- 関数オブジェクト ---")


print("--- オブジェクトとしての関数 ---")


"""
Pythonはこれまでに学習してきた様々な変数の型と同様、
関数も変数に代入して扱うことができます。
以降、このように関数を変数として扱う場合の関数を当サイトでは
関数オブジェクトと呼称することにします。
サンプルで見てみましょう。
"""

def sample_function():

	text = 'sample'
	print(text)    # sample
	return '戻り値'

text = sample_function()    # 通常の呼び出し
print(text)    # 戻り値

f = sample_function    # 関数オブジェクトとして変数fに格納

text = f()     # sample　関数オブジェクトを実行
print(text)    # 戻り値　戻り値も取得できる

"""
1行目から簡単な関数が定義されています。
8行目9行目では普通に関数を呼び出し、戻り値を取得して出力しています。
前述のとおり、関数をオブジェクトとして変数に格納することが可能で、
11行目にそれを行っています。13行目、14行目で実行、戻り値の出力を行っています。
関数宣言の引数として関数を渡すこともできます。
もうひとつ例を見てみましょう。
"""

def param_func():
	return 'サンプル'

def sample_function(f):
	x = f()
	print(x)    # サンプル

sample_function(param_func)

"""
8行目でsample_function関数を実行していますが、
引数としてparam_func関数を指定しています。
sample_function関数内部の5行目でparam_func関数が実行されて、
6行目の出力でそれが確認できます。
関数を変数として扱うと、様々なトリックを使えるようになります。
最初は何の役に立つのか理解できないかもしれませんが、
色んな場面で大活躍するので覚えておいてください。
"""





