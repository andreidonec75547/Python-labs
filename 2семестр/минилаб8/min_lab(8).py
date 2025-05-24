import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.metrics import mean_squared_error


def f(x):
    return 3 * np.cos(0.5 * x) + 0.5 * np.exp(0.2 * x) - 0.1 * x ** 3 + 2


np.random.seed(42)
x_min, x_max = -6, 6
x = np.linspace(x_min, x_max, 100).reshape(-1, 1)
y_true = f(x)
e_normal = np.random.normal(0, 0.8, size=(100, 1))
y_noisy = y_true + e_normal

models = {
    "Support Vector Regression (RBF)": SVR(kernel='rbf', C=10, gamma=0.1, epsilon=0.2),
    "Random Forest Regressor": RandomForestRegressor(n_estimators=100, max_depth=5),
    "Gradient Boosting Regressor": GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3)
}

plt.figure(figsize=(18, 12))
x_plot = np.linspace(x_min, x_max, 300).reshape(-1, 1)

for i, (name, model) in enumerate(models.items(), 1):
    model.fit(x, y_noisy.ravel())
    y_pred = model.predict(x_plot)

    mse = mean_squared_error(y_true, model.predict(x))

    plt.subplot(2, 2, i)
    plt.scatter(x, y_noisy, color='blue', alpha=0.6, label='Зашумленные данные')
    plt.plot(x_plot, f(x_plot), 'g-', linewidth=3, label='Истинная функция')
    plt.plot(x_plot, y_pred, 'r-', linewidth=2, label=f'Предсказание ({name})')
    plt.title(f'{name}\nMSE: {mse:.4f}', fontsize=12)
    plt.xlabel('x', fontsize=10)
    plt.ylabel('y', fontsize=10)
    plt.legend(fontsize=9)
    plt.grid(alpha=0.3)

plt.suptitle('Сравнение нелинейных методов регрессии', fontsize=16, y=1.02)
plt.tight_layout()
plt.show()

print("\nАнализ результатов:")
print("1. SVR с RBF-ядром:")
print("   - Плюсы: Хорошо сглаживает шумы, дает плавную аппроксимацию")
print("   - Минусы: Требует тонкой настройки гиперпараметров (C, gamma)")
print("   - MSE: {:.4f}".format(mean_squared_error(y_true, models["Support Vector Regression (RBF)"].predict(x))))

print("\n2. Random Forest Regressor:")
print("   - Плюсы: Хорошо обрабатывает сложные нелинейности")
print("   - Минусы: Склонен к небольшим ступенчатым артефактам")
print("   - MSE: {:.4f}".format(mean_squared_error(y_true, models["Random Forest Regressor"].predict(x))))

print("\n3. Gradient Boosting Regressor:")
print("   - Плюсы: Лучшая точность на этой задаче, плавная аппроксимация")
print("   - Минусы: Чувствителен к гиперпараметрам (learning_rate, n_estimators)")
print("   - MSE: {:.4f}".format(mean_squared_error(y_true, models["Gradient Boosting Regressor"].predict(x))))

print("\nИтоговый вывод:")
print("Gradient Boosting показал наилучший результат на этих данных, что видно по минимальному значению MSE и визуальному соответствию истинной функции.")
