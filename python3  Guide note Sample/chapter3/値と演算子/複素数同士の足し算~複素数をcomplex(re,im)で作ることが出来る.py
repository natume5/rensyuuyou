# 1jの2乗が-1になるかどうか確かめる
print(1j * 1j)

# 複素数同士の足し算
a = (1.5 + 3j)
b = (2 + 1j)
print(a + b)

# 複素数同士の掛け算
print((10 + 2j) * (2 + 5j))

# 複素数の実部と虚部を取り出す
v = 3 + 2j
print(v.real)     複素数の実部の値
print(v.imag)     複素数の虚部の値

# 複素数をcomplex(re,im)で作ることが出来る
v = complex(3, 2)
print(v)
