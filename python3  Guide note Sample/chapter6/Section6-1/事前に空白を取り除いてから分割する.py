# 事前に空白を取り除いてから分割する
colors = "red,blue, green, white, black"
colors = colors.replace(" ", "")    # (事前に)空白を取り除く
color_list = colors.split(",")      # カンマで分割する
print(color_list)
