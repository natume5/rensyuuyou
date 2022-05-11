# Carクラス
class Car:
    # 初期化メゾット
    def __init__(self, color = "white"):
        self.color = color    # 引数で受け取った値を代入
        self.mileage = 0    # 0からスタート
    # インスタンスメゾット
    def drive(self, Km):
        # self   第一引数をselfにする
        self.mileage += Km
        msg = f"{Km}Kmドライブしました。総距離は{self.mileage}Kmです。"
        print(msg)
