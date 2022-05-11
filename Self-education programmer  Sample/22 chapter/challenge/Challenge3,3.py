def bubble_sort(lst):
    n = len(lst)
    for i in reversed(range(n)):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


lst = [3333, 5123, 9981, 1243, 7412]
bubble_sort(lst)
print(lst)
# [1243, 3333, 5123, 7412, 9981]
