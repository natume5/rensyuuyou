# 2つのリストの要素同士を連結した新しいリストを作る
name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
name2 = ["星奈", "優美", "恵子", "薫花", "幸恵"]
longname = []
# name1とname2を連結したリストを作る
for n1, n2 in zip(name1, name2):
    longname.append(n1 + n2)
print(longname)
