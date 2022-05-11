# 底辺と高さから三角形の面積を求める
# 三角形の面積
def triangle(base, height):
    area = base * height / 2    # triangle()関数定義
    return area


# 関数を渡す
b = 15     # 底辺
h = 13     # 高さ
v = triangle(b, h)    # 三角形の面積を求める
# 2つの引数の値をカンマで区切って与える
print(f"底辺{b}, 高さ{h}の三角形の面積は{v :.1f}です。")
