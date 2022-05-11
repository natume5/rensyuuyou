# frozeset型のセットにadd()で要素を増加するとエラーになる
dataset = frozenset(["a", "b", "c"])
print(dataset.add("x"))    # frozenset型のセットは要素の変更などはできない
