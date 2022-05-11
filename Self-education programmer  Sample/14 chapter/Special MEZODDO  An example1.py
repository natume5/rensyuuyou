"""特殊メゾッド　例(クラスから作成したインスタンスオブジェクトをprint関数に渡した)"""


class Lion:
    def __init__(self, name):
        self.name = name


lion = Lion("Dilbert")
print(lion)
