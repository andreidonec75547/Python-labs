import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

file = open('dann.txt', 'w')

file.write('28 42 45 52 56 68 70 75 90 \n')
file.write('3.1 3.8 3.9 4.4 4.5 5.9 5.6 6.4 7.3')

file.close()

are1 = []
pon = open('dann.txt', 'r')

lol = (pon.read())
word_l = lol.split("\n")
lon = word_l[0].split()

for word in lon:
    are1.append(int(word))

pon.close()

pric1 = []
pon = open('dann.txt', 'r')

lol = (pon.read())
word_l = lol.split("\n")
lon = word_l[1].split()

for word in lon:
    pric1.append(float(word))

pon.close()

area = np.array(are1).reshape(-1, 1)
price = np.array(pric1).reshape(-1, 1)

model = LinearRegression()
model.fit(area, price)

plt.scatter(area, price)
plt.plot(np.linspace(15, 100, 100).reshape(-1, 1), model.predict(np.linspace(15, 100, 100).reshape(-1, 1)), 'r')
plt.ylim(2, 10)
plt.show()
