# 正の値だけを合算する
numbers = [2, 6, -3, 5, -1, 7]
sum = 0
# numbersの静の値だけを合算する
for num in numbers:      # numbersから順に数値をnumに取り出す
    if num > 0:
        sum += num     # numbersから順に取り出した値が市の時にsumに加算
print(sum)
