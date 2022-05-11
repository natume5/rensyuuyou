# ジェネレータに値を送る


def testgen():
    n = 0
    while True:
        received = yield n
        # yieldで返すだけでなく、send()された値を受けてreceivedに代入する。
        if received:
            n = received
            # send()で受け取った値がreceivedに入っている時に実行する
        else:
            n = n + 1


gen = testgen()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
gen.send(10)    # genジェネレータに10を送る
print(next(gen))
print(next(gen))
