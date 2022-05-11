# a,bともに40以上で、a+bが120以上ならば合格
# randomモジュールのrandint関数を読み込む
from random import randint
a = randint(0, 100)
b = randint(0, 100)
# 判定(3つの条件がTrueの時合格)
if a >= 40 and b >= 40 and (a + b) >= 120:
    result = "合格"
else:
    result = "不合格"

# 結果の出力
text = f"a{a}, b{b}, 合計{a + b}:{result}"
print(text)
