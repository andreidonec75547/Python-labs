import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

x_min = -5
x_max = 5
points = 100
true_a = 0.8  # Истинный коэффициент a
true_b = -1.5  # Истинный коэффициент b
true_c = 2.0  # Истинный коэффициент c
noise_amp = 5  # Амплитуда шума


def generate_data():
    x = np.linspace(x_min, x_max, points)
    y = true_a * x ** 2 + true_b * x + true_c + np.random.uniform(-noise_amp, noise_amp, size=len(x))
    return x, y


x, y = generate_data()


def get_da(x, y, a, b, c):
    return (2 / len(x)) * np.sum(x ** 2 * ((a * x ** 2 + b * x + c) - y))


def get_db(x, y, a, b, c):
    return (2 / len(x)) * np.sum(x * ((a * x ** 2 + b * x + c) - y))


def get_dc(x, y, a, b, c):
    return (2 / len(x)) * np.sum((a * x ** 2 + b * x + c) - y)


def mse(y_true, y_pred):
    return np.mean((y_true - y_pred) ** 2)


def fit(x, y, speed=0.001, epochs=1000, a0=0, b0=0, c0=0):
    a, b, c = a0, b0, c0
    history = {'a': [a], 'b': [b], 'c': [c], 'mse': [mse(y, a * x ** 2 + b * x + c)]}

    for _ in range(epochs):
        da = get_da(x, y, a, b, c)
        db = get_db(x, y, a, b, c)
        dc = get_dc(x, y, a, b, c)

        a -= speed * da
        b -= speed * db
        c -= speed * dc

        history['a'].append(a)
        history['b'].append(b)
        history['c'].append(c)
        history['mse'].append(mse(y, a * x ** 2 + b * x + c))

    return history


learning_rate = 0.001
epochs = 500
initial_a, initial_b, initial_c = 0, 0, 0

history = fit(x, y, speed=learning_rate, epochs=epochs,
              a0=initial_a, b0=initial_b, c0=initial_c)

# Визуализация с ползунком
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(bottom=0.25)

# График данных и регрессии
scatter = ax1.scatter(x, y, c='blue', label='Данные', alpha=0.6)
x_plot = np.linspace(x_min, x_max, 100)
curve, = ax1.plot(x_plot, history['a'][0] * x_plot ** 2 + history['b'][0] * x_plot + history['c'][0],
                  'r-', linewidth=2, label='Регрессия')
ax1.set_title(f'Квадратичная регрессия (MSE: {history["mse"][0]:.2f})')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True)

# График MSE
mse_line, = ax2.plot(history['mse'], 'g-')
ax2.set_title('Среднеквадратичная ошибка (MSE)')
ax2.set_xlabel('Эпоха')
ax2.set_ylabel('MSE')
ax2.grid(True)

# Ползунок
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03])
slider = Slider(ax_slider, 'Эпоха', 0, epochs, valinit=0, valstep=1)


# Обновление графиков
def update(val):
    epoch = int(slider.val)
    a = history['a'][epoch]
    b = history['b'][epoch]
    c = history['c'][epoch]

    curve.set_ydata(a * x_plot ** 2 + b * x_plot + c)
    ax1.set_title(f'Квадратичная регрессия (Эпоха: {epoch}, MSE: {history["mse"][epoch]:.2f})')

    mse_line.set_data(range(epoch + 1), history['mse'][:epoch + 1])
    ax2.set_xlim(0, max(epoch, 10))
    ax2.set_ylim(0, max(history['mse'][:epoch + 1]) * 1.1)

    fig.canvas.draw_idle()


slider.on_changed(update)

plt.show()

# Вывод результатов
final_a = history['a'][-1]
final_b = history['b'][-1]
final_c = history['c'][-1]
print(f"Истинные коэффициенты: a = {true_a}, b = {true_b}, c = {true_c}")
print(f"Найденные коэффициенты: a = {final_a:.4f}, b = {final_b:.4f}, c = {final_c:.4f}")
print(f"Финальная MSE: {history['mse'][-1]:.4f}")
