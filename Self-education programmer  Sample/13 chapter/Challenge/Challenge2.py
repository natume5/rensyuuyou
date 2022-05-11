"""Square(四角形)クラスにchange_sizeメゾットを定義して、
そこに渡した数値の分だけSquareオブジェクトの横幅を増やしたり、
減らしたり(マイナス値の場合)しよう。"""


class Square():
    def __init__(self, s1):
        self.square = s1

    def calculate_perimeter(self):
        return self.square * 4

    def change_size(self, new_size):
        self.square += new_size   # +=はa = a + b に同じ

a_square = Square(100)
print(a_square.square)

a_square.change_size(200)
print(a_square.square)
