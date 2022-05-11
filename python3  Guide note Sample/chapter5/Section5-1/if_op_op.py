# 5以上、8以下の時にTrue
from random import randint
a = randint(0, 10)

if 5 <= a <= 8:
    print(a, "合格")
else:
    print(a, "不合格")
