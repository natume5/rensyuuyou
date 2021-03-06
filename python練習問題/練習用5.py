#!/usr/bin/python
# -*- coding: UTF-8 -*-


# len()関数
"""
ここでは、リストオブジェクト cases の要素数を一週間分と決めて、
7件のデータだけを集計するようにプログラムを書いてきました。
しかし、これでは、3日分のデータを集計するときや、
10日分のデータを集計するときには、わざわざプログラムを書き直さなくてはいけなくなってしまいます。

それではあまりにも面倒ですので、リストオブジェクトの要素数を教えてくれる、
len() という関数がありますので、この関数を使って、リストオブジェクトの要素数がいくつあっても、
自動的にすべての要素を集計するようにしてみましょう。

"""
cases = [100, 125, 110, 135, 93, 95, 93]

index = 0    # インデックス値の初期値 0 を設定
len_cases = len(cases)
total = 0    # 合計感染者数の初期値 0 を設定

while index < len_cases:    # インデックス値 < 感染者リストの要素数の間、ループを繰り返す
	cases_of_day = cases[index]
	total = total + cases_of_day    # totalにcases[index]を加算
	index = index + 1

print("合計感染者数は:", total)


"""
あたらしく、リストの要素数を求める

len_cases = len(cases)

という代入文が追加されました。

関数 len() は、引数にリストオブジェクトを指定すると、その要素数を返してくれる関数です。
次の例は、要素数が4のリスト [1,2,3,4] を 指定してlen()を呼び出し、
戻り値として正しく 4 を受け取っています。

"""
values = [1, 2, 3, 4]    # 要素4のリスト
print(len(values))


# forによるループ
"""
for文の書き方
for 文は、次の形式で記述します。

for 変数名 in リストオブジェクト:
    処理1
    処理2
    ...

for 文は、リストオブジェクト から要素を一つずつ順番に取り出し、それぞれの要素ごとに、
for 文に続けて記述した処理を、一度ずつ実行します。変数名 には、
リストオブジェクトから取り出した要素を参照する変数名を指定します。

for 文の次の行から、それぞれの要素ごとに一度ずつ実行する処理を記述します。
この処理は、行の先頭にスペース４文字で インデント して記述します。

for 変数名 in リストオブジェクト:
    処理
^^^^
スペースを4文字入力
"""
# for文の例
values = [1, 2, 3, 4]

for value in values:
	print("valueは", value, "value * valueは", value*value)

"""
for 文は、変数 values のリストオブジェクトから要素を一つずつ取り出し、
それぞれの値ごとに次の行の print(...) を一度ずつ実行しています。

同じ処理を、while文を使ったリストのループ処理 で紹介した while 文を使ったループで書くと、次のようになります。
"""
values = [1, 2, 3, 4]
len_values = len(values)    # valuesの要素数を求める

index = 0    # インデックス値の初期値0を設定

while index < len_values:    # インデックス値 < len_valuesの間、ループを繰り返す
	value = values[index]
	print("valueは", value, "value * valueは", value*value)
	index = index + 1    # indexに1を加算

"""
while文を使うと、リストオブジェクトから値を取り出すインデックス値を決める処理などを、
自分で書かなければなりません。
しかし、for 文を使うと、そういった点はすべてPythonが裏でやってくれるので、処理が簡単になります。
"""


# 合計感染者数を for 文で求める
"""
while文を使ったリストのループ処理 で作成した、合計感染者数を計算するプログラムは次のようなプログラムでした。

cases = [100, 125, 110, 135, 93, 95, 93]

index = 0 # インデックス値の初期値 0 を設定
len_cases = len(cases)
total = 0 # 合計感染者数の初期値 0 を設定

while index < len_cases: # インデックス値 < len_cases の間、ループを繰り返す
    cases_of_day = cases[index]
    total = total + cases_of_day # totalに、cases[index]を加算
    index = index + 1 # index に 1 を加算

print("合計感染者数は:", total)

これも、for 文を使って書き直してみましょう。
"""
cases = [100, 125, 110, 135, 93, 95, 93]

total = 0    # 合計感染者数の初期値 0 を設定
for cases_of_day in cases:
	total = total + cases_of_day

print("合計感染者数は:", total)
"""
こちらも、for 文を使った方が簡潔で、処理を理解しやすくなっています。
for 文を使うパターンをマスターして、効率的にプログラムを書けるようにしてましょう。
"""


# 辞書
"""
リスト で紹介したリストオブジェクトは、順番に並んだ値をひとまとめの情報として
管理するためのオブジェクトでした。リストオブジェクトに登録された値を取り出すときには、
リストオブジェクト[インデックス] のように、参照する値の順番を指定します。
リストオブジェクトの例として、「東海道新幹線の停車駅」のリストを紹介しました。

stations = ["東京", "品川", "新横浜", "小田原", "熱海"]

このような単純なリストであれば、最初の駅は東京駅、2番目の駅は品川駅、 …… のように、
知りたい要素の順番だけを指定すれば必要な情報を取り出せます。

しかし、たとえば、英語の単語帳を作るときには、apple を指定すると りんご を返し、
orange を指定すると みかん を返すような仕組みが必要です。
あるいは、都道府県の県庁所在地を情報としてまとまるとき、埼玉県 を指定すると さいたま市 を返し、
北海道 を指定すれば 札幌市 と返す仕組みが必要です。
"""

