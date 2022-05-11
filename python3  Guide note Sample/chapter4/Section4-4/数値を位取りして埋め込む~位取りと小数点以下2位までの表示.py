# 数値を位取りして埋め込む
tokyo = 123456000
kyoto = 53900
s = "東京{:,}、 京都{:,}"
print(s.format(tokyo, kyoto))

# 小数点以下の桁数指定
length = 25.34
thickness = 5.62
text = f"長さ{length:.1f}cm、厚み{thickness:.0f}mm"
print(text)

# 小数点以下の桁数指定
length = 25.34
thickness = 5.62
s = "長さ{:.1f}cm、厚み{:.0f}mm"
print(s.format(length, thickness))

# 位取りと小数点以下2位までの表示
num = 2345.032
print(f"{num:,.2f}")
