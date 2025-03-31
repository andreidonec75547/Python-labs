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

clf = KNeighborsClassifier(n_neighbors=13)
clf.fit(x_train, y_train)

print(clf.score(x_test, y_test)) #выводит текушую точность модели
