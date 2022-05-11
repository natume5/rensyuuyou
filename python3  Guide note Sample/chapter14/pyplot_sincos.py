import matplotlib.pyplot as plt
import math
X = range(0, 360)
S = [math.sin(math.radians(d)) for d in X]
C = [math.cos(math.radians(d)) for d in X]
plt.plot(X, S)
plt.plot(X, C)
plt.show()
