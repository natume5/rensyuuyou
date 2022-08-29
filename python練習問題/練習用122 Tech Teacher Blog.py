#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Tech Teacher Blog ---")
print("--- Pythonのstrip()をマスターしよう！文字削除法まとめ ---")


"""
Pythonでは、必要のない文字列を削除できる「stripメソッド」が備わっています。

よく使用されるメソッドですが、

「どのように空白文字を削除するのか分からない」
「特定の文字を削除するのか分からない」
「stripメソッドについて網羅的に知りたい」

などの悩みもあるでしょう。

そこで今回は、stripメソッドの基礎知識から空白文字や特定文字の削除の仕方、
さらにlstripメソッド・rstripメソッドとの違いに至るまで詳しく説明していきますね。
"""


print("--- stripメソッドについて ---")


"""
「strip( )メソッド」とは、Pythonの組み込み関数の1つで、
両端にある特定の文字列や空白文字を削除するメソッドですよ。
入力フォームから文字列を取得して処理を実行したり、複数行のテキストデータを行ごと、
さらには単語ごとに分解してテキスト解析を実行したりする場合に、
文字列の末尾にスペースや改行コードが入ってしまったというケースに役立ちます。

stripメソッドの構文は次のようになっています。
1.　文字列 .strip ( )

このように、stripメソッドは文字列メソッドなので
先頭に削除したい必要ない文字を含んだ文字列を記述し、
カッコの中に引数として削除したい文字を指定します。
削除したい文字は複数指定することができます。
引数を指定しないということもでき、
その場合はデフォルトでいくつかの不必要な文字を自動的に削除してくれます。
"""


print("--- stripメソッドの使い方 ---")


"""
ここからは実際にコードを用いてstripメソッドの使い方を説明します。

    空白文字の削除
    特定文字の削除

それでは見ていきましょう。
空白文字の削除

stripメソッドの引数に何も指定しない場合、自動で空白文字を削除します。
では、実際にコードを用いて説明しましょう。
"""

# 引数を省略して実行
rawStr = ' Hello, World '    # 半角スペースで空欄を表示
newStr = rawStr.strip()

print(rawStr)    #  Hello, World
print(newStr)    # Hello, World

"""
このように、文字間の空白は削除されません。
また、スペースと同じように改行も自動的に削除されます。
"""

rawStr = '\nHello, World\n'    # 「\n」改行コード
newStr = rawStr.strip()

print(rawStr)    # Hello, World
print(newStr)    # Hello, World

"""
上記の結果から、rawStr変数では前後に改行が入って表示されているのが分かるでしょう。
しかし、stripメソッドを使用したあとの文字列newStrでは改行が削除されていることが分かりますね。

空白文字は以下の通りです。

    半角スペース
    全角スペース
    「\n」改行
    「\f」改ページ
    「\t」タブ
    「\v」垂直タブ
    「\r」復帰


特定文字の削除

strip( )の引数に削除する文字を指定すると特定の文字を削除することができますよ。
"""

rawStr = 'aaaHello, Worldaaa'
newStr = rawStr.strip('aaa')

print(rawStr)    # aaaHello, Worldaaa
print(newStr)    # Hello, World

"""
先頭と末尾に「aaa」という文字列が入っていましたが、しっかりと削除されていることが分かりますね。
"""


print("--- lstripメソッドとrstripメソッドの違いについて ---")


"""
ここからはlstripメソッドとrstripメソッドの基礎知識や使い方について説明していきます。
最後にstripメソッド・lstripメソッド・rstripメソッドの違いについてまとめますので、
ぜひ最後までご覧ください。


lstripメソッドとは

stripメソッドは文字列の両端から必要ない文字を削除するメソッドでしたが、
lstripメソッドは「left strip」、つまり左端から文字列を削除するメソッドとなります。

lstripメソッドの構文は下記の通りです。
1.　文字列 . lstrip ( )

それでは実際にコードを用いて説明していきます。
"""

rawStr = 'aaaHello, Worldaaa'
newStr = rawStr.lstrip('aaa')

print(rawStr)    # aaaHello, Worldaaa
print(newStr)    # Hello, Worldaaa

"""
このように左側の文字列、つまり指定した文字列の先頭を削除していることが分かるでしょう。
また、下記のようにlstripメソッドでも空白文字を削除することができますよ。
"""

