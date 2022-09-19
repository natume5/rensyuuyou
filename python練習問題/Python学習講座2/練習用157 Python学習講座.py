#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- Python学習講座 ---")
print("--- Python入門 ---")
print("--- for文 ---")


print("--- for文の基本 ---")


"""
for文とは冒頭で述べたとおり繰り返し処理を行うための文です。
Pythonのfor文は以下のように記述します。

for文
for ループ内変数 in イテラブルな変数:
    ループ内処理

イテラブルというのはリストや辞書といった複数の要素からなり、
反復処理が可能な性質をもつことを指し、以下のような型がそれに該当します。

リスト
タプル
文字列
set
range
辞書
[参考] range型
いくつか例を見ていきましょう。


リストのfor文
リストの要素の先頭から順番に表示する場合、以下のように記述します。
"""

datas = ['a', 'b', 'c']

for v in datas:
    print(v)    
# a
# b
# c


"""
rangeのfor文
rangeで初期値、限界、増分を指定すると、
C言語やJavaのループカウンタを利用したループ処理を行うことができます。
"""

for v in range(1, 5, 2):
    print(v)    # 1から2飛ばしで5未満まで出力されます。この場合、1、3が出力されます。
# 1
# 3


"""
辞書のfor文
辞書もfor文でループ処理可能です。リストなどの同様の書き方も場合、
キーのみのループになりますが、辞書のメソッドを使用することでキー、
値のループも可能となります。今回は紹介のみにとどめ、次回もう少し細かく説明します。

キーのループ
前述のとおり、通常のfor文の場合はキーをループ処理することができます。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}

for key in d:
    print(key, d[key])
# key1 110
# key2 270
# key3 350

"""
valueのループ
値でループしたい場合はvaluesメソッドを利用します。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}

for value in d.values():
    print(value)
# 110
# 270
# 350

"""
keyとvalueのループ
キー、値の両方をループで取得したい場合は、items()メソッドを利用します。
"""

d = {'key1': 110, 'key2': 270, 'key3': 350}

for key, value in d.items():
    print(key, value)
# key1 110
# key2 270
# key3 350


"""
ループインデックスを取得する場合
何番目の要素だけは処理をしない、
等の処理を入れたい場合はループインデックスを利用しますが、
これはenumerate関数で取得することができます。

リストの場合
"""

l = ['a', 'b', 'c']

for i, value in enumerate(l):
    print(i, value)    # ループインデックスとリストの値が出力
# 0 a
# 1 b
# 2 c

for (key, value) in enumerate(l):
    print(key, value) 
# 0 a
# 1 b
# 2 c

"""
辞書の場合
"""

dic = {'key1': 110, 'key2': 270, 'key3': 350}

for i, value in enumerate(dic):
    print(i, value)    # ループインデックスと値が出力
# 0 key1
# 1 key2
# 2 key3

for i, (key, value) in enumerate(dic.items()):
    print(i, key, value)    # ループインデックスとkeyと値が出力
# 0 key1 110
# 1 key2 270
# 2 key3 350


print("--- break ---")


"""
breakを使用するとループの途中で抜けることができます。
サンプルで確認してみましょう。以下のコードでは、
リストの各値をprintで出力していますが、
1より大きい値を出力した後breakでループを抜けています。
"""

data_list = [1, 2, 3]    

for data in data_list:
    print(data)
    if data > 1:
        break
# 1
# 2

"""
実行してみると、2まで出力された後、breakが実行され処理が終了します。
"""


print("--- for-else ---")


"""
Pythonのfor文はelseと併用することができます。
elseブロックに記述した処理は、以下の動作となります。

forループ処理回数によらず実行される
breakした場合は実行されない
サンプルで動作を確認してみましょう。
"""

data_list = []    # 空のリスト

for data in data_list:
    print(data)
else:
    print('ループ処理が終りました')     # ループ処理が終りました

"""
ループで回すリストが空なので、forブロック内の処理は行われませんが、
elseブロック内の処理は呼びだされます。
また、breakと組み合わせて使用する場合が多いです。
例えば、数値のリストで負の数の要素をループで見つけ、
なければその旨を表示する場合、以下のように記述します。
"""

l = [0, 3, 1, 10]

for x in l:
    if x < 0:
        print('負の数を探知しました')
        break
else:
    print('負の数は見つかりませんでした')    # 負の数は見つかりませんでした

"""
breakしない場合は最後のメッセージが表示されますが、
breakすると最後のメッセージは表示されません。
"""


print("--- continue ---")


"""
continueを使用すると、その回の後続処理をスキップすることができます。
以下のサンプルでは数値のリストをループで処理し、printで表示させますが、
マイナスの場合は処理をスキップしています。
"""

l = [0, 3, 1, -10, 11, 6]

for x in l:
    if x < 0:
        print('負の数を探知しました。処理をスキップします。')
        continue
    else:
        print(x)
# 0
# 3
# 1
# 負の数を探知しました。処理をスキップします。
# 11
# 6
