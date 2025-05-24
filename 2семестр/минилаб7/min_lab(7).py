import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score


def generate_datasets():
    seed = 30
    n_samples = 500

    datasets_list = [
        datasets.make_circles(n_samples=n_samples, factor=0.5, noise=0.05, random_state=seed),
        datasets.make_moons(n_samples=n_samples, noise=0.05, random_state=seed),
        datasets.make_blobs(n_samples=n_samples, cluster_std=[1.0, 0.5], random_state=seed, centers=2),
        (np.dot(datasets.make_blobs(n_samples=n_samples, random_state=170, centers=2)[0], [[0.6, -0.6], [-0.4, 0.8]]),
            datasets.make_blobs(n_samples=n_samples, random_state=170, centers=2)[1]),
        datasets.make_blobs(n_samples=n_samples, random_state=seed, centers=2)
    ]
    return datasets_list

def create_models():
    return [
        KNeighborsClassifier(n_neighbors=5),
        SVC(kernel='rbf', C=1.0, gamma='scale'),
        MLPClassifier(hidden_layer_sizes=(64, 32), activation='relu', max_iter=1000, random_state=42, early_stopping=True)
    ]

def plot_results_table(models, datasets):
    fig, axes = plt.subplots(nrows=5, ncols=3, figsize=(15, 20))
    fig.suptitle('Сравнение методов классификации на разных данных', y=1.02, fontsize=16)

    dataset_names = [
        "1. Вложенные окружности",
        "2. Полумесяцы",
        "3. Разрозненные кластеры",
        "4. Неодинаковые данные",
        "5. Пересекающиеся облака точек"
    ]

    model_names = [
        "Метод k-ближайших соседей (KNN)",
        "Метод опорных векторов (SVM)",
        "Многослойный перцептрон (MLP)"
    ]

    for i, (X, y) in enumerate(datasets):
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        for j, model in enumerate(models):
            ax = axes[i, j]

            # Обучение и предсказание
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            # Границы решений
            x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
            y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
            xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100), np.linspace(y_min, y_max, 100))

            Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
            Z = Z.reshape(xx.shape)

            # Визуализация
            ax.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
            ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='coolwarm', alpha=0.6)

            # Подписи
            if i == 0:
                ax.set_title(model_names[j], pad=12, fontsize=10)
            if j == 0:
                ax.set_ylabel(dataset_names[i], fontsize=10)

            # Точность в углу графика
            ax.text(0.95, 0.05, f'Точность: {accuracy:.2f}', transform=ax.transAxes, ha='right', bbox=dict(facecolor='white', alpha=0.8))

    plt.tight_layout()
    plt.show()

datasets = generate_datasets()
models = create_models()
plot_results_table(models, datasets)
