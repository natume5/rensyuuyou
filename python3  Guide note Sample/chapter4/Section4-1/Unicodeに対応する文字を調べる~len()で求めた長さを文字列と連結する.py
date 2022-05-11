# Unicodeに対応する文字を調べる
print(ord("a"))

print(chr(97))

print(ord("海"))

print(chr(28023))

# 文字数を調べる
print(len("Python"))

print(len("パイソン"))

# len()で求めた長さを文字列と連結する
kosu = len("Python")
ans = "文字数は" + str(kosu) + "個"
print(ans)
