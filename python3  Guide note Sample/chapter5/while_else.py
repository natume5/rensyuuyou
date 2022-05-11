from random import randint
numbers = []
while len(numbers) < 10:
    n = randint(-10, 90)
    if n < 0:
        print("中断されました")
        break
    if n in numbers:
        continue
    numbers.append(n)
else:
    print(numbers)