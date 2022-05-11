# ジェネレータ式を使う
odd_gen = (odd for odd in range(1, 6, 2))    # odd_genジェネレータを作る
# range(1, 6, 2)   1~6の奇数のシーケンス
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))
print(next(odd_gen))
