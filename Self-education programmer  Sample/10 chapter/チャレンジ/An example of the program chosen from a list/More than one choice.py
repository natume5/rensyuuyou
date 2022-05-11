# 複数枚抽出したいときは random ライブラリの sample 関数を使います。
import random

marks = ['club', 'diamond', 'heart', 'spade']
numbers = range(1, 14)
cards = [(m, n) for m in marks for n in numbers]

random.sample(cards, 5)
# => 52枚のカードの中からランダムに5枚
