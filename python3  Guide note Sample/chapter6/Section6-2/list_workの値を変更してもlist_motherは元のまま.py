# list_workの値を変更してもlist_motherは元のまま
list_mother = [10, 20, 30, 40, 50]
list_work = list_mother.copy()     # リストを複製する
list_work[0] = 99
print(list_work)
print(list_mother)
