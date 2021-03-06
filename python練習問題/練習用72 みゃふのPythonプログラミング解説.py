#!/usr/bin/python
# -*- coding: UTF-8 -*-


print("--- みゃふのPythonプログラミング解説---")
print("--- リスト（list）の使い方  ---")


"""
リストは「複数の変数を1個の値として扱えるようにまとめる」機能のことです。

複数の変数を扱えるようにする方法はリスト以外にもありますが、リストが最も基本的で手軽な方法です。
ここでは「リストって何？」「リストはどうやって使うの？」といった方向けに、
リストの基本的な使い方を解説します。
"""


print("--- リストの初期化 ---")


"""
まずは基本的なリストの初期化方法を見ていきましょう。
Pythonでリストを初期化する時は、以下のように書きます。

リスト名 = [ ]

これで、空のリストが生成されます。

初期化・生成とともに、値を入れることができます。
その場合は、リスト名 = [ 要素, 要素, 要素 ] ように記述します。
最も簡単な方法は[]の中にカンマ区切りで値を入れる方法です。

[構文]

[値1, 値2, 値3, … ]

カンマの後にある空白はなくてもかまいませんが、見やすくするために入れると良いでしょう。
では実際にリストを作ってみましょう。
"""

list = [2, 5, 2, 1, 6]
print(list)     # [2, 5, 2, 1, 6]

"""
リストをそのまま出力すると、リストの中身がそのまま結果として出力されます。
また、リストの値は型が混合していても問題ありません。
"""

list = [2, "Hello", 2, True, 5.5]
print(list)    # [2, "Hello", 2, True, 5.5]


print("--- リストの参照・更新 ---")


"""
次に一度初期化したリストの値を参照・更新する方法を見ていきましょう。
参照・更新はどちらも「リストの値に割り当てられたインデックス番号を使ってアクセスする」点が同じです。

参照

まずは参照から見ていきましょう。
先ほどのコードから「Hello」の文字列にアクセスし、出力します。
"""

list = [2, "Hello", 2, True, 5.5]
hello = list[1]
print(hello)    # Hello

"""
重要なのは2行目です。変数listの後ろに[1]が付いています。
この「1」がインデックスです。つまり、Helloには1番のインデックスが割り当てられていることになります。
でも違和感がありますよね？「Helloは2番目じゃないのか？」と思う方が多いかと思います。
実は、リストのインデックスは先頭が「0」です。そこから順に1, 2, 3...と割り当てられます。
最初のうちは慣れないかもしれませんが、プログラミング言語の慣習でもあるので、
徐々に慣れていくと良いでしょう。
"""


print("--- 更新 ---")


"""
次に更新です。次の例を見てください。
"""

list = [1, 2, 6, 4, 5]
print('リスト更新前')
print(list)

list[2] = 3
print('リスト更新後')
print(list)

"""
参照の時と同じく、インデックス番号を使ってリストを更新しています。
今回は2番を指定したので、左から3番目の「6」を「3」に更新しています。
"""


print("--- リストに値を挿入する ---")


"""
今度は更新ではなく、値を挿入してみましょう。
値を挿入するメソッドは「append()」と「insert()」の2種類があります。

末尾に追加-append()

まずはappend()で挿入する方法を見ていきましょう。
append()は「リストの末尾に要素を追加する」メソッドです。
"""

list = []    # 空のリストを初期化
list.append('Hello')
list.append(100)
print(list)    # ['Hello', 100]

"""
単純に値を追加したいだけなら、append()で十分でしょう。


指定箇所に追加-insert()
次はinsertメソッドです。insert()は「指定した箇所に値を挿入する」メソッドです。
"""

list = ['H', 'l', 'l', 'o']
list.insert(1, 'e')
print(list)    # ['H', 'e', 'l', 'l', 'o']

"""
第一引数の「1」はインデックス番号です。指定したインデックスの場所に、第二引数の値を挿入します。
"""


print("--- 要素の削除 ---")

"""
次はリストの要素を削除してみましょう。
要素を削除するには、del、pop()、remove()を使います。

構文 - del

まずはdelの使い方から見ていきましょう。delはpop()、
remove()と異なりPythonの構文なので注意しましょう。
delの後に要素を指定することで削除できます。
"""

num_list = [1, 2, 3, 4, 5]
del num_list[2]
print(num_list)    # [1, 2, 4, 5]

"""
また、delはインデックス番号を指定しない場合、リストそのものを削除することもできます。

num_list = [1, 2, 3, 4, 5]
del num_list
print(num_list)

[出力結果]

NameError: name 'num_list' is not defined

NameErrorは未定義の変数を参照しようとしたときに起こるエラーなので、
num_list変数が削除されているのが分かります。


要素を抜き出す-pop()

次にpop()です。pop()は削除というよりリストから要素を抜き出し返却する処理を行います。
"""

