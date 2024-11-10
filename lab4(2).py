#Лабораторная работа 4, задание 2 уровня, номер 1

matr = [[1, 4, 9, 2, 65, 39, 6], [76, 21, 84, 5, 7, 24, 8], [8, 3, 23, 12, 53, 41, 41], [49, 85, 17, 32, 75, 61, 53], [79, 49, 72, 62, 44, 82, 35]]

matr_end = []

for i in matr:
    kol = list(filter(lambda x: x > 0, i))

    max_v = max(kol)

    a = kol.index(max_v)

    mi = (a - 1)
    ma = a + 1

    ln = kol[ma]

    gn = kol[mi]

    if ln > gn:
        gn *= 2
    else:
        ln *= 2

    kol[ma] = ln
    kol[mi] = gn

    matr_end.append(kol)

print(matr)
print(matr_end)
