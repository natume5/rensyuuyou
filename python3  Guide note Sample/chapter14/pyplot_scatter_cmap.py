import matplotlib.pyplot as plt
import numpy as np
X, Y = np.random.rand(100), np.random.rand(100)
V = np.random.rand(100)
plt.scatter(X, Y, s=200, c=V, cmap="Blues", edgecolors="b")
plt.colorbar()
plt.grid(True)
plt.show()
