# KeyErrorを例外処理で回避する
city = input("調べる地域名:")    # 辞書から取り出すキーを入力する
members = {"東京": 21, "大阪": 16, "福岡": 11}
# 例外処理に組み込む
try:
    value = members[city]
    print(f"{city}の値は{value}です。")
except KeyError:
    print(f"{city}のデータはありません。")
except Exception as error:
    print(error)
