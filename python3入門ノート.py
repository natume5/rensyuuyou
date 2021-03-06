Python 3.6.5 | Anaconda custom (64-bit) | (default, Mar 29 2018, 13:32:41) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more iinformation.
# !/usr/bin/env python
# -*- Coding: utf-8 -*-
1 + 2
3

240 * 3
720

4 + 6 / 2
7.0

(4 + 6) / 2
5.0

# 変数を使った計算

kosu = 12 * 5	 # 12*5の計算結果がkosuに入る
kosu
60

red_ball = 5
white_ball = 7	 # 2個の変数に値を入力する
all = red_ball + white_ball	 # 変数allにはredとwhiteの値を足した値が入る
all	 # 計算結果を出力
12

red_ball / all
0.4166666666666667

# 変数の値を変更する
red_ball = 3   3に変更
all
12　　合計の値は変化せず
all = red_ball + white_ball　　新し値で再計算する
all
10

# コードをファイルに書く

kosu = 12 * 5
print(kosu)

# 値と変数
# コードの書き方

a = 10		# 4行のステートメント
b = 20
ans = a + b
ans		# 30

# 上の3行を1行で書くと
a = 10; b = 20; ans = a + b
ans		# 30


# pythonファイルで書く場合の4行のステートメント
# 改行で区切られた4行のステートメント
a = 10
b = 20
ans = a + b
print(ans)				# statement_1.py

# ステートメントの区切りにセミコロンを使って書いたコード
a = 10; b = 20; ans = a + b
print(ans)				# statement_2.py

python statement_1.py 		# statement_1.pyとstatement_2.pyを実行する
30							# どちらのファイルも実行するとaとbを合わせた30を出力する

python statement_2.py
30

# ステートメントの改行
# (改行コードは\n。windows10では¥（円）ボタンで\が表示される。)
1 + 2 + 3 + 4 + 5\
 + 6 + 7 + 8 + 9\
 + 10
55

# pythonファイルに書くコードでステートメントを折り返す
ans = 1 + 2 + 3 + 4 + 5\
 + 6 + 7 + 8 + 9\
 + 10
print(ans)

r = 25	 # 半径
pi = 3.14	 # 円周率
len = 2 * pi * r	 # 円周の長さ
len
157.0

# 台形の面積を求める
a = 30	 # 上辺
b = 50	 # 下辺
h = 10	 # 高さ
# h=5
# 面積
area = (a + b) * h/2
print(area)

# C:\Program Files\Sublime Text 3\サンプル>python daikei.py	400.0

# ステートメントを途中で改行する
price = 1200 + 400 + 680\
 + 500
price
2780

# 複数行のコメント

a = 10
b = 20
"""
この範囲はコメントとして
実行時には無視されます。
"""
ans = a + b
print(ans)

# 大文字と小文字の区別

a = 10
A = 20
a
A

# 値と演算子
"""
ファイルに書くプログラムコードではprint()を使って値を出力して表示する。
名前に()がついているのは関数。()の中に入れる値は引数。
"""

print(100)
100
a = 200
print(a)
200

# ()の中に式を書けば、式の結果が出力される

print(1 + 2)
3
a = 100; b = 200
print(a + b)
300

# print()は複数の引数を指定できる。引数は,で区切る。

a = 100; b = 200; c = 300
print(a, b, c)
100 200 300

# print()は出力の後で改行をする。

a = 100
b = 200
c = 300
print(a)
print(b)
print(c)

# 区切り文字、改行を指定する
"""
print()では、複数の値の区切り文字や、行の最後の文字を指定することができる。この二つの
指定する書式は以下の通り、sep(separator)を省略すると半角空白、endを省略した場合は
改行(\n)になる。
書式　値の区切り文字、改行を指定する。
print(値１,２,…,sep="区切り文字",end="行末文字")
最初のprint()でsepとendの値を指定すると、値は読点(、)で区切られ、行末には
「/以上」と表示される。そして、そのまま改行せずに次のprintで出力されるabcの値が
表示される。
"""
a = 100
b = 200
c = 300
abc = a + b + c
print(a, b, c, sep="、", end="/以上")
print(abc)

"""
python print_sep_end.py
100、200、300/以上600
"""

# 数値
"""
整数と浮動小数点(小数点がある数値)に加えて、複素数を扱うことができる。
整数
実数のうち、小数点以下がない値が整数。0と負の値も含む（-3,0,5等）。
"""
a = -3
b = 0
c = 5
a + b + c
2

a = 0.08
b = 98.5
c = -3.5
print(a, b, c)    # 0.08 98.5 -3.5

a = .99
b = 10.
print(a, b)    # 0.99 10.0

1.23e+7
# 12300000.0
9.6e+7
# 0.00096
"""
複数表記
複数表記のeはExponetのことで10を底とした指数です。e+4ならば10の4乗の100000です。
したがって1.2e+4は1.2に100000を掛けた12000.0です。e-4ならば1/10000となり1.2e-4
は0.00012です。
"""

10.3 + 0.5    # 10.8
10 - 1.23    # 8.77
120 * 0.1    # 1.20
1.08 * 100    # 108.0
120 / 2    # 60.0
round(1.4)    # 1
round(2.5)    # 2
round(2.6)    # 3
round(23.576, 1)    # 23.6

"""
小数点以下の切り上げ、切り捨て
切り上げはceil()、切り捨てにはfloor()の関数がある。
この関数を使うにはmathモジュールをインポートする必要がある。
"""
"""
2進数8進数16進数
通常、整数は10進数で扱うが、2進数、8進数、16進数でも扱うことができる。
2進数は0bを付けて0と1の数字、8進数は0～8の数字、16進数は0xを付けて
0～9AA～Fで数値を表す。
pythonインタプリタで出力すると10進数に換算された値が出力されます。
"""
0b0101    # 2進数 5
0o011     # 8進数 9
0xFF      # 16進数 255
0b0101+0o011  # 7
bin(0b0101+0b0010)   # 0b111

"""
複素数(虚数)
pythonでは複素数も扱える。
複素数は「実部+虚部」で表現し、虚部にはj又はJの虚数単位（2乗すると-1になる値）をつける。
数学では虚数単位をiで表現するのが一般的だがpythonではjを使う。
例えば、(1+2j)のように書く。
次のように1j*1jの式を試すと結果は(-1+0j)となり、1jの2乗が-1となることを
確かめることができる。
"""
# 1jの2乗が-1になるかどうか確かめる
1j * 1j    # (-1 + 0j)

