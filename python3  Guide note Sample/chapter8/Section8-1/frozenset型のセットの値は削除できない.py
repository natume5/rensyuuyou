# frozenset型のセットの値は削除できない
dataset = frozenset(["a", "b", "c"])
print(dataset.clear())     # frozenset型のセットはメゾットでの削除も出来ない
