#Лабораторная работа 2, работа 2, номер 6
# x = [270, 327, 402, 477, 627, 777, 927, 1077, 1227, 1527, 1827]
# y = [10, 7.5, 6, 5.1, 3.5, 3.1, 5, 8, 10, 2.5, 2]

file = open('x.txt', 'w')

file.write('270 327 402 477 627 777 927 1077 1227 1527 1827')

file.close()

file = open('y.txt', 'w')

file.write('10 7.5 6 5.1 3.5 3.1 5 8 10 2.5 2')

file.close()

x = []
pon = open('x.txt', 'r')

lol = (pon.read())
word_l = lol.split()

for word in word_l:
    x.append(int(word))

pon.close()

y = []
pon = open('y.txt', 'r')

lol = (pon.read())
word_l = lol.split()

for word in word_l:
    y.append(float(word))

pon.close()

import matplotlib.pyplot as plt
plt.plot(x, y, marker='X')
plt.show()
