#Лабораторная работа 5, задание 2 уровня, номер 2
#В массивах A размером 9 и B размером 7 заменить максимальные элементы на среднее арифметическое значение элементов, расположенных после максимального, в том массиве, для которого максимальный элемент расположен дальше от конца массива. Поиск максимального элемента осуществить в методе.

import random
a = [random.randint(0, 10**10) for _ in range(9)]
print(a)

import random
b = [random.randint(0, 10**10) for _ in range(7)]
print(b)

tot = 0

max1 = max(a)
print(max1)
max2 = max(b)
print(max2)

ind1 = a.index(max1)
index_1 = ind1 + 1
ind2 = b.index(max2)
index_2 = ind2 + 1

long1 = len(a) - 1
long2 = len(b) - 1

kn1 = long1 - ind1
kn2 = long2 - ind2

if kn1 > kn2:
    n = a[index_1::]
    for ni in n:
        tot += ni
    a[ind1] = tot
else:
    n = b[index_2::]
    for ni in n:
        tot += ni
    b[ind2] = tot

print(tot)
print(a)
print(b)
