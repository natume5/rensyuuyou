import csv

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Tianic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]
with open("movies.csv", "w") as csvfile:
    w = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        w.writerow(movie_list)