# 複素数も整数や浮動小数点と同じように計算できる
# 複素数同士の足し算
a = (1.5 + 3j)
b = (2 + 1j)
a + b    # (3.5+4j)

"""
次の例は複素数同士の掛け算です。(2j*5j)が-10いなるので、
次の計算は(20+50+j4-j10)のように展開されて、結果は(10++54j)になる。
"""
# 複素数同士の掛け算
(10 + 2j)*(2 + 5j)   # (10+54j)

"""
複素数の実部はreal、虚部はimagで個別に取り出すことができる。
次のように変数vに複素数が入っているならば、v.realが実部、v.imagが虚部の値になる。
"""
# 複素数の実部と虚部を取り出す
v = 3 + 2j
v.real    # 3.0
v.imag    # 2.0

# 複素数をconplex(re,im)で作る
v = complex(3, 2)
v     # (3+2j)
"""
complex("3+2j"),complex("3-2j")のように文字列から複素数を作ることも出来る。
+,-の前後に空白があるとエラーになる。

"""
"""
数値演算子
加減乗除などの数値計算には-や+などの記号を使います。これらの記号を演算子と言う。
そして数値の演算を行う演算子なので数値演算子と言う。数値演算子には、加減乗除のほかに
余りや商の数値を求める演算子がある。
"""
# 数値演算子には次のようなものがある。
"""
演算子    例     説明
+        a+b    足し算
-        a-b    引き算
*        a*b    掛け算
/        a/b    割り算
//       a//b   aをbで割った商の整数値（小数点以下を切り捨て）
%        a%b    aをbで割って、割りきれなかった余り（剰余）
**       a**n   aをn回掛けた値（べき乗、累乗）
"""
"""
350個のボールを12個ずつ箱に入れる時、何個出来て（//で表す）、
割り切れず何個余るか（%で表す）を計算する。
"""
all = 350    # 全部の個数
per = 12     # 1箱に12個入れる
all // per   # 完成する箱の数 29
all % per    # 余る個数 2

2**3   # 8

"""
文字列
文字の値は文字列、又はストリングと言います。
"～"又は'～'のようにダブルクォートかシングルクォートで囲って作る。
例
"こんにちは"、"箱根"、"python3","123","apple"   # 文字列
123   # 数値
apple   # 変数
"""
msg = "こんにちは"
where = "箱根"
language = "python3"
print(msg, where, langusge)    # こんにちは　箱根　python3
"""
シングルコートで囲っても文字列になる。
シングルコートは、ダブルクォートを含んだ文字列を作りたい時に全体を囲む場合に使用する。
"""
ai = 'いわゆる"人工知能"です。'
print(ai)
"""
逆にシングルコートを中に入れたい場合は全体をダブルクォートで囲みます。
ダブルクォートとシングルコートはエスケープシーケンスを使って埋め込むことができます。
エスケープシーケンス
文字列の中に改行やタブを埋め込みたい場合にバックスラッシュ\を使ったエスケープシーケンスを
利用する。
windowsでは\は￥と表示される。改行コードのエスケープシーケンスは\n。

"""
colors = "選んだ色は\n緑\n黄色"
print(colors)
# 選んだ色は
# 緑
# 黄色
"""
ダブルクォートで囲った文字列にエスケープシーケンスを使ってダブルクォートを埋め込んだ例。
\"がダブルクォートのエスケープシーケンスです。
"""
msg = "それは\"python 3\"です。"
print(msg)
"""
エスケープシーケンス    説明
\n               改行
\t               水平タブ
\r               キャリッジリターン
\"              ダブルクォート
\'              シングルクォート
\\              バックスラッシュ

複数行の文字列
クォートを３個続けて"""～"""或いは'''～'''のように囲むと複数行の文字列を作ることが
できる。
次の例では３個続けたダブルクォートで複数行の文字列を囲ってる。変数の値をそのまま出力
すると改行位置にエスケープシーケンスの\nが入っているのがわかる。
"""
poem = """ほととぎす
鳴きつる方をながむれば
ただ有明の月ぞ残れる"""    # python3にそのままコピーすれば「ほととぎす」と「ながむれば」の後に¥nがつく
poem
# これをprint()で出力すると画面でも改行して表示される
print(poem)
# ほととぎす
# 鳴きつる方をながむれば
# ただ有明の月ぞ残れる

neko = "吾輩は猫である。\n名前はまだない。"
print(neko)
# 吾輩は猫である。
# 名前はまだない。
"""
文字列を折り返して入力する
ステートメントの折り返しと同じように、長い文字列は\を入れた位置で折り返して
入力することができる。この折り返しは改行の\nとは違い、出力では無視される。
"""
# 文字列演算子
"""
数値演算子で足し算や掛け算ができるように文字列演算子を使って文字列の連結や、
繰返し文字を作ることができる。文字列には次のようなものがある。
演算子	列	説明
+		"a"+"b"	文字列"a"と"b"の連結。文字列"ab"になる。
*		"abc"*n	文字列"abc"をn回繰り返す。nが2ならば"abcabc"になる。
"""
# 文字列の連結
# +演算子を使うと2つの文字列を連結できる。
name = "鈴木" + "さん"

# 変数a,b,cに入っている文字列を連結してできた新しい文字列を変数dに入れている。
a = "Pen"
b = "Pine"
c = "Apple"
d = a + b + c
d
# 文字列の連結は+=を利用すると便利。
# 数値と文字列を連結連結する
"""
数値と文字列を連結したい場合は、数値と文字列型に変換する必要があります。
数値と文字列をそのまま連結するとタイプエラーになる。
price = 2500 + "円"		# エラー
エラーにならないようにするには、数値2500を文字列に変換する必要がある。
変換にはstr()を使う。
"""
price　=　str(2500)　+　"円"
price　# '2500円'

# これを利用すると単価と個数から値段の文字列を作れる
tanka = 80
kosu = 3
price = str(tanka+kosu) + "円"
price　# 240円

# 繰返し文字
"""
同じ文字が繰り返す文字列は、掛け算のように*演算子で作ることができます。
１文字の繰り返しだけでなく、複数文字の繰り返しを作ることができる。
"""
"a" * 3    # 'aaa'
"abc" * 3    # 'abcabcabc'
"""
次の例ではsymbolの文字を繰り返すことで、数値を簡易的な棒グラフとして表示している。
"""
symbol = "*"
print("東京", symbol * 12)
東京 ************    *を12個
print("金沢", symbol * 6)
金沢 ******    *を6個

