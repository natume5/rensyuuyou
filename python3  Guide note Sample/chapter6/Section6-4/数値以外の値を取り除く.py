# 数値以外の値を取り除く
numbers = [2.1, 4, "", 2.2, "1", 3]
numbers = [num for num in numbers if isinstance(num, (int, float))]
print(numbers)    # intかfloatの数値だけを取り出す
