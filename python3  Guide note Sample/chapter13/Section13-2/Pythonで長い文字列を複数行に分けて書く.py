"""Pythonでflake8などのPEP8に準拠したコードチェッカーを使っていると、
1行が80文字を超えたときにE501 line too longというエラーが出る。

URLなどの80文字を超えるような改行を含まない長い文字列を、
コード上で改行して複数行に分けて書く方法を紹介する。

    バックスラッシュ（\）を使う
    丸括弧を使う


バックスラッシュ（\）を使う

Pythonにおいて、バックスラッシュ（\）は継続文字であり、
行末におくとその後の改行が無視されて行が継続していると見なされる。

n = 1 + 2 \
    + 3

print(n)
# 6


また、複数の文字列リテラルを続けて書くと、
以下のように連結して一つの文字列になる。

s = 'aaa' 'bbb'

print(s)
# aaabbb


この2つを組み合わせると、

s = 'https://ja.wikipedia.org/wiki/'\
    '%E3%83%97%E3%83%AD%E3%82%B0%E3%83'\
    '%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E'

print(s)
# https://ja.wikipedia.org/wiki/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E

と、長い文字列をコード上で複数行に分けて書くことができる。

続けて書いて連結されるのは文字列リテラル（''や""で囲まれたもの）のみで、
文字列が格納された変数だとエラーになるので注意。


s_var = 'xxx'

# s = 'aaa' s_var 'bbb'
# SyntaxError: invalid syntax

変数同士や変数と文字列リテラルを連結するには+演算子を使う。


s = 'aaa' + s_var + 'bbb'

print(s)
# aaaxxxbbb


バックスラッシュ（\）で区切る場合も、変数を連結するには+演算子が必要。

s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'\
    + s_var\
    + 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'

print(s)
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaxxxbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb



丸括弧を使う

Pythonでは括弧（()、{}、[]）の中では自由に改行ができる。
このルールを利用して、長い文字列を括弧で囲んでしまってもよい。

なお、{}を使うと集合（set）、[]を使うとリストになってしまうので、
このような使い方の場合は丸括弧()を使う。

ここでも複数の文字列を続けて書くと連結して一つの文字列になることを利用すると、
以下のように書ける。


s = ('https://ja.wikipedia.org/wiki/'
     '%E3%83%97%E3%83%AD%E3%82%B0%E3%83'
     '%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E')

print(s)
# https://ja.wikipedia.org/wiki/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E



バックスラッシュを使った例と同様に、変数を含む場合は+演算子が必要。

s = ('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
     + s_var
     + 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')

print(s)
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaxxxbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb

"""
