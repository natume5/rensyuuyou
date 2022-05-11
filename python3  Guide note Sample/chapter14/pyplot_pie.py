import matplotlib.pyplot as plt
labels = ["E", "D", "C", "B", "A"]
V = [17, 25, 47, 68, 91]
ex = [0, 0, 0.1, 0, 0]
plt.pie(V, explode=ex, labels=labels, autopct='%1.1f%%', startangle=90)
plt.show()
