import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from math import e
import numpy as np
import random
from sklearn.tree import DecisionTreeRegressor
from typing import List, Tuple, Generator, Union


def mean(lst: Generator[Union[int, float], None, None]):
    lst = list(lst)
    return sum(lst) / len(lst)

def smape(y_true: List[float], y_pred: List[float]) -> float:
    return 100 * mean([abs(p - a) / (abs(a) + abs(p)) if (a + p) != 0 and a >= 1e-100 else 0 for a, p in zip(y_true, y_pred)])


class App:
    def __init__(self):
        self.history: List[List[Tuple[float, float]]] = []
        self.smape_history: List[float] = []
        self.n_estimators = 100
        self.learning_rate = 0.1
        self.max_depth = 3
        self.trees = []
        self.initial_prediction = None
        self.data = self.generate()
        self.algorithm(self.data)
        self.plot_smape_per_epoch()
        self.slider_plot()

    def algorithm(self, points: List[Tuple[float, float]]):
        X = np.array([x for x, y in points]).reshape(-1, 1)
        y = np.array([y for x, y in points])

        self.initial_prediction = np.mean(y)
        current_prediction = np.full_like(y, self.initial_prediction)
        self.history.append(sorted(zip(X.flatten(), current_prediction)))
        self.smape_history.append(smape(y, current_prediction))

        for epoch in range(self.n_estimators):
            residuals = y - current_prediction
            tree = DecisionTreeRegressor(max_depth=self.max_depth)
            tree.fit(X, residuals)
            tree_pred = tree.predict(X)
            current_prediction += self.learning_rate * tree_pred
            self.history.append(sorted(zip(X.flatten(), current_prediction)))
            self.smape_history.append(smape(y, current_prediction))
            self.trees.append(tree)

    @staticmethod
    def generate() -> List[Tuple[float, float]]:
        def add_poisson_noise(signal, scale=1.0):
            ns = (signal / scale)
            noisy_signal = np.random.poisson(np.maximum(ns, 1e-6)) * scale
            return noisy_signal

        x = np.arange(-31.0, 31.1, 0.5)
        y = 10 / (1 + e ** (-0.7 * x + 2))
        noisy_y = add_poisson_noise(y, scale=0.05)
        n_x = []
        for i in x:
            jitter = (random.random() * 2 - 1) * 0.1
            if i < 0:
                noisy_x = add_poisson_noise(abs(i), scale=0.2)
                n_x.append(noisy_x * -1 + jitter)
            else:
                noisy_x = add_poisson_noise(i, scale=0.2)
                n_x.append(noisy_x + jitter)
        return [(xp, yp) for xp, yp in zip(n_x, noisy_y)]

    def plot_smape_per_epoch(self):
        plt.figure(figsize=(8, 4))
        plt.plot(self.smape_history, marker='o')
        plt.title("Зависимость sMAPE от эпохи")
        plt.xlabel("Эпоха")
        plt.ylabel("sMAPE (%)")
        plt.grid(True)
        plt.show()

    def slider_plot(self):

        fig, ax = plt.subplots(figsize=(10, 5))
        plt.subplots_adjust(bottom=0.25)

        x_true = np.linspace(-31, 31.1, 200)
        y_true = 10 / (1 + e ** (-0.7 * x_true + 2))
        ax.plot(x_true, y_true, label="Истинная функция", color="black", linestyle="--")

        x_data = [d[0] for d in self.data]
        y_data = [d[1] for d in self.data]
        ax.scatter(x_data, y_data, color="blue", s=20, alpha=0.5, label="Пуассоновский шум")

        pred_line, = ax.plot([], [], marker='o', color='red', label="Предсказание")

        ax.set_title(f"Эпоха 0, sMAPE = {self.smape_history[0]:.2f}%")
        ax.legend()
        ax.grid(True)

        ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03])
        slider = Slider(ax_slider, 'Эпоха', 0, len(self.history) - 1, valinit=100, valstep=1)

        def update(val):
            epoch = int(slider.val)
            data = self.history[epoch]
            x_pred = [pt[0] for pt in data]
            y_pred = [pt[1] for pt in data]
            pred_line.set_data(x_pred, y_pred)
            ax.set_title(f"Эпоха {epoch}, sMAPE = {self.smape_history[epoch]:.2f}%")
            ax.relim()
            ax.autoscale_view()
            fig.canvas.draw_idle()

        slider.on_changed(update)
        update(0)

        plt.show()


if __name__ == "__main__":
    App()
