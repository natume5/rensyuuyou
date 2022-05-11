# リストが空でない時末尾の値を取り出す
fruits = ["apple", "orange", "banana", "peach"]
# fruitsが空でないかチェックする
if fruits:         # リストが空の時はFalseになる
    dessert = fruits.pop()
    print("デザートは" + dessert)
print(fruits)
