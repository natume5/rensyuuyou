# 3回間違えるか、"q"と入力されるまで出題を繰り返す
from random import randint
miss = 0       # 間違えた数
correct = 0    # 正解数
print("問題！3回間違えたら終了。qで止める")
while miss < 3:
    a = randint(1, 100)
    b = randint(1, 100)
    ans = a + b
    # 問題を出題し、キーボードからの入力待ちにする
    question = f"{a} + {b}は？"
    value = input(question)      # キーボードからの入力をvalueに代入
    # qと入力されたら中断
    if value == "q":
        break       # ブレイク
    # 解答が正解かどうか判定
    if value == str(ans):
        correct += 1
        print("正解！")
    else:
        miss += 1      # 間違いをカウント
        print("間違い！", "x" * miss)     # 間違いの数だけx
print("-" * 20)
print("正解:", correct)
print("間違い:", miss)