"""
[]で文字列を繰り返す
文字列から文字を取り出すには[]を利用する。
[]には、取り出す文字の位置を指定する。文字の位置は１文字目を０と教え、
マイナスは後ろから教える。-1が最後の文字です。位置を0から教える教え方は、
色々な場面で使われるので慣れてください。位置を示す番号はインデックス番号と言う。

文字列を取り出す
文字列[文字位置]

次の例では文字列の３文字目と最後の文字を取りだしています。
2を指定すると先頭から３文字目、-1は最後から１文字目です。
文字を取り出しても元の文字列は変化しない。
"""
id = "ab1cd9x"
id[2]     # '1'		先頭から３文字目
id[-1]    # 'x'		先頭から１文字目

"""
但し文字列[位置]に文字を代入して変更することはできない。
これは文字列が状態を変更できないイミュータブル(immutable)と呼ばれる属性のオブジェクト
だからです。したがって、id[2]の文字を"w"に変更しようとするとエラーになる。
"""
id[2] = "w"   # 文字列を取り出すことはできても、書き換えることはできない　エラーになる
"""
部分文字列を取り出す（スライス）
[]は範囲を指定して部分文字列（文字列の一部）を抜き出すことができる。
この操作はスライスと呼ばれる。抜き出す範囲は開始位置と終了位置で指定するが、
開始位置～（終了位置-1）の範囲になるので注意。マルチバイト文字にも対応。

文字列のスライス
文字列[開始位置:終了位置]
"""
"""
開始位置と終了位置は省略が可能。文字列[:]は文字列全体を返す。
文字列[開始位置:]ならば開始位置から最後まで、文字列[:終了位置]ならば
最初から終了位置の手前まで抜き出す。
"""
# 部分文字列を取り出す
s = "The quick brown fox jumps."
s[:]    # 全部
'The quick brown fox jumps.'
s[:4]     # ５文字目から最後まで
# 'quick brown fox jumps.'
s[4:4+5]    # ５文字目から５文字
# 'quick'
s[:-7]      # 先頭から、後から数えて７文字目の手前まで
# 'The quick brown fox'
"""
スライスでは、文字列を超えた範囲を指定してもエラーにならない。
例で使用している文字列の長さはlen()で調べると44文字だが、
終了範囲を50で指定してもエラーにならない。最長の文字数を指定できる。
"""
s = "The quick brown fox jumps over the lazy dog."
len(s)    # 文字列の長さを調べる   44
s[:50]    # 文字列の長さを超えた範囲
# 'The quick brown fox jumps over the lazy dog.'
"""
ステップがある書式
これに加えてステップ(増分)があるオプションもあります。
ステップは１文字おき、２文字おきのように文字を取り出したい
場合に便利なオプションです。開始位置、終了位置で処理範囲を
指定できます。
飛び飛びで抜き出す
文字列[開始位置:終了位置:ステップ]
次の例ではステップを２にしているので、１文字目、３文字目、５文字目のように取り出す。
"""
# ４文字目から１文字飛ばしで取り出す
data = "abc0123456789"
data = data[3::2]    # '02468'
"""
ステップをマイナスで指定すると文字をうしろから取り出す。
最初の例は後ろから1つ飛ばしで文字を取り出す。
後から取り出すので、文字は元の文字列とは逆の並びになる。
ステップを-1にすれば逆順の文字列を作り出すことができる。
ただし、マイナスのステップは間違いの元なので注意が必要。
"""
# 文字列から一つ飛ばしで文字を取り出す
num = "0123456789"
num = [::-2]    # '02468'

# 文字列を逆順にする
s = "あいうえおかきくけこ"
s = [::-1]    # 'こけくきかおえういあ'

# 論理値(ブール値)
"""
論理値とは真/偽、表/裏、ON/OFF、YSS/NOなどのように、二択の値のうちどちらかを取る値です。
論理値は真理値、ブール値(bool)ともいいます。pythonの論理値では真をTrue,偽をFalesの
二つの値を使う。さらに論理式において数値の1はTrue、0はFalesと同じ値として扱われます。
"""
# 比較演算子
"""
aとbの値が正しいか、aがbより大きいか、bより小さいかといった比較を行う演算は比較演算子で行う。
比較した結果は論理値で示される。例えば変数aとbに入っている値が等しいかどうかは
a==bの式で比較できる。比較した結果、等しければTrue、等しくなければFalesになる。
=でなく==なので注意。
次の例では、aとbは等しいのでa==bはTrue、aとcは等しくないのでa==cはFalesになる。
"""
# 値が等しくないときTrue、等しいときFales
a = 3 ; b = 3 ; c = 5
print(a == b)    # True
print(a == c)    # Fales
"""
逆に比較した値が等しくない時にTrueになる演算子は!=です。a、b、cの値を!=で比較すると
==で比較した結果と逆になる。
"""
# 値が等しくない時True、等しいときFales
a = 3 ; b = 3 ; c = 5
print(a != b)    # Fales
print(a != c)    # True
"""
大きさの大小の比較は>、<で行う。a>bの式はbよりaが大きい時にTrueです。aとbが等しいか、
bの方が大きければFales。>=、<=は等しい場合もTrueに含める演算子です。
例えば、a>=50はaが50以上の時にTrue、50未満の時Fales。
"""
# aがbより大きい時True
a =60 ; b = 45
print(a > b)    # True

# aが50以上の時True
a = 50
print(a >= 50)    # True
"""
比較演算子をまとめると次の通り。<=、>=、!=の演算子は2個の記号で1つの演算子です。
<=を=<のように逆に書くとエラーです。記号の順番に注意。
演算子　　　例　　説明
==　　　　　a==b　aとbが等しい時True
!=　　　　　a!=b　aとbが等しくない時True
>　　　　　　a>b　aがbより大きいときTrue
>=　　　　　a>=b　aがb以上の時True
<　　　　　　a<b　aがbより小さい時True

is、is not
比較演算子には、同一オブジェクトかどうかを比較するis、is notの演算子がある。
"""
# １個の変数の値を比較する場合
"""
pythonでは、１個変数に対して次のような比較式を使うことができる。
次の例では、変数ageの値が13以上20未満の時にTrueになる。
"""
# ageが16なのでTrue
age = 16
13 <= age < 20    # True

