# チケットの枚数だけループして、乱数を足し合わせた値を作る
from random import randint
tickets = 5
point = 0
fmt = "{:>3}"
# ticketが正の場合は繰り返す
while tickets > 0:
    v = randint(1, 20)
    print(fmt.format(v))
    point += v
    tickets -= 1

print("-" * 3)
print(fmt.format(point))
