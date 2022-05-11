# 共通している要素があるかないかを確かめる
a = {"earth", "wind", "fire"}
b = {"sky", "sea"}
c = {"fire", "warter"}
print(a.isdisjoint(b))     # aとbには共通要素がない
print(a.isdisjoint(c))     # aとbにはどちらも"fire"がある
