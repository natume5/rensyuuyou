def power_gene():
    num = 1
    while True:
        yield num ** num
        num += 1
# 無限ループジェネレーターはループに入れると止まらなくなるのでbreakを書く必要がある
for res in power_gene():
    print(res)
    if res >= 100000:
        break

    
        