# 論理演算子
"""
論理演算子には、and、or、notの３種類がある。
それぞれ、論理積、論理和、否定の演算をする。
論理演算子が使ってある式を論理式と言う。

演算子　　　例　　　　説明
and　　　　a and b　　論理積。aかつbの両方がTrueの時True。一方でもFalesならばFales。
or　　　　a or b　　　論理和。aまたbはのどちらか一方でもTrueならばTrue。両方ともFalesならばFales。
not　　　　not a　　　否定。aがTrueならばFalse。aがFalseならばTrue。
"""
# 論理積
True and True    #True
True and False   # False

# 論理和
True or True    # True
True or False   # True
False or False   # False

# 否定
not True   # Fales	Trueの反対
not False   # True	Falseの反対
"""
論理値のTrue/Falseは、比較演算子の結果としてかえってくるので、これを利用した論理演算を
行ってみる。比較演算子を活用することで、単純な論理式を複雑な論理式にすることができる。
次の例は変数aの値が50以上かつ100以下の時にTrueになる論理式をandを使って書いている。
aが80ならば(a>=50)と(a<=100)のどちらもTrueなので結果はTrueになる。
"""
# 変数aが50以上かつ100以下の時True、80なのでTrue
a = 80
(a >= 50) and (a <= 100)   # True
# 同じ式でaが110ならば、(a >= 50)はTrueでも(a <= 100)がFalesなので、論理値はFalse。

# 変数aが50以上かつ100以下の時True、110なのでFales
a = 110
(a >= 50) and (a <= 100)    # Fales
"""
次の例は、a、bのどちらかが"OK"ならばTrueになる論理和の式。
aが"NG"でもbが"OK"なので、式の結果がTrueになっている。
"""
# 変数a、bのどちらかが"OK"ならばTrue。変数bが"OK"なのでTrue
a = "NG" ; b = "OK"
(a == "OK") or (b == "OK")     # True

# 1と0
"""
数値論理でTrueとFalseが使われた時は、それぞれ1、0と同値として扱われる。
例、True+Trueは数値の2になる。
逆に論理値でとが使われた時は、それぞれTrue、Falseと同値として使われる。
"""
# True、Falesを数値式で使った時と0、1を論理式で使ったとき
True + False    # 1+0で計算、答え1
True + True     # 1+1で計算、答え2
1 and 1         # True and Trueと同じ、答え1
1 or 0          # True or Falseと同じ、答え1

# True False 0 1以外の値が論理式で使われた時
"""
True False 0 1以外の値が論理式で使われた時、値の大きさにかかわらずorでは左項、
andでは右項が式の値になる。
"""
# True False 0 1以外の値が論理式で使われた時
2 or 3      # 左項を採用、答え2
2 and 3     # 右項を採用、答え3

# ビット演算子
"""
ビット演算子では2進数の値をビットごとに演算する。
ビット演算子には次の種類がある。
ビット演算子を使えば、ビットの合成や、打消しができるので画像の合成などで活用されている。

論理積、論理和、排他的論理和
ビット演算子には次のようなものがある。
ビット演算の論理積(AND)、論理和(OR)、排他的論理和(XOR)では2つの値の桁同士を演算する。
反転(NOT)では各ビットの1、0を反転する。

演算子　　　例　　　　説明
&　　　　　a&b　　　　論理積(AND。両ビット共に1のとき)
|　　　　　a|b　　　　論理和(OR。どちらのビットが1ならば1)
^　　　　　a^b　　　　排他的論理和(XOR。比較したビットの値が異なるとき1)
~　　　　　a~　　　　　ビット反転(NOT。ビットの1と0を反転させる)

たとえば、0b0101、0b0011のAND、OR、XORのビット演算は次の図で示すように行われます。
ANDならば、各行を比較してどちらも1の桁が1になる。ORはどちらか一方でも1ならば1です。
ORは2つのビットを合成したことになる。XORは一致しない桁が1になる。
NOTはビットの反転なので、aが0b0101なら~aは0b1010になる。
"""

# 左シフト、右シフト
"""
左シフト、右シフトは10進数で考えると分かり易い。
例えば、12を120、1200のように桁を左にシフトすると10倍、100倍になり、逆にシフトすると
1/10、1/100になる。2進数も同様に桁を左にシフトすると2倍、4倍になり、右にシフトすると
1/2、1/4になる。シフトしてあふれた桁は消え、空いた桁には0が入る。

演算子　　　例　　　　説明
<<　　　　　a<<1　　　左シフト。ビットを左にずらす。値は2倍になる。
>>　　　　　a>>1　　　右シフト。ビットを右にずらす。値は1/2倍になる。

次の例では0b001011(10進数では11)を左へ1桁シフトしている。pythonインタプリタでは
演算結果が10進数で出力されるので、結果が22と表示されます。
"""
# 左に1桁シフトすると値が2倍になる
a = 0b001011
a     # 11
a << 1     # 22
"""
bin()を使うと数値を2進数の文字列で表示できる。
これを利用してビットがシフトされる様子を確認してみる。
"""
# 左にシフトされた値を2進数表記で確認
a = 0b001011
bin(a << 1)    # '0b10110'

# ビットマスク
"""
必要な部分を1にした値とANDすることで、数値から必要なビットを抜き出すことができる。
これをビットマスクと言う。下３桁を取り出している。
"""
# ビットマスクで下3桁を取り出す
a = 0b100110
bin(a &0b111)      # '0b110'
"""
途中のビットを抜き出したい時は値をシフトしてビットマスクする。
次の例は右へシフトして、途中の2ビットを取り出している。
つまり、0b10101を0b1010にしておいて0b11とビットマスク演算をする。
こうすることで元の数値の3-2桁である10を取り出せる。
"""
# 途中の2ビットを取り出す
a = 0b10101
bin((a>>1) & 0b11)    # '0b10'   (a>>1)で先に右へ1桁シフトした

# 型を変換する
"""
pythonの場合、通常の計算では値の型についてさほど意識する必要はありませんが、
型について最低限のことは知っておくべき。

型を調べる
値の型はtype()で調べることができる。例えば、数値の1の型を調べると<class 'int'>
のように出力される。
これは、数値の1がint型(整数型)であることを示している。intはintegerの略。
"""
# 値の型を調べる
type(1)    # <class 'int'>		整数はint型
"""
浮動小数点の方はfloat、文字列の型はstrと表示される。strはstringの略。
"""
# float型str型
n = 12.3 ; name = "山田"
type(n)    # <class 'float'>		浮動小数点はfloat型
type(name)    # <class 'str'>		文字列はstr

