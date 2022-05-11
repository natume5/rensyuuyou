# 大文字小文字を区別せずにソートする
words = ["peach", "ver3", "Python", "Pokemon", "ver2"]
new_words = sorted(words, key=str.lower)    # 小文字で比較してソート
print(new_words)
