# 例外処理を組み込んだコード
fruits = []       # 空で試している
# 例外処理に組み込む
try:
    dessert = fruits.pop()
    print("デザートは" + dessert)
    print(fruits)
except:
    print("エラーになりました。")
