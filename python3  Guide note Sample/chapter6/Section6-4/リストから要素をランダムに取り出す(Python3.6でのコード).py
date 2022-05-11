# リストから要素をランダムに取り出す(Python3.6でのコード)
import secrets    # secretsをインポート
fruits = ["apple", "orange", "banana", "peach"]
dessert = secrets.choice(fruits)
print(dessert)
