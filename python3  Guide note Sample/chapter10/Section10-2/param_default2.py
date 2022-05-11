# キーワード引数を利用して特定の引数だけ指定する
def calc(size="M", num=6):    # 2つの引数に初期値がある
    unit_price = {"S": 120, "M": 150, "L": 180}
    price = unit_price[size] * num
    return(size, num, price)

# calc()を試す
a = calc()    # サイズ、個数共に省略
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")

b = calc("L")    # 個数を省略
print(f"{b[0]}サイズ、{b[1]}個、{b[2]}円")

c = calc(num=1)    # キーワード引数を利用して個数だけ指定する
print(f"{c[0]}サイズ、{c[1]}個、{c[2]}円")