# 数値を文字列に型変換する
"""
計算で求めた数値を"長さ12.3cm"のように文字列と連結したい場合、
文字列同士ならば+演算子で連結できますが、数値と文字列を連結しようとすると
エラーになります。
"""
# 文字列と数値を+演算子で連結しようとするとエラーになる
len = 10 * 1.23
ans = "長さ" + len + "cm"	# 文字列と数値を連結するとエラーになる
# この場合、次のようにstr()を使って数値を文字列に型変換することで問題を解決できる
# 数値をstr()で文字列にして連結する
ans = "長さ" + str(len) + "cm"	# 数値を文字列に変換して連結すればエラーにならない
ans		# '長さ12.3cm'
"""
str()は数値を文字列に型変換するだけでなく、他の型の値も文字列に変換できます。
次の例では論理値のTrueを文字列に変換していく。
"""

# str()で論理値を文字列に型変換する
ans = "5<10は" + str(5<10) + "です"
ans    #'5<10はTrueです'

format()を使って文字列に埋め込むことも出来る

# 色々な型変換
"""
str()で値を型変換できるように、整数値への型変換はint()、
浮動小数点への型変換はfloat()、論理値への型変換はbool()で行える。
int()、float()を使えば、文字列を数値計算で使えるようになる。
"""
int("250") * 3    # 整数に型変換		750
float("1.5") + 0.2    # 浮動小数点に型変換			1.7
# int()で浮動小数点を整数化すると小数点以下は切り捨てられる。
# 浮動小数点を整数にする
int(12.9)    # 12

# 2進数、8進数、16進数を文字列に換算する
"""
bin()、oct()、hex()を使うと、数値を2進数、8進数、16進数を文字列に変換できる。
"""
# 数値を2進数、8進数、16進数で表記した文字列に変換する
bin(10)    # '0b1010'
oct(10)    # '0o12'
hex(10)    # '0xa'

# 変数
"""
既に変数を使って簡単な計算を行ってきたが、この節では改めて変数について説明する。
変数名のつけ方や変数に値を代入する方法を整理する。

変数とは
変数は値を一時的に保管する箱のようなものと説明されることがありますが、
変数の大きな役割は変数を使って式を掛けるという点にあります。
例えば、「1200 * 3」では、この式が何を計算しているかわかりませんが、
「tanka * kosu」と書くことで式の意味を読み取ることができるようになる。
また、変数を使えば定価や個数の値が決まっていなくても式が書ける。
さらに、個数が10個以上ならば割引するといった条件分岐なども組み込むことも
できるようになる。
つまり、変数を使うことでアルゴリズムを書けるようになる。
これが変数を使う、最も大きな理由と言える。
pythonには定数がない。慣習として大文字で書いた変数を定数として使う。
"""
# 変数を作る
"""
pythonの変数には宣言文がなく手軽に利用できる。
値を代入することで変数が作られ、使い始めることができる。
「代入」とは変数に値を設定することです。変数に値を代入するために使う=を代入演算子と言う。
"""
# 変数に値を代入して使い始める
width = 20.0
hight = 10.0
area = width * hight / 2
print(area)    # 100.0

# 変数名のつけ方
"""
変数名は半角英数と_(アンダースコア)で付ける。ひらがなや漢字などのマルチバイト文字を
使うことも出来ますが、一般的には使わない。また、慣例として変数名は小文字でつける。
変数名はa、bといった汎用的なものではなく、何を示す値かがわかる名前をつけるようにする。
そうすることでコードが読みやすくなり、コードの確認や修正を効率よく行えるようになる。
"""
# 変数名の例
id、name、tax、width、speed、lines、img1、img2
"""
わかりやすい変数名にするために、複数の単語や数字を組み合わせることが多くあります。
その場合、myNameのように単語の区切りを大文字にするつけ方があるが、
pythonではmy_nameのように_で連結するつけ方が多く使われる。
"""
# 単語を連結して作る変数名の例
color_green、ball_weight、id_list、doll_yen_rate

# キャメルケースとスネークケース
"""
myNameはラクダのこぶのように見えるのでキャメルケース、my_nameは蛇のように見えるので
スネークケースと言う。pythonでは変数名にスネークケースを使う。
"""
# 使えない変数名
"""
変数名の1文字目には数字が使えない。また、+、-、/、%、(、{、#などの演算子や記号は使えない。
使えない変数名の例
7eleven、4_peeks、you+i、green-card、red/box、[a]、pin#1、pen&apple
pythonの予約語を変数名に使うことはできない。予約語には次のようなものがある。
"""
# pythonの予約語
and、as、assert、break、class、continue、def、elseif、else、except、False、
finally、for、from、grobal、if、import、in、lamda、None、nonlocal、not、or、pass
、raise、return、True、try、while、with、yield

# 大文字と小文字
"""
大文字と小文字は区別される。例えば、point_aとpoint_Aという変数があった時、
2つは似た名前の別の変数である。
"""
# 変数の型
"""
変数の値には型がありますが、変数には型がない。例えば、文字列が入っている変数に数値を
代入しても値が置き換わるだけでエラーにはならない。
"""
# 文字列が入っていた変数に数値を代入する
price = "未定"
price = 120 * 2
price    # 240

# 複合代入演算子
"""
まず、次のコードを見てください。これはどのような計算を行っているでしょうか？
2行目の式では左右の両辺にageがあります。
"""
# 変数自身を計算に使う式
age = 19
age = age + 1
age    # 20
"""
2行目の式では、=よりも先に+の演算子が実行されるため、まず、age+1が計算されます。
この時点ではageの値は19なので結果は20です。そしてこの値がageに代入される。
つまり、ageの値が20になる。
このように、変数の値を更新するために変数自身に演算を行うことはよくある。
そこで変数への演算と代入の両方を行う複合代入演算子(代入演算子と呼ぶこともある)
というものが用意されている。
先のコードは、複合代入演算子の+-を使って、次のように書き替えることができる。2行目に注意。
"""
# 複合代入演算子+-を利用した場合
age = 19
age += 1
age    # 20

# 次の例では*=を使って、pointを2倍にしている
# pointを2倍にする
point = 10
point *= 2
point    # 20

# 複合代入演算子
"""
複合代入演算子には次のようなものがある。
演算子　　　例　　　　説明
+=　　　　　a += b　　a = a + bと同じ。aにbを足した値を代入。
-=　　　　　a -= b　　a = a - bと同じ。aにbを引いた値を代入。
*=　　　　　a *= b　　a = a * bと同じ。aにbを掛けた値を代入。　
/=　　　　　a /= b　　a = a / bと同じ。aにbを割った値を代入。
//=　　　　a // = b　a = a // bと同じ。aをbで割った整数値を代入。
%=　　　　　a %= b　　a = a % bと同じ。aをbで割った余りを代入。
**=　　　　a ** = b　a = a ** bと同じ。aをb回かけ合わせた値を代入。
"""

