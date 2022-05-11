# 3つのリストを1つにまとめる
x = [1, 2, 3]
y = [4, 5, 6]
z = [7, 8, 9]
zip_obj = zip(x, y, z)     # zipオブジェクトにする
xyx = list(zip_obj)       # リストに変換
print(xyx)
