# リストから要素をランダムに取り出す
import random      # ランダムモジュールをインポート
fruits = ["apple", "orange", "banana", "peach"]
dessert = random.choice(fruits)     # 実行する度にリストから1つ選ばれる
print(dessert)