rawStr = ' Hello, World '
newStr = rawStr.lstrip()

print(rawStr)    #  Hello, World
print(newStr)    # Hello, World


"""
rstripメソッドとは

rstripメソッドは「right strip」、つまり右側の文字列を削除するメソッドです。

rstripメソッドの構文は下記の通りです。
1.　文字列 . rstrip ( )

それでは実際にコードを用いて説明していきます。
"""

rawStr = 'aaaHello, Worldaaa'
newStr = rawStr.rstrip('aaa')

print(rawStr)    # aaaHello, Worldaaa
print(newStr)    # aaaHello, World

"""
このように右側の文字列、つまり指定した文字列の末尾を削除していることが分かるでしょう。
また、下記のようにrstripメソッドでも空白文字を削除することができますよ。
"""

rawStr = ' Hello, World '
newStr = rawStr.rstrip()

print(rawStr)    #  Hello, World
print(newStr)    #  Hello, World


print("--- stripメソッド・lstripメソッド・rstripメソッドの違い ---")


"""
ここまでstripメソッド・lstripメソッド・rstripメソッドを紹介してきましたが、
ここでもう一度特徴をまとめます。

stripメソッド 	先頭と末尾の両端から文字を削除したコピーを返す
lstripメソッド 	先頭から文字を削除したコピーを返す
rstripメソッド 	末尾から文字を削除したコピーを返す

上記のような違いがあるので、使用する際は間違えないように注意しましょう。
"""


print("--- strip系メソッドの注意点 ---")


"""
最後にstrip系メソッドで単語を削除する場合、
注意しなければいけない点がいくつかありますので紹介します。

次のコードをご覧ください。
"""

text = 'dog.jpeg'
print(text.strip('.jpeg'))    # do


"""
このコードでは、「.jpeg」という拡張子だけを削除したいところが、
削除対象の文字の1つ「g」がファイル名の最後に来てしまっているのでそれも削除され、
結果として「do」出力されています。
そのため、次のように削除したい文字列を分断する必要があります。
"""

text = 'dog_x.jpeg'
print(text.strip('.jpeg'))    # dog_x

"""
見落としがちなミスなので注意しておきましょう。
指定した特定文字に一致する文字列ではなく、
指定した特定文字に含まれる文字が削除されるので注意しましょう。
"""

Str = 'aaabbbccc - HelloWorld - aaabbbccc'

print(Str.strip('abc'))    #  - HelloWorld -

print(Str.strip('bca'))    #  - HelloWorld -

"""
このように「’abc’」でも「’bca’」でも同じ結果となりますよ。
こちらも間違えやすいので注意しておきましょう。
また、引数に文字列を指定した場合は空白文字は削除されません。
"""

Str = ' \n aaabbbccc - HelloWorld - aaabbbccc \t'
# 末尾のスペースやタブを分かりやすくするために組み込み関数repr()を使用
print(repr(Str))    # ' \n aaabbbccc - HelloWorld - aaabbbccc \t'

print(repr(Str.strip('abc')))    # ' \n aaabbbccc - HelloWorld - aaabbbccc \t'

"""
そのため、空白文字も削除したい場合には明示的に指定するか、strip( )を繰り返し使用しましょう。
"""

print(repr(Str.strip('abc\n \t')))    # 明示的に指定
# '- HelloWorld -'


print(repr(Str.strip().strip('abc')))    # strip()を繰り返し使用
# ' - HelloWorld - '


print("--- まとめ ---")


"""
これまでstripメソッドについて詳しく説明してきましたがいかがでしたでしょうか。

今回説明した要点をまとめると以下のようになります。

    stripメソッドは先頭と末尾の空白文字や特定文字を削除する
    stripメソッドの構文は「文字列 . strip ( )」
    lstripメソッドは先頭の空白文字や特定文字を削除する
    lstripメソッドの構文は「文字列 . lstrip ( )」
    rstripメソッドは末尾の空白文字や特定文字を削除する
    rstripメソッドの構文は「文字列 . rstrip ( )」

stripメソッドはよく使用するメソッドです。
また、見落としがちなミスがいくつかありますので間違えないようにしっかり頭に入れておきましょう。
"""
