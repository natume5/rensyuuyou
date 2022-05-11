class Orange:
    def __init__(self, w, c):
        """weight(重さ)はグラム"""
        self.weight = w
        self.collor = c
        self.mode = 0
        print("Created!")

# rotはオレンジを買ってからの日数とその期間の平均気温の二つの引数を受け取っている
    def rot(self, days, temp):
        """temp(温度)は摂氏"""
        self.mode = days * temp

orange = Orange(200, "orange")
print(orange.mode)
orange.rot(10, 37)
print(orange.mode)
