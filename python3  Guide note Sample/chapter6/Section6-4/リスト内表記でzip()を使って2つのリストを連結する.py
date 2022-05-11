# リスト内表記でzip()を使って2つのリストを連結する
name1 = ["鈴木", "田中", "赤尾", "佐々木", "高田"]
name2 = ["星奈", "優美", "恵子", "薫花", "幸恵"]
longname = [n1 + n2 for n1, n2 in zip(name1, name2)]
print(longname)    # n1にはname1の要素、n2にはname2の要素が入る
