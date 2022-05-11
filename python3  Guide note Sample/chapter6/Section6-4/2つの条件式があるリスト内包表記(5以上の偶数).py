# 2つの条件式があるリスト内包表記(5以上の偶数)
numbers = [4, 12, 21, 32, 8, 6, 11, 16]
result = [num for num in numbers if num >= 5 if num % 2 == 0]
print(result)    # (if num >= 5)→5以上、(if num % 2 == 0)→偶数
