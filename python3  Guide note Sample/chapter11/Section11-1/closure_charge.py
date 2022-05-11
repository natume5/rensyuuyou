# priceを保持するクロージャを定義する


# クロージャの定義
def charge(price):
    # 関数の実態
    def calc(num):
        return price * num    # charge()の戻り値として関数のcalc()を返す
    return calc

# クロージャ(関数オブジェクト)を2種類作る
child = charge(400)    # 子供料金400円
adult = charge(1000)    # 大人料金1000円
# 料金を計算する
price1 = child(3)    # 子供3人  charge(400)で作られた関数を使って計算
price2 = adult(2)    # 大人2人  charge(1000)で作られた関数を使って計算
print(price1)
print(price2)
