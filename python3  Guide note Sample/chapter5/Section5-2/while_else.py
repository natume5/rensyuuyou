# 重複しない値が10個入ったリストを作る。ただし、マイナスが出たら中断
from random import randint
numbers = []
# numbersの値が10個になるまで繰り返す
while len(numbers) < 10:
    n = randint(-10, 90)    # -10~90の乱数
    if n < 0:
        # nがマイナスならブレイク
        print("中断されました")
        break
    if n in numbers:
        # nがnumbersに含まれていたらスキップ
        continue
    # numbersにnを追加
    numbers.append(n)
else:
    print(numbers)     # 繰返しが終わったら実行
