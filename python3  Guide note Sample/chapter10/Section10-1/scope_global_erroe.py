# グローバル変数の値を関数の中で10倍にする
v = 2    # グローバル変数


def calc():
    v = v * 10     # グローバル変数vを10倍にする
    # 上の式がエラーになる
    ans = 3 * v
    print(ans)

# calc()を実行
print(calc())
