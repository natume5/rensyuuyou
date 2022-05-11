# 文字列に引数の値を埋め込む
s = "チューリップは{}と{}と{}でした。"
print(s.format("赤", "青", "黄色"))

# 埋め込む値に数値がある場合
name = "高橋"
age = 23
point = 102.5
s = "{}選手、年齢{}、得点{}でした。"
text = s.format(name, age, point)
print(text)

# f"{値}"の書式で文字列に値を埋め込む
name = "高橋"
age = 23
point= 102.5
text = f"{name}選手、年齢{age}、得点{point}でした。"
print(text)

# 対応する引数を番号で指定する
name = "高橋"
age = 23
point= 102.5
s ="得点{2}、{0}、{1}歳"
text = s.format(name, age, point)
print(text)

# 埋め込む引数をキーワード引数で指定する
s = "{name}選手、年齢{age}、得点{point}でした。"
text = s.format(name="高橋", age=23, point=102.5)
print(text)
