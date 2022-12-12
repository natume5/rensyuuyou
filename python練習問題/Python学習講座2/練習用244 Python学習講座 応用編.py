#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python応用編 ---")
print("--- mojimoji 半角⇔全角の変換 ---")


print("--- mojimoji ---")


"""
自然言語処理の前処理として全半角の変換を行うことが多いと思いますが、
その際に便利なmojimojiというライブラリについて学習します。
全半角処理ができるライブラリは色々あるのですが、
その中でもmojimojiは処理が比較的高速である点に特徴があります。

インストールは以下の通りpipで行います。
一部のlinuxではgcc-c++がインストールがなくエラーが出るかもしれません。
ページ下部の補足を参照してください。

pip install mojimoji

では使い方について見ていきましょう。
"""


print("--- 全角から半角へ変換する ---")


"""
その名もズバリzen_to_hanメソッドを使用します。
kana、digit、asciiというオプションをキーワード引数で指定すると、
カナ、数字、アルファベットの無効化を指定することができます。
"""

import mojimoji

text = 'Ｐｙｔｈｏｎ　パイソン　１０００'
print(mojimoji.zen_to_han(text))
# Python ﾊﾟｲｿﾝ 1000

print(mojimoji.zen_to_han(text, kana=False))
# Python パイソン 1000

print(mojimoji.zen_to_han(text, digit=False))
# Python ﾊﾟｲｿﾝ １０００

print(mojimoji.zen_to_han(text, ascii=False))
# Ｐｙｔｈｏｎ　ﾊﾟｲｿﾝ　1000

"""
特に解説は不要かと思います。
形態素解析の前処理ではkana=Falseのみを指定するケースが多いのではないでしょうか。
"""


print("--- 半角から全角へ変換する ---")


"""
こちらの処理は使う機会があまりないかもしれませんが、
参考のため掲載します。han_to_zenメソッドを使用します。
やはりzen_to_hanと同様、kana、digit、ascii
というオプションをキーワード引数で指定すると、
カナ、数字、アルファベットの無効化を指定することができます。
"""

import mojimoji

text = 'python パイソン　1000'

print(mojimoji.han_to_zen(text))
# ｐｙｔｈｏｎ　パイソン　１０００

print(mojimoji.han_to_zen(text, kana=False))
# ｐｙｔｈｏｎ　パイソン　１０００

print(mojimoji.han_to_zen(text, digit=False))
# ｐｙｔｈｏｎ　パイソン　1000

print(mojimoji.han_to_zen(text, ascii=False))
# python パイソン　１０００


print("--- インストールの補足 ---")


"""
特定の環境ではgcc-c++が無いため以下のエラーが出力されます。

以下のコマンドでgcc-c++をインストールして再度pipコマンドを実行してみてください。

yum install gcc-c++
"""
