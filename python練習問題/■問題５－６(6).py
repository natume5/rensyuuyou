# !/usr/bin/python3
# -*- coding: utf-8 -*-


# （６）「入力した数を表示する作業を，0が入力されるまで繰り返す，
# 　ただし，10回を過ぎたら終了する」プログラムをfor文を用いて作れ


"""　while文の場合
numbers = int(float(input("数を入力して下さい。:")))
i = 0

while True:
    numbers = int(float(input("数を入力して下さい。:")))
    i += 1
    if i == 10:    # numberが11の時にぬける
        break
    if numbers == 0:
        break


for文の有限ループの例

l = [0]
for i in l:
    print(i)
    l.append(i + 1)
    if i == 10:
        break
"""

kazu = [0]

for i in range(10):
    print(float(input("数を入力して下さい。: {}回目")))
    kazu.append(i)
    if i == 10:
        print("中断します")
        break
    if i == 0:
        break
