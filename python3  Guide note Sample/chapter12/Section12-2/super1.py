# Personクラスの初期化メゾットはplayerクラスの初期化メゾットにオーバーライドされる


# スーパークラス
class Person():
    def __init__(self, name, age):
        # このままではスーパークラスの初期化メゾットは実行されない
        self.name = name
        self.age


# サブクラス
class Player(Person):
    def __init__(self, number, position):
        # Personクラスの初期化メゾットをオーバーライドしてしまう
        self.number = number
        self.position = position
