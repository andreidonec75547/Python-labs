#контрольная к ближайших

from sklearn.datasets import load_breast_cancer #импорт библиотеки с данными об раке молочных желёз
from sklearn.neighbors import KNeighborsClassifier #импорт метода ближайших соседей
from sklearn.model_selection import train_test_split #разделение данных для обучения и для теста
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt

data = load_breast_cancer()

x_train, x_test, y_train, y_test = train_test_split(np.array(data.data),np.array(data.target), test_size=0.2)

x_tr = []

for i in x_train:
    l = []
    l.append(i[0])
    l.append(i[1])
    x_tr.append(l)

x_tes = []

for i in x_test:
    l = []
    l.append(i[0])
    l.append(i[1])
    x_tes.append(l)

clf = KNeighborsClassifier(n_neighbors=13)
clf.fit(x_tr, y_train)

print(clf.score(x_tes, y_test)) #выводит текушую точность модели

xt = np.float64(x_tes)

xtest = []
ytest = []

for i in xt:
    xtest.append(i[0])
    ytest.append(i[1])

x_test0 = np.float64(xtest)
y_test0 = np.float64(ytest)

xtr = np.float64(x_tr)

xtrain = []
ytrain = []

for i in xtr:
    xtrain.append(i[0])
    ytrain.append(i[1])

x_train0 = np.float64(xtrain)
y_train0 = np.float64(ytrain)

plt.scatter(x_test0, y_test0)
plt.scatter(x_train0, y_train0, marker="X")
plt.show()
