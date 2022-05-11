def calc(num):
    unit_price = 180
    try:
        num = float(num)
        return num * unit_price
    except:
        return None
while True:      # return Noneの後2行空けない
    num = input("個数を入れてください。(qで終了)")
    if num == "":
        continue
    elif num == "q":
        break
    result = calc(num)    # breakの後2行空けない
    print(result)
