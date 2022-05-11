"""HorseクラスとRiderクラスを定義する。コンポジションを使って、
馬(Horse)に騎手(Rider)を持たせる。
2018年12月23日　有馬記念　中山競馬場
1着=ブラストワンピース　牡3　騎手(池添謙一)
"""


class Horse():
    def __init__(self, name):
        self.name = name


class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

horse = Horse("Blast Onepiece")
rider = Rider("池添　謙一", horse)


print(rider.horse.name)
print(rider.name)
