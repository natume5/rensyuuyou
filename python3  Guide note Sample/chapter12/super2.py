class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Player(Person):
    def __init__(self, name, age, number, posision):
        super().__init__(name, age)
        self.number = number
        self.posision = posision
