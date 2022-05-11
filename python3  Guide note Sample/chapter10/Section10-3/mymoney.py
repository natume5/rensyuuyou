# exchange.pyで定義してあるyen2dollar()を使う
import exchange    # exchangeモジュールを読み込む
# 関数が定義されているファイルを指定
yen = 25000
rate = 114.22    # 円/ドル(中間値)
charge = 1.0    # 為替手数料
dollar = exchange.yen2dollar(yen, rate, charge)    # 関数を呼び出し
print(f"{dollar: ,.2f}ドル")
