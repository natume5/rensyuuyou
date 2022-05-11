qs = ["What is your name?",
      "What is your fav. color?",
      "What is our quest?"]
n = 0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n + 1) % 3
