"""Shapeクラスを定義する。呼ばれたら"I am a shape"を返すメゾット
what_am_iを定義する。前のチャレンジで定義したRectangleとSquareクラスを
変更して、このShapeクラスを継承させる。そして、RectangleとShapeのオブジェクトを
生成して、このチャレンジで追加したメゾットwhat_am_iを呼び出す。"""


class Shape():
    def what_am_i(self):
        print("I am a shape.")


class Rectangle(Shape):
    def __init__(self, w, l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2


class Square(Shape):
    def __init__(self, s1):
        self.square = s1

    def calculate_perimeter(self):
        return self.square * 4

a_rectangle = Rectangle(1, 2)
a_square = Square(2)

a_rectangle.what_am_i()
a_square.what_am_i()
