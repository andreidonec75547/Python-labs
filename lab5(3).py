#Лабораторная работа 5, задание 3 уровня, номер 2
#В заданной матрице расположить элементы четных строк в порядке возрастания, а элементы нечетных строк в порядке убывания. Обработку матрицы по строкам осуществлять в методе. Для упорядочения строки использовать делегат.

matr = [[1, 2, 3, 4], [5, 2, 8, 9], [6, 3, 12, 1]]

for i in matr[1::2]:
    i.sort()

for a in matr[::2]:
    a.sort(reverse=True)

print(matr)