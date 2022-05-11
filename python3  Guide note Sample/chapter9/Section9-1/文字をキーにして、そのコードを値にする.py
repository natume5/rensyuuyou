# 文字をキーにして、そのコードを値にする
unicode = {letter: ord(letter) for letter in "hello"}
# 文字列を1文字ずつに分解して辞書のキーにする
print(unicode)
