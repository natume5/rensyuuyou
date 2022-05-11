# 1以上2未満の数値だけを取り出したリストを作る
numbers = [2.1, 0.2, 0.3, 1.4, 3.1, 0.3, 1.6]
result = [num for num in numbers if 1 <= num < 2]
print(result)    # 1以上2未満の数値だけを取り出す