num_list = [1, 2, 3, 4, 5]
end = num_list.pop()
print(num_list)    # [1, 2, 3, 4]
print(end)    # 5

"""
endにはnum_listからpop()して返ってきた末尾の5が格納されているのが分かります。
またこのpop()ですが、引数で位置を指定することもできます（指定なしの場合はデフォルトで「-1」）。
"""

num_list = [1, 2, 3, 4, 5]
three = num_list.pop(2)
print(num_list)    # [1, 2, 4, 5]
print(three)    # 3

"""
pop()の引数にインデックス番号を指定することで、3を抜き出すことができました。


要素を指定して削除-remove()

最後にremove()を見てみましょう。
delやpop()がインデックス番号を指定していた一方で、
remove()は要素の値をそのまま指定して削除します。
"""

str_list = ['a', 'b', 'c']
str_list.remove('b')
print(str_list)

"""
「b」を直接指定して要素を削除しました。remove()はpop()と違い戻り値はありません。
また、remove()は指定した値の「最初の要素のみ削除」するので、
全て削除したい場合は次のようにします。
"""

str_list = ['a', 'b', 'c', 'b', 'd', 'b']
target = 'b'
while target in str_list:
	str_list.remove(target)

print(str_list)    # ['a', 'c', 'd']

"""
while..inは指定したtargetがstr_listから全て削除されるまでループし続けるので、
このような実装ができます。


要素の削除はエラーに注意

delとpop()はリストの要素数を超過したインデックス番号を指定するとIndexErrorになります。
回避するにはlen()を使うと良いです。len()はリストの要素数を返却する関数です。
"""

num_list = [1, 2, 3, 4, 5]
target = 5
length = len(num_list)
print(length)
if length > target:    # 5 > 5 False
	num_list.pop(target)     # 5
print(num_list)     # [1, 2, 3, 4, 5]

"""
num_listの要素数は5つなので、len()は5を返却しています。
取得した要素数と削除したいインデックス番号(target)を比較して、
要素が存在する場合だけpop()を実行しています。
次にremove()です、remove()は存在しない要素の値を指定するとValueErrorになります。
リスト内にその値が存在するか確認するにはif..inを使うと便利です。
"""

str_list = ['a', 'b', 'c']
target = 'd'
if target in str_list:
	str_list.remove(target)

print(str_list)    # ['a', 'b', 'c']

"""
if..inを使うことで、指定したリスト内にtargetの文字列が存在するかチェックできます。
リスト内に「d」はいないので、上のコードではremove()はスルーされています。
"""


print("--- リストの連結 ---")


"""
次は2つ以上のリストを連結して1つのリストにしてみましょう。
"""

num_list = [1, 2, 3]
str_list = ['a', 'b', 'c']
print(num_list + str_list)    # [1, 2, 3, 'a', 'b', 'c']

"""
リストは「+」演算子を使って連結することができます（「+=」で連結することもできます）。
また、extend()を使うことでも連結可能です。
"""

num_list = [1, 2, 3]
str_list = ['a', 'b', 'c']
num_list.extend(str_list)
print(num_list)     # [1, 2, 3, 'a', 'b', 'c']


print("--- リストのスライス ---")


"""
リストから一部分だけ取り出して別のリストを作りたい場合はスライスという操作を行います。
スライスはリストの取り出したい部分の開始インデックスと終了インデックスを指定します。

[書式]

リスト[開始位置 : 終了位置]

それぞれの位置は省略可能で、開始位置を省略した場合はリストの最初から、
終了位置を省略した場合は最後まで取り出します。
"""

str_list = ['a', 'b', 'c', 'd', 'e']
print(str_list[1:3])    # ['b', 'c']
print(str_list[1:])    # ['b', 'c', 'd', 'e']
print(str_list[:3])    # ['a', 'b', 'c']
print(str_list[:])    # ['a', 'b', 'c', 'd', 'e']

"""
このスライスですが、開始位置はそのままインデックス番号として使われますが、
終了位置は「終了位置 - 1」のインデックス番号を指定する点に注意が必要です。
例えば上記の一番上の例では、
開始位置の「1」はそのままインデックス番号1の「b」を開始位置としていますが、
終了位置の「3」は「d」ではなく「c」を指定しています。
"""


print("--- リストの並び替え ---")


"""
次はリスト内の要素の並び替え方法を見ていきましょう。

要素の並び替えはsort()またはsorted()で行えます。

元のリストの並び替え-sort()

sort()は単純に元のリストを直接並び替えるメソッドです。
何も指定しない場合は昇順で並び替えますが、
reverseにTrueを指定することで降順にすることも可能です。
"""

