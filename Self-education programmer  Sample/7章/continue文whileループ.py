i = 1
while i <= 5:
    if i == 3:
        i += 1   # i=i+1と同じ　↑↑iが5以下である　↑iが3と等しい
        continue
    print(i)
    i += 1
