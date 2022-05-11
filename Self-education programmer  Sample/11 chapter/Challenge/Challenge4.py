"""六角形を表すHexagonクラスを定義する。そのクラスに外周の長さを計算して返すメゾット
calculate_perimeterを定義する。そして、Hexagonオブジェクトを作って、
calculate_perimeterメゾットを呼び出し、結果を出力する。"""
# calculate perimeter→周辺を計算しなさい


class Hexagon():
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.side1 = s1
        self.side2 = s2
        self.side3 = s3
        self.side4 = s4
        self.side5 = s5
        self.side6 = s6

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
        +self.side4 + self.side5 + self.side6

hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print(hexagon.calculate_perimeter())
