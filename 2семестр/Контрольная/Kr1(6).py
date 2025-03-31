#контрольная к ближайших

from sklearn.datasets import load_breast_cancer #импорт библиотеки с данными об раке молочных желёз
from sklearn.neighbors import KNeighborsClassifier #импорт метода ближайших соседей
from sklearn.model_selection import train_test_split #разделение данных для обучения и для теста
from sklearn.model_selection import GridSearchCV
import numpy as np
import matplotlib.pyplot as plt

data = load_breast_cancer()

print(data.feature_names)
print(data.target_names)

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

plt.show(x_tes, y_test)
