"""Rectangle(長方形)とSquare(四角形)クラスを作る。
両方のクラスに、その図形の外周の長さを計算して返す
calculate_perimeterメゾットを定義する。
そして、RectangleとSquareのオブジェクトを作って、それぞれの
calculate_perimeterメゾットを呼ぶ。"""


class Rectangle():
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square():
    def __init__(self, s1):
        self.square = s1

    def calculate_perimeter(self):
        return self.square * 4

a_rectangle = Rectangle(1, 2)
a_square = Square(2)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())
