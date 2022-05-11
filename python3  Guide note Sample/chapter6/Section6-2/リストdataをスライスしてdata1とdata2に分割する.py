# リストdataをスライスしてdata1とdata2に分割する
data = [10, 21, 35, 49, 51, 60, 77, 81, 92, 100]
n = 3
data1 = data[:n]     # 最初からn-1まで
data2 = data[n:]     # nから最後まで
print(data1)
print(data2)
