# 重複しない値が10個入ったリストを作る
from random import randint
numbers = []     # 空のリスト
# numbersの値が10個になるまで繰り返す
while len(numbers) < 10:
    n = randint(0, 100)     # 0~100迄の乱数
    if n in numbers:
        # nがnumbersに含まれていたらスキップ
        continue
    # numbersにnを追加
    numbers.append(n)     # 初めての数値ならばnumbersをリストに追加

print(numbers)
