# 数列の値を生成するジェネレータ


def num_generator():
    n = 0
    while True:
        num = n * n + 2 * n + 3    # 数列式
        yield num    # ジェネレータが順に返す値
        n += 1
        # ここまでがジェネレータを作る関数


# 何かを行う関数
def do_something(num):
    return(num % 2, num % 3)

# ジェネレータが返す値を使って処理を行う
gen = num_generator()    # genジェネレータを作る
for i in range(1, 10):
    num = next(gen)    # ジェネレータから次の値を取り出す
    result = do_something(num)    # ジェネレータから取り出した値で実行
    print(result)
