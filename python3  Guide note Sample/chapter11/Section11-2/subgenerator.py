# 値の生成とサブイテレータとサブジェネレータを利用する
# メインのジェネレータ


def main_gen(n):
    yield "start"
    yield from range(n, 0, -1)    # サブイテレータから値を作る
    yield from "abc"    # サブイテレータから値を作る
    yield from [10, 20, 30]    # サブイテレータから値を作る
    yield from sub_gen()    # サブジェネレータから値を作る
    yield "end"


# サブジェネレータ
def sub_gen():
    # sub_gen()上のサブジェネレータにかかる
    yield "X"
    yield "Y"
    yield "Z"
