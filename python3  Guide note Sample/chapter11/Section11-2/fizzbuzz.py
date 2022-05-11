# FizzBuzzジェネレータ


def fizzbuzz():    # fizzbuzzジェネレータの定義
    n = 1
    while True:
        if n % 15 == 0:    # 3と5の倍数なので"FizzBuzz"
            yield "FizzBuzz"
        elif n % 3 == 0:    # 3の倍数なので"Fizz"
            yield "Fizz"
        elif n % 5 == 0:    # 3の倍数なので"Buzz"
            yield "Buzz"
        else:
            yield str(n)    # そのままの数字
        n = n + 1    # カウントアップ

# fizzbuzz()でgameジェネレータを作って20回呼び出す
game = fizzbuzz()    # gameジェネレータを作る
for i in range(0, 20):
    print(next(game))    # 次の値を取り出して表示する
