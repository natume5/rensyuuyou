# スライスを利用してリストlist_motherを複製する
list_mother = [10, 20, 30, 40, 50]
list_work = list_mother[:]     # リストを複製
print(list_work)
print(list_work is list_mother)
