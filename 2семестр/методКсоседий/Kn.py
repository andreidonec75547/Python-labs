# метод K ближайших соседей для K = бесконечности нечётных чисел
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

# толстый человек
x_r1 = [150, 152, 157, 151, 159, 162, 154, 155, 153, 164]
y_r1 = [100, 85, 92, 99, 81, 88, 82, 94, 91, 90]

# худой человек
x_r2 = [177, 189, 180, 176, 183, 188, 175, 181, 190, 186]
y_r2 = [59, 53, 51, 58, 60, 52, 55, 50, 57, 54]

# создаём общий масив х рост человека
x = []

for i in x_r1:
    x.append(i)

for i in x_r2:
    x.append(i)

# создаём общий масив у вес человека
y = []

for i in y_r1:
    y.append(i)

for i in y_r2:
    y.append(i)

# создаём вложаный масив с координатами х и у
l = len(x) - 1

i = -1

xy = []

while i < l:
    i += 1
    g = []
    g.append(x[i])
    g.append(y[i])
    xy.append(g)

# создаём классы к точкам
classy = []

l1 = len(x_r1) - 1

nol = -1

while nol < l1:
    nol += 1
    h = 0
    classy.append(h)

one = -1

while one < l1:
    one += 1
    n = 1
    classy.append(n)

# ищем длину списков
len_x = len(x) - 1
len_y = len(y) - 1

# проверяем равны ли эти списки
if len_y != len_x:
    print("Допушена ошибка в одном из масиве х или у")

# создаём масив с индексами списка
kf = []
if len(kf) != len_x:
    for i in range(0, len(x)):
        kf.append(i)

# делим данные на обучение и тестовые
xy_train, xy_test = train_test_split(np.array(xy), test_size=0.3)

# ищем растояние между точками
for test in xy_test:
    dlin = []
    for train in xy_train:
        rsx = train[0] - test[0]
        rsy = train[1] - test[1]
        dl = []
        if rsx < 0:
            rsx *= -1
            dl.append(rsx)
        else:
            dl.append(rsx)
        if rsy < 0:
            rsy *= -1
            dl.append(rsy)
        else:
            dl.append(rsy)
        kr = (((dl[0]) ** 2) + ((dl[1]) ** 2)) ** (0.5)
        dlin.append(round(kr))

    # ищем минимальную длину
    min_tchk1 = min(dlin)
    dlin1 =[]
    for i in dlin:
        if i > min_tchk1:
            dlin1.append(i)

    min_tchk2 = min(dlin1)
    dlin2 = []
    for i2 in dlin1:
        if i2 > min_tchk2:
            dlin2.append(i2)

    min_tchk3 = min(dlin2)

    # с начала проверяем найденые минимальные растояния на самое близкое, если два растояния равны то берётся третье растояние и проверяется
    # находимм индекс данной точки, после получаем её класс и на основе класа делаем ещё одну проверку
    # если класс относится к 0 то выводим круглую зелённую точку, если нет то выводим зелённый крестик
    if min_tchk1 <= min_tchk2:
        if min_tchk1 < min_tchk3:
            ind_dl = dlin.index(min_tchk1)
            tchk1 = xy_train[ind_dl]
            ind1 = x.index(tchk1[0])
            clas1 = classy[ind1]
            if clas1 == 0:
                plt.scatter(test[0], test[1], color='green')
            else:
                plt.scatter(test[0], test[1], color='green', marker='X')
        else:
            ind_dl3 = dlin.index(min_tchk3)
            tchk3 = xy_train[ind_dl3]
            ind3 = x.index(tchk3[0])
            clas3 = classy[ind3]
            if clas3 > 0:
                plt.scatter(test[0], test[1], color='green')
            else:
                plt.scatter(test[0], test[1], color='green', marker='X')
    else:
        ind_dl2 = dlin.index(min_tchk2)
        tchk2 = xy_train[ind_dl2]
        ind2 = x.index(tchk2[0])
        clas2 = classy[ind2]
        if clas2 > 0:
            plt.scatter(test[0], test[1], color='green')
        else:
            plt.scatter(test[0], test[1], color='green', marker='X')
            
# здесь выводим точки принадлежашие к обучаюшим точкам модели с проверкой на класс
for train in xy_train:
    ind_tr = x.index(train[0])
    clas_tr = classy[ind_tr]
    if clas_tr == 0:
        plt.scatter(train[0], train[1], color='blue')
    else:
        plt.scatter(train[0], train[1], color='blue', marker='X')
plt.show()
