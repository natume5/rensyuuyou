import csv

movies = [["トップガン", "卒業白書", "マイノリティリポート"],
          ["タイタニック", "レヴェナント", "インセプション"],
          ["トレーニングデイ", "マイ・ボディガード", "フライト"]]
with open("movies.csv", "w") as csvfile:
    w = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        w.writerow(movie_list)
