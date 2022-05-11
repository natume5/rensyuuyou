# 関数の外で作った変数vを利用する
v = 2    # 変数を設定する――calc()の外でvに値を代入


def calc():
    ans = 3 * v     # 変数vを利用する――vには2が入っている
    print(ans)

# calcc()を実行
print(calc())
print(v)
