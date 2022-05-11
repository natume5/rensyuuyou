data = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
result = []
for alist in data:
    for num in alist:
        result.append(num * 2)
print(result)
