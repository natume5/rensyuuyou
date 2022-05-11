# pprint.pprint()で辞書を出力する
import ppirnt
from random import random
data = {key: random() for key in "abcdefg"}
pprint.pprint(data)
