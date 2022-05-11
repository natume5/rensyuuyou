# PersonクラスをスーパークラスにするPlayerクラス


# スーパークラス
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


# サブクラス
class Player(Person):
    def __init__(self, name, age, number, position):
        super().__init__(name, age)    # スーパークラスの初期化メゾットを呼び出す
        self.number = number
        self.position = position
