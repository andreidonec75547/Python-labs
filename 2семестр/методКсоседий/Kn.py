#метод K ближайших соседей для K = бесконечности нечётных чисел
import numpy as np
from sklearn.model_selection import train_test_split

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

#делим данные на обучение и тестовые
x_train, x_test, y_train, y_test = train_test_split(np.array(xy),np.array(xy), test_size=0.2)

rs = []

for test in x_test:
    for train in x_train:
        rsx = train[0] - test[0]
        rsy = train[1] - test[1]
        if rsx < 0:
            rsx *= -1
            
