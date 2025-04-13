#метод K ближайших соседей для K = 3

#неизвестная точка
x_1 = 178
y_1 = 56

#толстый человек
x_r1 = [150, 152, 157, 151, 159, 162, 154, 155, 153, 164]
y_r1 = [100, 85, 92, 99, 81, 88, 82, 94, 91, 90]

#худой человек
x_r2 = [177, 189, 180, 176, 183, 188, 175, 181, 190, 186]
y_r2 = [59, 53, 51, 58, 60, 52, 55, 50, 57, 54]

#создаём общий масив х рост человека
x = []

for i in x_r1:
    x.append(i)

for i in x_r2:
    x.append(i)

#создаём общий масив у вес человека
y = []

for i in y_r1:
    y.append(i)

for i in y_r2:
    y.append(i)

#создаём вложаный масив с координатами х и у
l = len(x) - 1

i = -1

xy = []

while i < l:
    i += 1
    g = []
    g.append(x[i])
    g.append(y[i])
    xy.append(g)

#создаём классы к точкам
classy = []

nol = -1

while nol < l:
    nol += 1
    h = 0
    classy.append(h)

one = -1

while one < l:
    one += 1
    n = 1
    classy.append(n)

#ищем длину списков
len_x = len(x) - 1
len_y = len(y) - 1

#проверяем равны ли эти списки
if len_y != len_x:
    print("Допушена ошибка в одном из масиве х или у")

#создаём масив с индексами списка
kf = []
if len(kf) != len_x:
    for i in range(0, len(x)):
        kf.append(i)

# #переводим см в метры
# nx = []
# for i in x:
#     g = i / 100
#     nx.append(g)
#
# #создаём масив с кофициентом жирности, отношение веса и роста
# en = []
# for i in kf:
#     lot = y[i] / (nx[i]**2)
#     en.append(round(lot, 2))
#
# #ищим ваш коофициент жирности
# jol = y_1 / ((x_1 / 100)**2)
# kf_you = round(jol, 2)

#через цикл перебирается значения по х насколько эта точка удалена от остальных по х
n = []

for i in x:
    l = i - x_1
    n.append(l)

#сортируем масив
k = sorted(n)

#закидываем в масив только отрецательные элементы
b = []

for i in k:
    if i < 0:
     b.append(i)

#все элементы делаем положительными
s = []

for i in b:
    g = i * -1
    s.append(g)

#находим минимальный элемент
min_1 = min(s)

#убераем уже найденый минимальный элемет из масива
s_2 = []

for i in s:
    if i > min_1:
        s_2.append(i)

#находим ещё один минимальный элемент из масива толстых
min_1_1 = min(s_2)

#закидываем в масив только положительные элементы
d = []

for i in k:
    if i > 0:
        d.append(i)

#находим минимальный элемент из положительных
min_2 = min(d)

bl_t_x = []

#смотрим растояние по x
if min_2 <= min_1:
    if min_2 < min_1_1:
        for i in k:
            if min_2 == i:
                tchk3 = x_1 + min_2

        index3 = -1
        for i in xy:
            index3 += 1
            rs3 = i[0]
            if tchk3 == rs3:
                pol_tchk3 = xy[index3]
                bl_t_x.append(pol_tchk3)
    else:
        tochka1_1 = min_1_1 * (-1)

        for i in k:
            if tochka1_1 == i:
                tchk2 = x_1 + tochka1_1

        index2 = -1
        for i in xy:
            index2 += 1
            rs2 = i[0]
            if tchk2 == rs2:
                pol_tchk2 = xy[index2]
                bl_t_x.append(pol_tchk2)
else:
    tochka1 = min_1 * (-1)

    for i in k:
        if tochka1 == i:
            tchk1 = x_1 + tochka1

    index1 = -1
    for i in xy:
        index1 += 1
        rs1 = i[0]
        if tchk1 == rs1:
            pol_tchk1 = xy[index1]
            bl_t_x.append(pol_tchk1)

print(bl_t_x)

#строим график для наглядности и проверки
# import matplotlib.pyplot as plt
# plt.scatter(x, y)
# plt.scatter(x_1, y_1)
# plt.show()
