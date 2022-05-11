# 先に範囲でスライスする場合とステップでスライスする場合の違い
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(letters[1:5][::2])     # 先に範囲でスライスする
print(letters[::2][1:5])     # 先にステップでスライスする
print(letters[1:5:2])        # 範囲とステップを同時に指定する
