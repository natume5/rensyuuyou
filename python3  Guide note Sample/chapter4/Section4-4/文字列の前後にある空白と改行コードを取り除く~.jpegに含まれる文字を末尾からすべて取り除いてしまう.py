# 文字列の前後にある空白と改行コードを取り除く
t = "__hello_\n"
print(t.strip())

# 末尾にある連続した"."を取り除く
t = "abc....."
print(t.rstrip("."))

# 末尾にあるカンマ、ピリオド、改行コードを取り除く
t1 = "2, 3, 4,"
print(t1.rstrip(".,\n"))
t2 = "Hello World.\n"
print(t2.rstrip(".,\n"))

# ".jpeg"に含まれる文字を末尾からすべて取り除いてしまう
t = "dog.peg.jp"
print(t.rstrip(".jpeg"))
