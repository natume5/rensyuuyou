# 2個のサイコロを振った合計を出力する行為を5回行う
from random import randint


# サイコロを定義する
def dice():
    num = randint(1, 6)
    return num     # dice()関数の定義

# 2個のサイコロを5回呼び出す
for i in range(5):
    dice1 = dice()    # 1個目のサイコロを振る
    dice2 = dice()    # 2個目のサイコロを振る
    sum = dice1 + dice2    # 2個のサイコロの目の合計
    print(f"{dice1}と{dice2}で合計{sum}")
