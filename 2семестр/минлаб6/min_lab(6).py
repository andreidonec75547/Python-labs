import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


def func(x):
    return (x**2 * np.exp(-0.1*x) + 2*np.sin(x) + 3)

def dfunc(x):
    return 2 * x * np.exp(-0.1 * x) - (0.1 * np.exp(-0.1 * x) * (x ** 2)) + 2 * np.cos(x)

def grfunc(f, df, x_0, speed, epohs):
        xlist = [x_0]
        ylist = [f(x_0)]

        for _ in range(1, epohs):
            current_x = xlist[-1]
            gradient = df(current_x)
            new_x = current_x - speed * gradient
            xlist.append(new_x)
            ylist.append(f(new_x))

        return np.array(xlist), np.array(ylist)

def update(val):
    speed = speed_slider.val
    x_new, y_new = grfunc(func, dfunc, 15.15, speed, 100)
    trajectory.set_data(x_new, y_new)
    current_point.set_data(x_new[0], y_new[0])
    fig.canvas.draw_idle()


x = np.linspace(14, 18, 200)
y = [func(val) for val in x]

xstar, ystar = grfunc(func, dfunc, 15.15, 0.1, 100,)
plt.plot(xstar, ystar, c='red')

speed = 0.1

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_xlabel('X')
ax.set_ylabel('Y')
trajectory, = ax.plot(xstar, ystar, 'ro-', markersize=2, label='Траектория')
current_point, = ax.plot(xstar[0], ystar[0], 'go', markersize=3, label='Текущая точка')
ax.legend()

slider_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
speed_slider = Slider(
    ax=slider_ax,
    label='Скорость обучения',
    valmin=0.007,
    valmax=1,
    valinit=speed,
    valstep=0.001)

speed_slider.on_changed(update)

plt.show()
