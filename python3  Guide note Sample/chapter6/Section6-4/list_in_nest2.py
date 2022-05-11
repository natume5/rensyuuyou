# リスト内包表記を使わずに書いたコード
data = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
result = []
for alist in data:    # dataからリストをalistに取り出す
    temp = []
    for num in alist:
        temp.append(num * 2)    # numを2倍してtempリストに追加する
    else:
        result.append(temp)    # alistの値を2倍にしてresultに追加する
print(result)
