import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

area = np.array([28, 42, 45, 52, 56, 68, 70, 75, 90]).reshape(-1, 1)
price = np.array([3.1, 3.8, 3.9, 4.4, 4.5, 5.9, 5.6, 6.4, 7.3]).reshape(-1, 1)

model = LinearRegression()
model.fit(area, price)

plt.scatter(area, price)
plt.plot(np.linspace(15, 100, 100).reshape(-1, 1), model.predict(np.linspace(15, 100, 100).reshape(-1, 1)), 'r')
plt.ylim(2, 10)
plt.show()
