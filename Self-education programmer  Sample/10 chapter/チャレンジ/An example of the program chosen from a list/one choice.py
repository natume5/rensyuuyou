# 1つだけ抽出したいときは random ライブラリの choice 関数を使います
import random

marks = ["club", "diamond", "heart", "spede"]
numbers = range(1, 14)
cards = [(m, n) for m in marks for n in numbers]

random.choice(cards)   # トランプのカードのいずれか
