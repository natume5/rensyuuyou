# 数値でない値を取り出したら無視して、数値だけを処理する
numlist = [3, 4.2, 10, "x", 1, 9]     # 文字列が含まれる
sum = 0
for num in numlist:
    # numが数値でない時処理をスキップ
    if not isinstance(num, (int, float)):
        print(num, "数値ではありません。")
        continue     # スキップ
    sum += num
    print(num, "/", sum)