str_list = ['b', 'c', 'a']
str_list.sort()
print(str_list)     # ['a', 'b', 'c']
str_list.sort(reverse=True)    # 降順
print(str_list)    # ['c', 'b', 'a']

"""
新しいリストを作成-sorted()

Sorted()はSort()とほぼ同じですが、
元のリストではなく新しいリストを作成して返却するところが異なります
（あとSort()はリストのメソッドですが、Sorted()は関数なので使い方が違います）。
"""

str_list= ['b', 'c', 'a']
sorted_list = sorted(str_list)
print(sorted_list)    # ['a', 'b', 'c']
reverse_sorted_list = sorted(str_list, reverse=True)
print(reverse_sorted_list)     # ['c', 'b', 'a']


"""
文字数順に並び変え-len()

sort()とsorted()では比較関数を指定することができます。
例えばlen()を比較関数に指定することで、文字列の長さで並び替えることができます。
"""

str_list = ["blue", "red", "yallow"]
str_list.sort(key=len)    # 括弧は付けない
print(str_list)    # ['red', 'blue', 'yallow']
str_list.sort(key=len, reverse=True)    # 降順もできる
print(str_list)      # ['yallow', 'blue', 'red']


print("--- 合計・最大・最小 ---")


"""
リスト内の要素の合計・最大・最小を取得するには、それぞれsum(), max(), min()を使用します。
"""

num_list = [28, 11, 87, 91, 7, 43]
print(sum(num_list))    # 267
print(max(num_list))    # 91
print(min(num_list))    # 7


print("--- 応用：リストの内包表記 ---")


"""
リスト内包表記はPythonらしい記述方法で、内包表記を使うことで、
純粋にlistを初期化するよりも簡潔にリストを初期化できます。
難しい日本語を使っていますが、やっていることは簡単です。
まずは例を見てみましょう。
次のプログラムは「リスト内の数値を10倍し、
新しいリストに代入する」処理を実行しています。
"""

list = [1, 2, 3, 4, 5]
list_ten_times = [num * 10 for num in list]    # リスト内包表記
print(list_ten_times)    # [10, 20, 30, 40, 50]

"""
重要なのは2行目の[]内です。次のような構文になっています。

[構文]

[式 for 式で使う変数 in イテラブル]

「イテラブル」とは、リストのような「複数の値を1個ずつ取り出せる」ようなデータのことです。
リストのほかに、タプルや辞書、文字列などが該当します。

リスト内包表記は

    「イテラブル」の値を先頭から1つずつ取り出し
    それを「式で使う変数」に代入し
    最後に「式」の結果を先頭からリストに加えていく

という処理をしています。

今回の例だと、まずlistから「1」を取り出して1 * 10を計算し、list_ten_timesに入れる。
次に「2」を取り出して2 * 10を計算し、またlist_ten_timeに入れる...という処理を、
listの最後の値まで繰り返しています。

リスト内包表記を使うことで、リストを初期化したり、
「リスト内の値を全て書き換える」といったことを容易に行えます。
"""


print("--- 応用：多次元リスト ---")


"""
最後に多次元リストについても解説します。

ここまで見てきたリストは全て一次元リストと呼ばれるリストで、
多次元リストとは二次元以上のリストのことを指します。

[書式（二次元リスト）]

[[要素1-1, 要素1-2, 要素1-3], [要素2-1, 要素2-2, 要素2-3], ...]

まずは初期化してみましょう。 
"""

two_d_list = [[1, 2, 3], [4, 5, 6]]
print(two_d_list)    # [[1, 2, 3], [4, 5, 6]]

"""
 多次元リストの要素を参照する

多次元リストの要素を参照・更新する場合はインデックス番号を2つ指定します。
また、1つだけ指定した場合はリスト内のリストを取得できます。
"""

two_d_list = [[1, 2, 3], [4, 5, 6]]
print(two_d_list[1][1])    # 2つ目のリストの2つ目の要素　　5
print(two_d_list[0])    # 1つ目のリスト　　　[1, 2, 3]

"""
リスト内のリストに要素を追加・削除する

リスト内のリストに要素を追加する場合は、
追加したいリストのインデックス番号を指定することで可能です。
また、同じ方法で削除することもできます。
"""

two_d_list = [[1, 2, 3], [4, 5, 6]]
two_d_list[0].append(10)    # 1つ目のリストに10を追加
two_d_list[1].pop()    # 2つ目のリストの最後の要素をpop
print(two_d_list)    # [[1, 2, 3, 10], [4, 5]]
