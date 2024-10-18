
# Контрольная работа 1, Лабораторная работа 3, задание 3 уровня, номер 8
#Упорядочить по убыванию отрицательные элементы массива, сохраняя остальные элементы на прежних местах.

import random
Mol = [random.randint(-(10**10), 10**10) for _ in range(8)]
print(Mol)

kol = list(filter(lambda x: x < 0, Mol))
kol.sort(reverse=True)
print(kol)

def get_ihd(lon, ran):
    indexin = []
    for index, element in enumerate(lon):
        if element in ran:
            indexin.append(index)
    return indexin

result = get_ihd(Mol, kol)
print(result)

doom = 0
for n in result:
    Mol[n] = kol[doom]
    doom = doom + 1

print(Mol)



# Контрольная работа 1, Лабораторная работа 3, задание 1 уровня, номер 6

Vector = [1, 2, 3, 4, 5]
Vector2 = []
sumin = 0

for x in Vector:
    Vector2.append(x**2)

for num in Vector2:
    sumin += num
print(sumin ** 0.5)
