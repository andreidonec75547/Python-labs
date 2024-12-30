#Лабораторная работа 5 уровня 2 номер 2
#В массивах A размером 9 и B размером 7 заменить максимальные элементы на среднее арифметическое значение элементов, расположенных после максимального, в том массиве, для которого максимальный элемент расположен дальше от конца массива. Поиск максимального элемента осуществить в методе.

import random
a = [random.randint(0, 10**10) for _ in range(9)]
print('Первый масив A размером 9', a)

import random
b = [random.randint(0, 10**10) for _ in range(7)]
print('Второй масив B размером 7', b)

tot = 0

def max_list(list):
    max = list[0]
    for a in list:
        if a > max:
            max = a
    return max

max1 = max_list(a)
print('Максимальный элемент первого масива', max1)
max2 = max_list(b)
print('Максимальный элемент второго масива', max2)

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
    end1 = tot / kn1
    a[ind1] = round(end1)
    print('Ответ: первый масив изменён', a)
else:
    n = b[index_2::]
    for ni in n:
        tot += ni
    end2 = tot / kn2
    b[ind2] = round(end2)
    print('Ответ: второй масив изменён', b)
