# for文が途中でbreakeされなかったらばelseブロックを実行して終わる
numlist = [3, 4.2, 10, "x", 1, 9]
sum = 0
for num in numlist:
    # umが数値でない時処理をブレイク
    if not isinstance(num, (int, float)):
        print(num, "数値ではない値が含まれていました。")
        break    # ブレイク
    sum += num
else:
    # breakされなかった時は合計した値を出力する
    print("合計", sum)
