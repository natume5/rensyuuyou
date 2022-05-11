# クラスメゾットcountup()
from car_class3 import Car


# Carクラス
class Car:
    # クラス変数
    maker = "PEACE"    # 自動車メーカー
    count = 0    # 台数

    # クラスメゾット
    @classmethod
    def countup(cls):
        cls.count += 1
        print(f"出荷台数:{cls.count}")

    # 初期化メゾット
    def __init__(self, color = "white"):
        Car.countup()    # カウントアップする   クラスメゾットcountup()を実行
        self.mynumber = Car.count
        # 自分の番号  インスタンス変数mynumberに
        self.color = color
        # 初期化で受け取った値を代入  自分の番号として保存
        self.mileage = 0    # 0からスタート

    # インスタンスメゾット
    def drive(self, Km):
        self.mileage += Km
        msg = f"{Km}Kmドライブしました。総距離は{self.mileage}Kmです。"
        print(msg)
