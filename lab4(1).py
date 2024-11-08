#Лабораторная работа 4, задание 1 уровня, номер 25

matr = [[8, -9, 3, -1, 6], [-6, -45, 7, 2, 21], [56, 83, -25, -89, 54], [90, 37, -15, 32, 72], [-10, -40, 72, 71, -86],
        [3, -8, 75, -14, 9]]
print(matr)

wat = []

for i in matr:
    kol = list(filter(lambda x: x < 0, i))

    v = len(kol)
    wat.append(v)

max_v = max(wat)
min_v = min(wat)

a = wat.index(max_v)
b = wat.index(min_v)
matr[a], matr[b] = matr[b], matr[a]
print(matr)
