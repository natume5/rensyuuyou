# 元のネスティングを保ったままで要素の値を2倍したリストを作る
data = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
result = [[num * 2 for num in alist] for alist in data]
print(result)
