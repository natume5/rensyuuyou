# 合計が21になる3つの値が出たら繰返しをブレイクする
from random import randint
# 値が見つかるまで無限ループする
while True:
    a = randint(1, 13)
    b = randint(1, 13)
    c = randint(1, 13)
    # 合計が21ならばブレイク
    if (a + b + c) == 21:
        break      # ブレイク

print(a, b, c)
