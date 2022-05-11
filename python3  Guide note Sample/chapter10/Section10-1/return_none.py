# 引数が数字ではない時は中断する
def calc(num):
    unit_price = 180    # 単価
    if not num.isdigit():    # 数字かどうかチェックする
        return None    # 数字出ない時は中断する
    price = int(num) * unit_price
    return price


#  キーボードから引数を入力して試す
while True:
    num = input("個数を入力して下さい。(qで終了。)")
    if num == "":
        continue
    elif num == "q":
        break


# calc()で計算する
    result = calc(num)    # calc()を呼び出す
    print(result)
