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

#выводит какое значениие k лучше

# param_grid = {'n_neighbors': np.arange(1, 50)}
# knn_cv = GridSearchCV(clf, param_grid, cv=5)
# knn_cv.fit(x_train, y_train)
# print(knn_cv.best_params_)
# print(knn_cv.best_score_)

#Выведение графика насколько точно будет модель при увеличение k

# neighbors = np.arange(1, 25)
# accuracy = np.empty(len(neighbors))
#
# for i, k in enumerate(neighbors):
#     knn = KNeighborsClassifier(n_neighbors=k)
#     knn.fit(x_train, y_train)
#     accuracy[i] = knn.score(x_test, y_test)
#
# plt.title('Точность K-NN по количеству соседей')
# plt.plot(neighbors, accuracy)
# plt.xlabel('Количчество соседей')
# plt.ylabel('Точность')
# plt.show()

print(x_test[0])
# x: List[List[float, float]]   [[x0,y0], [x1,y1], ...]
# y: List[Literal[0,1]]   [0,0,1,0, ...]

# plt.plot(x_test, y_test, 'ro')
# plt.show()

