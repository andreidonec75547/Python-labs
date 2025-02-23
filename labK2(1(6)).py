#Лаборвторная работа 2, номер 1, задча 6
#f(x)=a*ln(x)+b

a = int(input("Введите число a:"))
b = int(input("Введите число b:"))

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
y = []

for l in x:
    import math
    f = a * math.log(l) + b
    y.append(f)

plt.plot(x, y, marker='X')
plt.show()
