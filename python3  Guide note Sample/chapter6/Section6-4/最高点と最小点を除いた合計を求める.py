# 最高点と最小点を除いた合計を求める
judge = [8.7, 8.8, 9.0, 9.1, 8.5]
result = sum(judge) - max(judge) - min(judge)
print(result)    # sum(judge)→合計,max(judge)→最高点,min(judge)→最小点
