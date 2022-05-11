# グローバル変数の値を関数の中で10倍にする
v = 2    # グローバル変数


def calc():
    v_local = v * 10    # vはグローバル変数 グローバル変数vを10倍にする
    ans = 3 * v_local
    print(ans)

# calc()を実行
print(calc())