# +-を使って文字列を連結する
"""
+=を使うと文字列を効率よく連結できる。次の例の変数text最初は""つまり空ですが、
+=で"吾輩は"、whoの値、"である。"を連結した文字列になっています。
このコードの注意点としては、最初に変数textに""を代入するところである。
これによって変数textが作られて初期化される。
"""
# 文字列を+-で連結する
who = "猫"
text = ""
text += "吾輩は"
text += who
text += "である"
text    # '吾輩は猫である'

# 変数に値を代入するとは
"""
ここで改めて変数に値を代入すると値がどのように受け渡されるかを見ておく。
次の式では変数wallet1に100を代入している。wallet1の中身を確かめると、
確かに100が入っている。これは、wallet1に100を入れるという感覚と一致している。
"""
# 変数walletに100を入れる
wallet1 = 100
wallet1    # 100
"""
次に変数wallet2にwallet1を代入する。wallet2の中身を確認すると100が入っている。
"""
# 変数wallet2にwallet1を代入する
wallet2 = wallet1
wallet2    # 100
"""
さて、この時wallet1の値はどうなったでしょうか？wallet1の中身をwallet2に移したので
wallet1は空っぽになっているのではないでしょうか？実際に調べてみよう。
"""
# wallet1の中身を確認
wallet1    # 100
"""
するとwallet1の値をwallet2に入れたにもかかわらず、wallet1には100が入ったままです。
つまり代入は値を移しているわけではないことがわかる。勘違いに注意。

MEMO
リテラルとリファレンス(参照)
リテラルとは、10、20、"abc"等、コードに値を直接書いたもの。
これに対しリファレンスは値が記録されているアドレスへの参照。
値を変数に代入すると変数には値への参照が入る。
リストや辞書を使う際には気を付けなければいけないポイント。
"""

# 組み込み関数
"""
pythonをインストールすると標準でインストールされるライブラリのうち、
いつでもどこからでも呼び出せる関数が組み込み関数。
この節では組み込み関数にはどのようなものがあるかを紹介する。
"""
# 関数とは
"""
一般的によく利用する処理のコードは、呼び出すだけで使えるようにコードに
名前を付けて定義してある。例えば、
max()と言う関数は複数の数値の中から一番大きな値を返す関数です。
max()が内部でどのようにして最大値を選んでいるかは知らなくてもmax()は利用できる。
"""
# 一番大きな値を返すmax()関数
max(3,5,2)    # 5	3、5、2では5が最大値
"""
関数は関数名に()を付けて呼び出す。()の中には関数で処理したい値を入れる。
これを「引数（ひきすう）」と呼ぶ。複数の引数がある場合は、引数をカンマで区切って与える。
どのような引数を与えるかは関数によって違い、引数を取らない関数もある。
関数から返ってくる値を「戻り値」「返り値」と呼ぶ。
"""
# 組み込み関数とは
"""
組み込み関数とはいつでもどこからでも呼び出せる関数のことである。
これまでにもいくつかの組み込み関数をすでに使ってきている。
値を出力するprint()、型を調べるtype()、型変換で使うstr()、int()、float()、bool()、
数値を2進数、8進数、16進数の文字に変換するbin()、oct()、hex()、
小数点以下を四捨五入するround()などはすべて組み込み関数である。
"""
# 桁を指定して数値を丸める
round(3.65, 1)    # 3,6

# 文字列に使う関数
"""
関数　　　　　説明
chr(整数)　　整数が示すUnicodeを文字列で返す(iは0～1,114,111)
ord(1文字)　　文字列に対応するUnicodeを調べる
len(文字列)　文字列の文字数を求める。2バイト文字も1文字で数える
str(値)　　　値を文字列に変換する

chr()とord()は逆の変換をする。ord()で文字をUnicodeに変換し、
chr()で文字に戻してみる。
"""
# Unicodeに対応する文字を調べる
ord("a")     # 97	Unicode
chr(97)    # 'a'
ord("海")    # 28023		Unicode
chr(28023)    # '海'
"""
文字数はlen()で数えることが出来る。半角英数だけでなく、
かな漢字などの2バイト文字も1文字として数える。
なお、len()はリストや辞書などの要素の数を数えることも出来る。
"""
len('Python')    # 6		文字数
len("パイソン")     # 4
"""
str()は値を文字列に変換する。求めた数値を文字列と連結して出力したい時などに利用する。
"""
kosu = len("Python")
ans = "文字数は" + str(kosu) + "個"		数値を文字列に変換すれば、文字列同士は+で連結できる
print(ans)    # 文字数は6個
"""
少し難しい話になるが、文字列は文字列型(strクラス)のオブジェクトであることから、
strクラスの様々な文字列メゾットを使って操作することも出来る。
"""

# 入出力に使う関数
"""
入出力に使う関数もある。imput()はキィーボードからの入力を受け取る。
open()はファイルの読み書きに使う関数です。

関数　　　　　　　説明
input(文字列)　　キィーボードからの入力を受け取る。文字列はプロンプトとして表示される。
open()　　　　　　テキストファイルを開く
print(値,sep=文字列,end=文字列)　値を出力する

input()を実行するとキーボードからの入力待ちになり、入力した値を受け取る。
pythonインタプリタで次のようにinput()を書いて実行すると、次の行には引数の
「好きな言葉を入力して下さい。:」がプロンプトとして表示され、キーボードからの入力待ちになる。
"""
# キーボードからの入力待ちになる
value = input("好きな言葉を入力して下さい。:")
# 好きな言葉を入力して下さい。:		キーボードからの入力待ちになる
"""
キーボードから文を入力すると変数valueに入る。出力して確認する。
"""

# キーボードから入力し、入力された値を確かめる
"""
value = input("好きな言葉を入力して下さい。:")
好きな言葉を入力して下さい。:こんにちは	表示キーボードから「こんにちは」と入力します
print(value)    #こんにちは 		キーボードから入力された文字列が入る
"""

# 組み込み定数、酌み込み型、組み込み例外
"""
組み込み関数と同じように、組み込み定数、組み込み型、組み込み例外がある。
数値や文字列などの標準で使える値の型は組み込み型である。
True、Falseは組み込み定数の値である。
"""

