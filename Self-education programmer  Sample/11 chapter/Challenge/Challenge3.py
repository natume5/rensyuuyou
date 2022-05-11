"""三角形を表すTriangleクラスを定義して、面積を返すareaメゾットを持たせる。
そしてTriangleオブジェクトを呼び出して、結果を出力する。"""


class Triangle():
    def __init__(self, b, h):
        self.bottom = b   # bottom=底辺
        self.height = h

    def area(self):
        return self.bottom * self.height / 2

triangle = Triangle(2, 3)
print(triangle.area())
