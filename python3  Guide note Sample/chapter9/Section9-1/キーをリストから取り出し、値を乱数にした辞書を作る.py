# キーをリストから取り出し、値を乱数にした辞書を作る
from random import randint
keys = ["green", "red", "blue", "yellow"]
data = {key: randint(1, 100) for key in keys}
# keyからキーにする文字列を順に取り出す
print(data)
