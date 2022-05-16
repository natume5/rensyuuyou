def power_gene():
    num = 1
    while True:
        yield num ** num
        num += 1
pg = power_gene()
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))
print(next(pg))
    
        








