me = {
    "height": "6",
    "fav_color": "blue",
    "fav_musican": ["Jonus blue", "DJ Tiesto", "Armin van Buuren"]
}

answer = input("Type height, fav_color or fav_musican")
if answer in me:
    result = me[answer]
    print(result)
