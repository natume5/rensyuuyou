# クラス変数を追加したCarクラス
# Carクラス


class Car:
    # クラス変数
    maker = "PEACE"    # 自動車メーカー
    count = 0    # 台数

    # 初期化メゾット
    def __init__(self, color = "white"):
        self.color = color    # 引数で受け取った値を代入
        self.mileage = 0    # 0からスタート

    # インスタンスメゾット
    def drive(self, Km):
        self.mileage += Km
        msg = f"{Km}Kmドライブしました。総距離は{self.mileage}Kmです。"
        print(msg)
