# リスト内包表記を使わずに書いたコード
data = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
result = []
for alist in data:    # dataからリストをalistに取り出す
    for num in alist:
        result.append(num * 2)    # numを2倍にしてresultリストに追加する
print(result)
