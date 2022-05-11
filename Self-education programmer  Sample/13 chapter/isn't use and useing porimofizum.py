# このコードは例なので実行できない
# ポリモーフィズムなしで様々な形状を描画する場合
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if isinstance(a_shape, Triangle):
        a_shape.draw_triangle()
    if isinstance(a_shape, Square):
        a_shape.draw_square()
    if isinstance(a_shape, Circle):
        a_shape.draw_circle()

# ポリモーフィズムを実装して描画する場合
shapes = [tr1, sw1, cr1]
for a_shape in shapes:
    a_shape.draw()
