# yen2dollar()とdollar2yen()が定義してあるモジュールファイル
# 円をドルに換算


def yen2dollar(yen, rate, charge=0):
    dollar = yen / (rate + charge)
    return dollar


# ドルを円に換算
def dollar2yen(dollar, rate, charge=0):
    yen = dollar * (rate - charge)
    return yen
