# 2番目のリストの3個目の要素を書き替える
r101 = "佐藤"
r102 = "田中"
r103 = "鈴木"
r201 = "青木"
r202 = "広田"
r203 = "野村"
floor1 = [r101, r102, r103]
floor2 = [r201, r202, r203]
apartment = [floor1, floor2]
apartment[1][2] = "マイケル"
print(apartment[1])
