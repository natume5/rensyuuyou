import matplotlib.pyplot as plt
X1, Y1 = range(0, 7), [61, 45, 27, 88, 47, 56, 61]
X2, Y2 = range(0, 5), [77, 49, 56, 47, 67]
X3, Y3 = range(0, 4), [56, 41, 67, 76]
labels = ["A", "B", "C", "D", "E", "F", "G"]
fig = plt.figure()

ax1 = fig.add_subplot(2, 1, 1)
ax1.bar(X1, Y1, color="b", tick_label=labels)
ax1.set_title("dog")


ax2 = fig.add_subplot(2, 2, 3)
ax2.bar(X2, Y2, color="g", tick_label=labels[:5])
ax2.set_title("cat")


ax3 = fig.add_subplot(2, 2, 4)
ax3.bar(X3, Y3, color="c", tick_label=labels[:4])
ax3.set_title("bird")
plt.tight_layout()
fig.show()
