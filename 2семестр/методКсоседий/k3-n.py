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

#через цикл перебирается значения по y насколько эта точка удалена от остальных по y
ny = []

for i in y:
    ly = i - y_1
    ny.append(ly)

#сортируем масив
ky = sorted(ny)

#закидываем в масив только отрецательные элементы
by = []

for i in ky:
    if i < 0:
     by.append(i)

#все элементы делаем положительными
sy = []

for i in by:
    gy = i * -1
    sy.append(gy)

#находим минимальный элемент
min_1y = min(sy)

#убераем уже найденый минимальный элемет из масива
sy_2 = []

for i in sy:
    if i > min_1y:
        sy_2.append(i)

#находим ещё один минимальный элемент из масива y
min_1_1y = min(sy_2)

#закидываем в масив только положительные элементы
dy = []

for i in ky:
    if i > 0:
        dy.append(i)

#находим минимальный элемент из положительных
min_2y = min(dy)

bl_t_y = []

#смотрим растояние по y
if min_2y <= min_1y:
    if min_2y < min_1_1y:
        for i in ky:
            if min_2y == i:
                tchk3y = y_1 + min_2y

        index3y = -1
        for i in xy:
            index3y += 1
            rs3y = i[1]
            if tchk3y == rs3y:
                pol_tchk3y = xy[index3y]
                bl_t_y.append(pol_tchk3y)
    else:
        tochka1_1y = min_1_1y * (-1)

        for i in ky:
            if tochka1_1y == i:
                tchk2y = y_1 + tochka1_1y

        index2y = -1
        for i in xy:
            index2y += 1
            rs2y = i[0]
            if tchk2y == rs2y:
                pol_tchk2y = xy[index2y]
                bl_t_y.append(pol_tchk2y)
else:
    tochka1y = min_1y * (-1)

    for i in ky:
        if tochka1y == i:
            tchk1y = y_1 + tochka1y

    index1y = -1
    for i in xy:
        index1y += 1
        rs1y = i[0]
        if tchk1y == rs1y:
            pol_tchk1y = xy[index1y]
            bl_t_y.append(pol_tchk1y)

print(bl_t_y)

print(x_1, y_1)
#раскрываем точку 1 по x
x1_1 = []

for i in bl_t_x:
    x1_1.append(i[0])

#убераем найденую точку 1 по x из масива
x1 = []

for xi in x1_1:
    for i in x:
        if i != xi:
            x1.append(i)

#раскрываем точку 1 по y
y1_1 = []

for i in bl_t_x:
    y1_1.append(i[1])

#убераем найденую точку 1 по y из масива
y1 = []

for yi in y1_1:
    for i in y:
        if i != yi:
            y1.append(i)

#раскрываем точку 2 по x
y_x1_1 = []

for i in bl_t_y:
    y_x1_1.append(i[0])

#убераем найденую точку 2 по x из масива
y_x1 = []

for xi in y_x1_1:
    for i in x1:
        if i != xi:
            y_x1.append(i)

#раскрываем точку 1 по y
y_y1_1 = []

for i in bl_t_y:
    y_y1_1.append(i[1])

#убераем найденую точку 1 по y из масива
y_y1 = []

for yi in y_y1_1:
    for i in y1:
        if i != yi:
            y_y1.append(i)

#создаём вложаный масив с координатами х и у без найденых точек
l1 = len(y_x1) - 1

ixy = -1

xy1 = []

while ixy < l1:
    ixy += 1
    g1 = []
    g1.append(y_x1[ixy])
    g1.append(y_y1[ixy])
    xy1.append(g1)

#через цикл перебирается значения по х насколько эта точка удалена от остальных по х
n1 = []

for i in y_x1:
    lo = i - x_1
    n1.append(lo)

#сортируем масив
k1 = sorted(n1)

#закидываем в масив только отрецательные элементы
b1 = []

for i in k1:
    if i < 0:
     b1.append(i)

#все элементы делаем положительными
s1 = []

for i in b1:
    g1 = i * -1
    s1.append(g1)

#находим минимальный элемент
new_min_1 = min(s1)

#убераем уже найденый минимальный элемет из масива
s1_2 = []

for i in s1:
    if i > new_min_1:
        s1_2.append(i)

#находим ещё один минимальный элемент из масива толстых
new_min_1_1 = min(s1_2)

#закидываем в масив только положительные элементы
d1 = []

for i in k1:
    if i > 0:
        d1.append(i)

#находим минимальный элемент из положительных
new_min_2 = min(d1)

bl_t_x1 = []

#смотрим растояние точки 3 по x
if new_min_2 <= new_min_1:
    if new_min_2 < new_min_1_1:
        for i in k1:
            if new_min_2 == i:
                new_tchk3 = x_1 + new_min_2

        new_index3 = -1
        for i in xy1:
            new_index3 += 1
            new_rs3 = i[0]
            if new_tchk3 == new_rs3:
                new_pol_tchk3 = xy1[new_index3]
                bl_t_x1.append(new_pol_tchk3)
    else:
        new_tochka1_1 = new_min_1_1 * (-1)

        for i in k1:
            if new_tochka1_1 == i:
                new_tchk2 = x_1 + new_tochka1_1

        new_index2 = -1
        for i in xy1:
            new_index2 += 1
            new_rs2 = i[0]
            if new_tchk2 == new_rs2:
                new_pol_tchk2 = xy1[new_index2]
                bl_t_x1.append(new_pol_tchk2)
else:
    new_tochka1 = new_min_1 * (-1)

    for i in k1:
        if new_tochka1 == i:
            new_tchk1 = x_1 + new_tochka1

    new_index1 = -1
    for i in xy1:
        new_index1 += 1
        new_rs1 = i[0]
        if new_tchk1 == new_rs1:
            new_pol_tchk1 = xy1[new_index1]
            bl_t_x1.append(new_pol_tchk1)

print(bl_t_x1)

#строим график для наглядности и проверки
# import matplotlib.pyplot as plt
# plt.scatter(x, y)
# plt.scatter(x_1, y_1)
# plt.show()
