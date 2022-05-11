# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題５－６
（１）forの2重ループを使って，九九の表を書くプログラムを作成せよ．
ただし，表の罫線を書くのは大変なので，中身の数字だけを書く．

（２）9×9 の足し算の答えを表にせよ．

（３）12×12 の掛け算の答えを表にせよ．
"""

# （１）forの2重ループを使って，九九の表を書くプログラムを作成せよ．
# ただし，表の罫線を書くのは大変なので，中身の数字だけを書く

for i in range(1, 10):
    for j in range(1, 10):
        print('{x:3}'.format(x=i * j), end='')
        # x=i * yでいつもの九九に、x=i + 1 * yで足し算になる
    print()

"""
endはprintでデータを出力した後(末尾)に出力するものを指定
今回はスペース
何もしていななければ、改行コードが指定される。

解答例1    yahoo!japan知恵袋より
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j end='')
    print()


解答例２
for i in range(1, 10):
    for j in range(1, 10):
        ans = i * j
        print('{0}x{1}={2}'.format(i,j,ans))


解答例3   Python の for 文による繰返し より
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:>4d}", end="")
    print() # 改行


解答例4    【Python】while文を使って繰り返し処理を行う！サンプルコード付き！ より
i = 1
j = 1

while i <= 9:
    j = 1
    while j <= 9:
        print(i*j,end = " ")
        j = j + 1
    i = i + 1
    print("\n")


解答例5    2重ループより
i = 1   #かけられる数

while i < 10:
    j = 1   #かける数
    while j < 10:
        print(i * j, end=" ")
        j = j + 1
    print()   #改行
    i = i + 1

プログラムの書き換え問題
計算結果をそのまま出力させると，
1桁と2桁の数が交った表になり，列（かける数）をそろえて出力することができない。
i * j（かけられる数×かける数）を右寄せ2文字で出力させるように上のプログラムを改良するには
ヒント

i * jが10未満かどうかの条件判断を行い，真の場合にスペース1文字を出力させる文
print(' ', end="")を書き加えればよい。
あるいは，%演算子やformatメソッドを用いる方法もある。
解答例
99.pyの5行目のprint文を次のいずれかの文に書き換えればよい。

print("%2d" % (i * j), end=" ")
print("{0:>2}".format(i * j), end=" ")


解答例6    九九の表を二次元リストで表示する方法についてより
for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i * j:3}', end='')
    print()

"""

# （２）9×9 の足し算の答えを表にせよ．

for i in range(1, 10):
    for j in range(1, 10):
        print('{x:3}'.format(x=i + 1 * j), end='')
    print()


# （３）12×12 の掛け算の答えを表にせよ．

for i in range(1, 13):
    for j in range(1, 13):
        print(f'{i * j:4}', end='')
    print()
