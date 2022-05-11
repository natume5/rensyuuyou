from random import randint
size = randint(5, 20)
weight = randint(20, 40)

if (size >= 10) and (weight >= 25):
    result = "合格"
else:
    result = "不合格"

text = f"サイズ{size}、重量{weight}:{result}"
print(text)
