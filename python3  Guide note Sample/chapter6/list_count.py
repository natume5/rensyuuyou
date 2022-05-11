result = [1, 1, 0, 0, 1, 0, 1, 1]
half = len(result) / 2
point = result.count(1)
if point >= half:
    print("合格")
else:
    print("不合格")
