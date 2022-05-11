city = input("調べる地区名")
members = {"東京": 21, "大阪": 16, "福岡": 11}
try:
    value = members[city]
    print(f"{city}の値は{value}です")
except KeyError:
    print(f"{city}のデータはありません。")
except Exception as error:
    print(error)
