# 数値が入った変数を代入しても参照が渡される
num_a = 10
num_b = num_a         # 参照を代入
print(num_b)
print(num_a is num_b)    # 同じオブジェクトかどうか比較
