# randomモジュールからrandint()を読み込んで使う
from random import randint
print(randint(1, 6))
print(randint(1, 6))
print(randint(1, 6))

# randomモジュールからrandom()を読み込んで使う
from random import random
print(random())

# randint()をdiceの名前で読み込む
from random import randint as dice
print(dice(1, 6))
