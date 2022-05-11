import matplotlib.pyplot as plt
price = [200, 300, 400, 500, 600]
count = [31, 29, 25, 28, 26]
plt.plot(price, count, marker="o")
plt.title("count - price")
plt.xlabel("price")
plt.ylabel("count")
plt.grid(True)
plt.show()
