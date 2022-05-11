# ネスティングしたリストの要素を全て取り出して2倍にしたリストを作る
data = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
result = [num * 2 for alist in data for num in alist]
print(result)    # (for alist in data)→外側のネスト、(for num in alist)→内側のネスト
