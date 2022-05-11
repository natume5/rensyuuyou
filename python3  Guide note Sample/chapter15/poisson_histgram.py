import numpy as np
import matplotlib.pyplot as plt

data = np.random.poisson(lam=50, size=1000)
count, bins_edges, patches = plt.hist(data, bins=100)
plt.grid()
plt.show()
