# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題5－11（whileとif文の練習）
数当てゲームを作りたい．
１から100までの適当な整数を用意し，
キーボードから入力した整数がその数と同じならば 終了するプログラムを作成する．
ただし，はずれたときは，
正解よりも大きかったか小さかったかを表示して ヒントを出すようにすること．
"""


import random


ans = random.randint(1, 100)
max_count = 6
print("1～100の数字の中からひとつを選んでください。")
print('その数字を', max_count, '回以内に当ててください。')

for i in range(1, max_count + 1):
    print(i, '回目、いくつでしょう？')
    num = int(input())
    if num == ans:
        print('当たりです')
        break
    elif i == max_count:
        pass
    elif num > ans:
        print("もっと下です。")
    else:
        print("もっと上です。")
else:
    print('残念 正解は', ans, 'でした')
