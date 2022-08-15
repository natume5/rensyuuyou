import random

class Dice:
    def __init__(self, number=1):
        self.number = number

    @property
    def number(self):
        return self.__number

    def roll(self):
        self.number = random.randint(1, 6)

    @number.setter
    def number(self, value):
        if isinstance(value, int) and 1 <= value <= 6:
            self.__number = value
        else:
            raise ValueError('数値は1～6の整数で設定して下さい。')

