# ジェネレータをリストに変換して確認する
even_data = (even for even in range(0, 10, 2))
# range(0, 10, 2))   0~10の偶数のシーケンス
print(list(even_data))
