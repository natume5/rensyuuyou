# 2で割った余りが0,Falseになることを使って奇数か偶数かを振り分ける
from random import randint
num = randint(0, 100)

if num % 2:
    result = "奇数"
else:
    result = "偶数"
print(num, result)
