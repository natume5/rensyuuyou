# 引数と戻り値がある関数オブジェクトを処理する
def calc(func, arg=1):
    price = func(arg)    # 引数で受け取った関数funcとargでfunc(arg)を実行
    return price


def child(arg):
    # calc()に渡して実行する関数
    return 400 * arg


def adult(arg):
    # calc()に渡して実行する関数
    return 1200 * arg

# 年齢によって計算する関数を変える
age = 12
num = 3
if age < 16:
    price = calc(child, num)    # 16歳未満ならばchild()で計算
else:
    price = calc(adult, num)    # 17歳以上ならばadult()で計算


print(f"{age}歳、{num}人は{price}円です。")
