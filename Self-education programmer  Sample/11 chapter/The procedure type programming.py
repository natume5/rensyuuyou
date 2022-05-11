# グローバル変数を関数から直接書き換えるコード例
pop = []
jpop = []


def collect_songs():
    song = "曲名を入力して下さい:"
    ask = "pかjのどちらかを入力して下さい。qで終わります: "

    while True:
        genre = input(ask)
        if genre == "q":
            break

        if genre == "p":
            p = input(song)
            pop.append(p)

        elif genre == "j":
            j = input(song)
            jpop.appendd(j)

        else:
            print("不正な値です。")
    print("pop songs: ", pop)
    print("jpop songs: ", jpop)


collect_songs()
