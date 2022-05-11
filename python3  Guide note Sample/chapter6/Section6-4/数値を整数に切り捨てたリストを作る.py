# 数値を整数に切り捨てたリストを作る
import math
num_List = [5.1, 4.3, 8.2, 6.3, 9.6, 10.2, 2.3]
result = [math.floor(num) for num in num_List]
print(result)
