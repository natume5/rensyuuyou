def calc(size="M", num=6):
    unit_price = {"S": 120, "M": 150, "L": 180}
    price = unit_price[size] * num
    return(size, num, price)


a = calc()
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")
b = calc("L")
print(f"{b[0]}サイズ、{b[1]}個、{b[2]}円")
c = calc(num=1)
print(f"{c[0]}サイズ、{c[1]}個、{c[2]}円")
