def power_gene():
    for num in  range(1, 4):
        print("{0}の{0}乗".format(num))
        yield num ** num
    # 返された値を出力しないパターン
for res in power_gene():
    pass
print("-" * 10)
# 返された値を出力するパターン
for res in power_gene():
    print(res)
        








