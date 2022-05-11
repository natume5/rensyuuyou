# 4行3列の点の座標を求める
for i in range(4):       # 4行
    print()      # 各行の改行
    for j in range(3):       # 3行
        x = j * 2
        y = i * 3
        print(f"({x}, {y})", end="")
print()      # 最後の改行
