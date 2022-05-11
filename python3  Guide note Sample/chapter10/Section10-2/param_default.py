# 引数に初期値がある関数
def calc(size, num=6):    # numには初期値がある
    unit_price = {"S": 120, "M": 150, "L": 180}
    price = unit_price[size] * num
    return(size, num, price)

# calc()を試す
a = calc("S", 2)    # sizeは"S",numは2で計算する
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")

b = calc("M")    # numが省略されている 個数を省略(サイズ変更不可)
print(f"{b[0]}サイズ、{b[1]}個、{b[2]}円")

c = calc("L", 4)
print(f"{c[0]}サイズ、{c[1]}個、{c[2]}円")
