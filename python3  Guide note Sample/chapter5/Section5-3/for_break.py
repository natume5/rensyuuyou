# リストnumlistから取り出した値が数値でなければブレイクする
numlist = [3, 4.2, 10, "x", 1, 9]     # 文字列が含まれている
sum = 0
for num in numlist:
    # numが数値でない時ブレイクする
    if not isinstance(num, (int, float)):     # intかfloat出ない時
        print(num, "数値ではありません。")
        break     # ブレイク
    sum += num
    print(num, "/", sum)
