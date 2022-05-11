# !/usr/bin/python3
# -*- coding: utf-8 -*-


"""
■問題5－16
キーボードから整数xを入力し，xの数だけ#を横に並べて表示する，
という作業を繰り返すプログラムを作れ．
ただし，入力した数が0なら終了するようにします．
例えば，5,3,15,0と入力した場合にはこのようになる．

5
＃＃＃＃＃
3
＃＃＃
15
＃＃＃＃＃＃＃＃＃＃＃＃＃＃＃
0

参考　第18回.例外処理（try文）とexception一覧
　　　
"""


x = int(input("数値を入力して下さい。入力した数だけ#が出ます。:"))

try:
    for i in range(0, x):
        try:
            print('#', end='')
        except IndexError as e:
            print(f'{i}:{e}')
except ZeroDivisionError:
    print("ゼロは表示できません。")
except ValueError:
    print("整数を入力して下さい。")
except TypeError as e:
    print(f"{i}:{e}")
print()
