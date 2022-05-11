import matplotlib.pyplot as plt
import math
X = range(0, 360)
Y = [math.sin(math.radians(d)) for d in X]
plt.plot(X, Y)
plt.show()
