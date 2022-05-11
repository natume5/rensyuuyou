# resultに含まれている1が半数以上ならば「合格」
result = [1, 1, 0, 0, 1, 0, 1, 1]
half = len(result) / 2    # 要素の個数の半分
point = result.count(1)     # 1の個数
if point >= half:
    print("合格")
else:
    print("不合格")
