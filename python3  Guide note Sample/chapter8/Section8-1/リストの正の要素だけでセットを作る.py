# リストの正の要素だけでセットを作る
numbers = [-1.3, 1.2, -1.2, 1.1, 1.5, -1.1, 1.2, 1.1, 1.4]
num_set = {num for num in numbers if num > 0}
print(num_set)
