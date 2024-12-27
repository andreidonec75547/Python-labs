#Лабораторная работа 5, задание 3 уровня, номер 2
#В заданной матрице расположить элементы четных строк в порядке возрастания, а элементы нечетных строк в порядке убывания. Обработку матрицы по строкам осуществлять в методе. Для упорядочения строки использовать делегат.

matr = [[1, 2, 3, 4], [5, 2, 8, 9], [6, 3, 12, 1]]

def sort_by(a_list, selector, ton):
    return sorted(a_list, key=selector, reverse=ton)

m = []

for i in matr[1::2]:
    for ch in i:
        m.append(ch)

n = sort_by(m, None, False)

matr[1:2] = [n]

s = []

for a in matr[::2]:
    s.append(sort_by(a, None, True))

matr[0] = s[0]
matr[2] = s[1]

print(matr)
