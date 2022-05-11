answer = input("あなたの好きな色は何色？")
with open("fav_color.txt", "w") as f:
    f.write(answer)