# モジュールを読み込む
"""
標準でインストールされていても、組み込み関数以外の関数は利用を開始する前に
モジュールを読み込む必要がある。
この節ではモジュールの読み込みと関数の利用方法をmathモジュールとrandomモジュールを
使って説明する。
"""
# モジュールを読み込む
"""
標準ライブラリには数多くの関数があるが、それらの関数は数学関数のmathモジュール、
疑似乱数を生成するrandomモジュール、日付と時間のdatetimeモジュールというように、
目的に応じてモジュール別になっている。
これらを使うには利用を開始する前にモジュールを読み込む必要がある。
また、pythonファイルに分けてコードを保存している時、他のpythonファイルでていぎしている関数や
変数などもモジュールとして読みこんで使うことが出来る。
"""

# モジュールを読み込む書式
"""
モジュールの読み込みにはimportを使う。カンマを区切ることで複数のモジュールを
読み込むことが出来る。as別名のオプションを追加すれば、読みこんだモジュールに
別名をつけて利用することが出来る。
これはモジュール名が長かったり、モジュール名がバッティングしていたりする場合に問題を解決する
有効な手段である。
"""
# モジュール全体を読み込む
import モジュール名,モジュール名,・・・
import モジュール名 as 別名
# 読みこんだ関数を使うには、モジュール名と関数を指定して呼び出す。

# 読みこんだモジュールの関数を使う
モジュール名.関数()

# mathモジュールを読み込んで
"""
それでは実際にmathモジュールを読み込んで関数を使ってみる。
mathモジュールには、切り上げ、切り捨て、ラジアンの換算、三角関数と言った関数が入っている。
まず、import mathを実行してmathモジュールを読み込む。次にmathモジュールにあるceil()を
実行する。ceil()は小数点以下を切り上げる関数です。このとき、ceil()がmathモジュールにある
ことを示すためにmath.ceil(15.2)のように呼び出す。
続いてfloor()を実行する。floor()は切り捨て関数です。すでにmathモジュールは読み込んでいる
ので再読み込みの必要はないが、ceil()の場合と同じようにfloor()がmathモジュールの関数
であることを示さなければならない。
"""
# mathモジュールを読み込んでceil()とfloor()を使う
import math     mathモジュールを読み込む
math.ceil(15.2)     # 16 切り上げ		mathでモジュールを指定して関数を呼び出す。
math.floor(15.2)    # 15 切り捨て
"""
三角関数のsin()、cos()、tan()等も同様に使う。三角関数の引数の角度は(radian)
という単位です。ラジアンと度(degree)は「360度 = 2πラジアン」という関係だが、
degrees(ラジアン)、radians(度)という換算の換算の関数がある。
πはmath.piで定数として定義してある。
"""

# 定数piとラジアンを度に換算するdegrees()を使う
import math
math.pi    # 3.141592653589793	定数
math.degrees(math.pi/4)    # 45.0	ラジアンを度に換算
"""
次のコードではtan()を使って距離(20m)と(32m)から木の高さを計算している。
結果は小数点以下第2位で切り捨てる。floor()は小数点以下を切り捨てるので、
100倍して切り捨てた後に100で割って元の桁に戻す。
"""

# tan()を使って距離と角度から木の高さを求める
import math
kyori = 20
kakudo = math.radians(32)    # ラジアンに換算する
takasa = kyori * math.tan(kakudo)    # 高さを計算する
takasa = math.floor(takasa * 100) /100    # 小数点以下第2位で切り捨て
print(str(takasa) + "m")    # 12.6m	計算結果を文字列に変換して出力

# mathモジュールの関数と定数
"""
mathモジュールには多くの関数及び定数がある。代表的なものを次に列挙する。
関数　　　　　　　説明
ceil(x)　　　　　小数点以下を切り上げて整数にする
copysign(x,y)　　xの大きさで、yと同じ政府の値を作る
fabs(x)　　　　　xの絶対値
factorial(x)　　　xの階乗
floor(x)　　　　　小数点以下を切り捨てて整数にする
fmod(x,y)　　　　xをyで割った余り。xとyが浮動小数点の場合に用いる
fsum(iterable)　　iterable(タプル、リスト、辞書、集合など)の値の浮動小数の和
gcd(a,b)　　　　　整数aとbの最大公約数
exp(x)　　　　　　指数関数。eのx乗
log(x,base)　　　baseを底とした対数。baseを省略するとeを底とする自然対数
log2(x)　　　　　　2を底とした対数
log10(x)　　　　　10を底とした対数(常用対数)
pow(x,y)　　　　　xのy乗
sqrt(x)　　　　　　xの平方根
e　　　　　　　　　自然対数
inf　　　　　　　　浮動小数点の無限大
nan　　　　　　　　浮動小数点の非数

次は三角関数に関する関数及び定数。θはラジアン単位の角度。
関数　　　　　　　説明
acos(x)　　　　　逆余弦。cos(θ)がxになるθを返す
asin(x)　　　　　逆正弦。sin(θ)がxになるθを返す
atan(x)　　　　　逆正弦。tan(θ)がxになるθを返す
atan2(x,y)　　　　原点から点(x,y)へのベクトルの角度
cos(θ)　　　　　　θの余弦
sin(θ)　　　　　　θの正弦
tan(θ)　　　　　　θの正接
degrees(θ)　　　　ラジアンを度に換算する
radians(x)　　　　度をラジアンに換算する
pi　　　　　　　　円周率
"""

# 関数を指定して読み込む
"""
モジュール全体ではなく特定の関数を指定して読み込むことも出来る。
その場合は次の書式を使う。as別名のオプションを追加することで、
読みこんだ関数に別名をつけて利用することも出来る。関数名が長かったり、
関数名がバッティングする場合に問題を解決したり、全体のコードを変更せずに
利用する関数を入れ替えたい場合に有効な手段です。
関数名には()を付けずに指定する。
"""
# モジュール内の特定の関数を読み込む
"""
fom　モジュール名　import　関数名
fom　モジュール名　import　関数名　as　別名

読みこんだ関数を使うには、モジュール全体を読み込んだ時と違って、
モジュールを指定せずに関数名だけで利用できる。
"""
# 読みこんだ関数を使う
# 関数()
# randomモジュールの関数を読み込む
"""
randomモジュールには乱数の作成や値をシャッフルするといった関数がある。
複数の値からランダムに値を選ぶ、値をシャッフルする関数についてはリストと合わせて説明する。
使う次のコードでは、その中から整数の乱数を作成するrandint()だけを読み込んで使う。
radint()関数を指定する際に括弧を付けずにrandintと指定している点に注意すること。
randt(1,6)では、サイコロの目を出すように1～6の整数の中から1つの値を選び出す。
randint(1,6)を実行する度に値が変わるのがかがわかる。
"""
# randomモジュールからrandnt()を読み込んで使う
from random impport randint
randint(1, 6)      # 6　1～6の乱数　モジュール名を付けなくてもrandint()だけで実行できる
randint(1, 6)    # 5
randint(1, 6)    # 1
"""
0.0～1.0の浮動小数点の乱数が欲しい場合はrandom()を使う。引数は不要。
"""

