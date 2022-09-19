#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- イミュータブルとid関数 ---")


"""
ここではプログラミングするにあたり重要な概念、
イミュータブル（=変更不可性）について説明します。
"""


print("--- イミュータブルとは ---")


"""
イミュータブルとは
イミュータブルとは、後から値を変更することができない性質を指します。
ここまでさまざまな基本的な変数の型について学習してきましたが、
以下の変数はイミュータブルです。

bool型
数値型
文字列型
タプル型
range型
上の文章を読んで、以下のような反論を思いつく方がいるかもしれません。

text = "abc"
text = "def"

「変数textに"abc"を定義して、あとから"def"に変更した、
つまり文字列は変更できたのではないか？」と思われた方は、
再度変数への再代入を参照してみてください。
代入という操作では、元々あった値（つまりハコの中身）は変更されないのです。
"""


print("--- id関数とオブジェクトの同一性 ---")


"""
上で述べたとおり、Pythonの文字列型はイミュータブル、
つまり生成後にオブジェクトの状態を変更することができない型です。
以前学習した通り、再度代入したり、+演算子で結合する操作ができますが、
こういった操作をした場合は元のオブジェクトとは異なるオブジェクトが生成されます。
組込みのid関数について学習した後、
文字列がイミュータブルであることを確認してみましょう。


id関数
Pythonのオブジェクトには、固有の番号が振られています。
組込みのid関数はそのオブジェクトの固有の番号を取得します。
"""

num = 100
text = 'aaaa'
dic = {'key': 200}

print(id(num))    # 2014554445264
print(id(text))    # 2014560942256
print(id(dic))    # 2014560942144

"""
同じオブジェクトであれば同じ番号を取得することができます。


文字列型の同一性確認

では確認してみましょう。
"""

text1 = 'aaa'
text2 = text1
text3 = text1 + 'bbb'

print(id(text1))    # 2735581978928
print(id(text2))    # 2735581978928 text1を参照しているためtext1と同じID
print(id(text3))    # 2735585228208 text1とはIDが異なる

text1 = 'bbb'
print(id(text1))    # 1855498659568 もともとのIDとは異なる

"""
変数text1という文字列に対し、text2は参照先がtext1なのでIDが同じです。
しかし、text1に文字列を加えた場合はIDが変わっていることが確認できます。
また、text1に対し別の文字列を代入しても
やはりIDが代わり元のオブジェクトとは別のオブジェクトが生成されたことが確認できます。
"""
