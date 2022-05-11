import matplotlib.pyplot as plt
X1, Y1 = range(0, 5), ["61", "45", "27", "88", "47"]
X2, Y2 = range(0, 5), ["17", "39", "46", "40", "27"]
labels = ["A", "B", "C", "D", "E"]

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, sharey=True)
ax1.bar(X1, Y1, color="b", tick_label=labels)
ax1.set_title("dog")
ax2.bar(X2, Y2, color="g", tick_label=labels)
ax2.set_title("cat")
fig.show()
