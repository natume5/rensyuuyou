# dice()を定義して5回呼び出す
from random import randint


# 関数を定義する
def dice():
    num = randint(1, 6)
    return num     # defからreturn numまでdice()関数の定義

# dice()を5回呼び出す
for i in range(5):
    result = dice()    # resultはdice()の戻り値が入る
    # dice()はdice()関数の呼び出し
    print(result)
