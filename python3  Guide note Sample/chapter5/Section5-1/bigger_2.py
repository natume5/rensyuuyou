# if~elseを1行で書く
from random import randint
a = randint(0, 100)
b = randint(0, 100)
# 大きな方の値を代入する
bigger = a if a > b else b
# 結果
text = f"{a}と{b}では、{bigger}が大きい"
print(text)