# randomモジュールからrandom()を読み込んで使う
from random import random
random()    # 0.07962074139508624
"""
読み込む関数に別名を付けて利用する例も示しましょう。
次のコードではrandintにdiceの名前を付けています。
randint(1,6)をdice(1,6)のように実行できる。
"""

#randint()をdiceの名前で読み込む
from random import randint as dice
dice(1,6)    3

# オブジェクトのメゾット
"""
pythonの値は全てオブジェクトです。オブジェクトには、実行できる関数（メゾット）が定義されている。
オブジェクト指向プログラミングについては「Chapter12クラス定義」で詳しく解説するが、
この節でオブジェクトと型（クラス）の概念に触れておくと、今後のプログラミングの理解度が
大きく違ってくる。
"""

# オブジェクトのメゾット
"""
オブジェクトとはデータ（属性）とメゾットを持ったものである。データは変数で保持し、
メゾットは関数で定義する。これまでに説明してきた関数は、誰に命令することもなく
len("abc")のように関数を呼び出せば実行されました。
しかし、これから説明するオブジェクトのメゾットは、対象のオブジェクトを指定して
メゾットの実行を命令する。

これは人や機器に命令することと同じですが、何かを命令したとして、
それが理解され執行できるのか？という問題がある。洗濯機に食品の温めを命令しても
実行できないように、オブジェクトにメゾットを命令しても実行できるとは限らない。
次のオブジェクトがcalk()を知らなければエラーになる。
"""

# インスタンスメゾットとクラスメゾット
"""
クラスから作ったオブジェクト（インスタンス）に対して実行するメゾットはインスタンスメゾット、
クラスに対して実行するメゾットはクラスメゾットという。
"""

# オブジェクトの型と実行できるメゾット
"""
オブジェクトがメゾットを命令された時、そのメゾットをどう処理すればよいかはオブジェクト自身が
知っている必要がある。逆に言えば、オブジェクトが知っている幾つかのメゾットの中から、
実行したいメゾットを命令する。次のオブジェクトにa()、b()、c()のメゾットが定義してあるならば、
b()を命令すれば実行できる。
車や機器の形式を見れば機能がわかるように、オブジェクトの型を見れば実行できるメゾットを
知ることが出来る。例えば、文字列であればstr型（テキストシーケンス型）で定義されている
メゾットを実行できる。
"""

# オブジェクトのメゾットを実行する
"""
オブジェクトのメゾットを実行するには、次のようにドットシンタックスを使う。

オブジェクトのメゾットを実行する
オブジェクト.メゾット()

では、str型のオブジェクトである文字列を例にとってオブジェクトのメゾットを実行してみる。
まず、変数sに文字列の"Hello　Python"を代入しておく。メゾットを実行する前に
変数がstr型であることを確認しておく。変数の型（変数に入っている値の型）は
type()で調べる。結果は<class 'str'>でした。文字列を代入した変数がstrクラスの
オブジェクトすなわちstr型だと分かる。
"""

# オブジェクトの型を調べる
s = "Hello Python"
type(s)    # <class 'str'>	str型（文字列型）
"""
それでは、変数sに対してupper()を実行してみる。upper()はstr型のオブジェクトに対して
利用できるメゾットの一つで、半角英字を大文字に変換するメゾットです。
変数sに文字列を代入してあるので、s.upper()のようにメゾットを実行する。
すると変数の値である"Hello Python"が大文字で変換されて出力される。
"""

# str型なのでupper()が使える
s = "Hello Python"
s.upper()    # 'HELLO PYTHON'
"""
もちろん、文字列を変数に入れずに直接メゾットを実行することも出来る。結果は同じ
"""
"Hello Python".upper()    # 'HELLO PYTHON'

# 文字列のメゾット
"""
この節では文字列オブジェクトが実行できる色々なメゾットを紹介する。
全てを覚える必要はないが、文字列の処理は様々な場面で必要となるので、
どのようなことが出来るのかをざっと知っておくこと。
"""
# 大文字小文字の変換
"""
半角英字は大文字小文字の相互変換ができる。upper()は全てを大文字に変換し、
lower()は全てを小文字に変換する。swapcase()は大文字と小文字を入れ替える。
"""
# 大文字と小文字を入れ替える
s = "Apple iPhoneとGoogle Android"
s.upper()    # 'APPLE IPHONEとGOOGLE ANDROID'
s.lower()    # 'apple iphoneとgoogle android'
s.swapcase()    # 'aPPLE IpHONEとgOOGLE aNDROID'
"""
capitalize()は文字列の1文字目だけを大文字にし以降を全て小文字にする。
title()は各単語の1文字目を大文字にし、単語の2文字目移行を小文字にする。
ただし、"it's"のようにアポストロフィがある文はうまく処理できない。
そのようなケースにも対応するには正規表現を使用する必要がある。
"""
# 1文字目を大文字にする
s= "may the force be with you!"
s.capitalize()     # 'May the force be with you!'
s.title()     # 'May The Force Be With You!'

# 文字列を検索する
"""
count()は文字列を検索して、引数で指定した文字列が何個含まれているかを返す。
マルチバイト文字も正しくカウントできる。
"""
# 文字列が含まれる個数を返す
"""
count(文字列)
"""
# 文字列に含まれる"p"、"どど"の文字を数える
s = "appple pie"
s.count("p")    # 3		"p"の個数を数える
"どっどどどどどうど".count("どど")    # 2	"どど"が連続しているが、同じ文字は数えないので結果は2個

"""
次のように検索結果を指定することも出来る。結果範囲は、開始位置から終了位置の手前までで、
終了位置は範囲に入らないので注意。終了位置を省略すると最後までが検索範囲となる。
"""
# 検索範囲を指定して文字を数える
"""
count(文字列,開始位置)
count(文字列,開始位置,終了位置)
"""
# 先頭から4文字目までに含まれる"p"の個数
s = "apple pie"
s.count("p", 0, 4)   # 2
"""




































