"""Squareクラスにsquare_listクラス変数を追加する。
そして、新しくSquareクラスのオブジェクトが作られるたびに、
そのオブジェクトをこのリストに追加する。"""


class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.square = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    def what_am_i(self):
        super().what_am_i()
        print("I am a Square.")


a_square = Square(2)
print(Square.square_list)
anoter_square = Square(3)
print(Square.square_list)