# 辞書オブジェクト
"""
このような、あるデータに対応する関連データを登録できるような仕組みとして、
Pythonは 辞書オブジェクト を用意しています。辞書オブジェクトには、apple と りんご のような、
2つの値を組み合わせた情報を登録できます。apple と りんご の組み合わせを登録した辞書オブジェクトで、
apple を検索すると、本物の英和辞典とおなじように りんご が返ってきます。

このような機能から、辞書オブジェクトは、別名「連想配列」とも呼ばれます。
"""

# キーと値
"""
辞書オブジェクトを検索する時に指定するデータ(この例では apple) を、辞書の キー といいます。
また、キーに対応して、検索の結果となるデータ(この例では りんご)を、辞書の 値 といいます。

辞書の キー と 値 は非常に重要な用語ですので、しっかり覚えておいてください。
"""

# 辞書オブジェクトの作成
"""
辞書オブジェクトは、波括弧 { と } で作成します。

{キー1:値1, キー2:値2, ...}

{ と } の間には、登録するキーと値を キー:値 という形式で指定し、, で区切って記入します。

例として、こんな情報が入った英単語帳を作ってみましょう。
キー (英単語) 	値 (日本語)
apple 	りんご
orange 	みかん
peach 	もも

辞書を検索する キー として英単語を指定し、英単語に対応する日本語を 値 として、辞書を作成します。
"""

english_words = {"apple": "リンゴ", "orange": "みかん", "peach": "桃"}
print(english_words)


empty_dict = {}
print(empty_dict)


# 辞書の参照
english_words = {"apple": "リンゴ", "orange": "みかん", "peach": "桃"}
print(english_words["apple"])


# 辞書の操作
# 要素の追加と置き換え
"""
辞書オブジェクトに要素を追加するときは、次のように記述します。

辞書オブジェクト[キー] = 値

変数 の代入文とおなじ形式ですね。
"""
dict_obj = {}
dict_obj["dog"] = "犬"

print(dict_obj["dog"])


dict_obj = {"dog": "犬"}
print("修正前:", dict_obj["dog"])

dict_obj["dog"] = "わんこ"
print("修正後:", dict_obj["dog"])

# 要素の削除
"""
辞書オブジェクトに登録されている要素を削除するときには、del 文を使います。

del 辞書オブジェクト[キー]

辞書オブジェクトから、指定したキーの要素を削除します。次の例では、
辞書 dict_obj に登録されている、キーが"dog"の要素を削除します。

dict_obj = {"dog": "犬", "cat":"猫"}

del dict_obj["dog"]

登録されていないキーを削除すると、次のように KeyError というエラーが発生します。

dict_obj = {"dog": "犬", "cat":"猫"}

del dict_obj["penguin"]

---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-16-8cd30ef91c86> in <module>
      1 dict_obj = {"dog": "犬", "cat":"猫"}
      2 
----> 3 del dict_obj["penguin"]

KeyError: 'penguin'

"""
dict_obj = {"dog": "犬", "cat":"猫"}

del dict_obj["dog"]

# 辞書の要素数を求める
"""
辞書に登録されている要素の数は、リストオブジェクトと同じ ように、 len() 関数を使って求められます。
"""
dict_obj = {"dog": "犬", "cat":"猫"}
print(len(dict_obj))    # dict_objの要素数を求める

dict_obj["penguin"] = "ペンギン"    # dict_objに要素を追加する
print(len(dict_obj))    # dict_objの要素数を求める

del dict_obj["cat"]    # dict_objに要素を削除
print(len(dict_obj))     # dict_objの要素数を求める


# in 演算子
"""
辞書にキーが登録されているかどうか調べるときは、in 演算子を使います。

in 演算子は < や == のような 比較演算子 の一種で、

キー in 辞書オブジェクト

という式は、指定したキー値が辞書オブジェクトに登録されていれば True を、
登録されていなければ False を返します。

次の例では、キー値 "apple" は辞書 english_words に登録されていますので、
in 演算子は True を返します。
"""
english_words = {"apple": "リンゴ", "orange": "みかん", "peach": "桃"}
print("dog" in english_words)

# 練習問題
"""
in 演算子を使って、次のようなプログラムを書いてみましょう。

    input() 関数を使って、文字列を入力します。
    1. で入力した文字列が辞書オブジェクト english_words に登録されていたら、
    対応する日本語を出力します。
    登録されていなければ、"登録されていません" と出力します。
"""
english_words = {"apple": "リンゴ", "orange": "みかん", "peach": "桃"}

key = input("果物の英単語を入力して下さい。")

if key in english_words:
	# キーがenglish_wordsに登録されている
	print(english_words[key])
else:
	# キーがenglish_wordsに登録されていない
	print("登録されていません。")
	