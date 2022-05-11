# 10文字フィールドに右詰で表示する
num1 = 123.4
num2 = 56.9
num3 = 3040.1
print(f"{num1:>10.1f}")
print(f"{num2:>10.1f}")
print(f"{num3:>10.1f}")

# %形式の文字列フォーマット
print("%s %s%s" % ('Hello', "Python", 3.6, ))
print("計算%s%s%f" % ('10/4', "は", 10/4, ))
