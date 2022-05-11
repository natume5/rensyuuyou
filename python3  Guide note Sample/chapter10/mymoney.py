import exchange
yen = 25000
rate = 114.22
change = 1.0
dollar = exchange.yen2dollar(yen, rate, change)
print(f"{dollar :, 2f}ドル")
