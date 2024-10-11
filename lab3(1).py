
#Лабораторная работа 3, задание 1 уровня, номер 12 

import random
Mol = [random.randint(-(10**10), 10**10) for _ in range(8)]
print(Mol)

kol = list(filter(lambda x: x < 0, Mol))
long = len(kol)
d = long - 1
print(kol[d::])
