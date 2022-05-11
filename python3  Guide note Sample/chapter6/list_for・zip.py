name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
name2 = ["星奈", "優美", "恵子", "薫花", "幸恵"]
longname = []
for n1, n2 in zip(name1, name2):
    longname.append(n1 + n2)
print(longname)
