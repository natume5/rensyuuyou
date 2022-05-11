import numpy as np
sigma = 3.5
mu = 65


data = sigma * np.random.randn(200) + mu
x = float(input("得点は？:"))
t_score = 10 * (x - data.mean()) / data.std() + 50
print("平均点:", round(data.mean(), 1))
print("標準偏差:", round(data.std(), 1))
print("偏差値:", round(t_score, 1))
