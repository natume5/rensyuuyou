# ランダムな並びのリストを作る
import random      # randomモジュールをインポートする
numbers = list(range(10))     # 0~9のリストを作る
random.shuffle(numbers)
print(numbers)
