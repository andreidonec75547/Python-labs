import math
import random
import matplotlib.pyplot as plt

random.seed(24)


def generatePoints():
    points = []

    clrCnt = [[100, 250]]
    for i in range(1, 3):
        a, b = random.randint(105, 125), random.randint(-100, 100)
        clrCnt.append([clrCnt[i - 1][0] + a, clrCnt[i - 1][1] + b])

    for center in clrCnt:
        for i in range(0, 20):
            r = random.randint(3, 50)
            angle = math.pi * random.uniform(-2, 2)

            x = r * math.cos(angle)
            y = r * math.sin(angle)

            points.append([center[0] + x, center[1] + y, 'X'])

    for i in range(0, 123):
        a = random.randint(0, len(points) - 1)
        b = random.randint(0, len(points) - 1)
        points[a], points[b] = points[b], points[a]

    return points


points = generatePoints()


def kmeansClusters(points, MAX_ITER):
    i_iter = 0
    centroids = [[points[0][0], points[0][1], 1], [points[1][0], points[1][1], 2], [points[2][0], points[2][1], 3]]

    avg = [[centroids[0][0], centroids[0][1], 1], [centroids[1][0], centroids[1][1], 1],
           [centroids[2][0], centroids[2][1], 1]]

    while True:
        for pt in points:
            min_dist = 999999999999999999999999999999
            for ct in centroids:
                dist = math.sqrt((pt[0] - ct[0]) ** 2 + (pt[1] - ct[1]) ** 2)
                if dist < min_dist:
                    min_dist = dist
                    pt[2] = ct[2]

        for pt in points:
            avg[pt[2] - 1][0] += pt[0]
            avg[pt[2] - 1][1] += pt[1]
            avg[pt[2] - 1][2] += 1

        centroids = [[avg[0][0] / avg[0][2], avg[0][1] / avg[0][2], 1],
                     [avg[1][0] / avg[1][2], avg[1][1] / avg[1][2], 2],
                     [avg[2][0] / avg[2][2], avg[2][1] / avg[2][2], 3]]

        i_iter += 1
        print(i_iter)
        if i_iter > MAX_ITER:
            break


fig, ax = plt.subplots()

plt.xlim([0, 500])
plt.ylim([0, 500])

scatter_objects = []


def update(MAX_ITER):
    global points, scatter_objects
    for pt in points:
        pt[2] = 'X'

    kmeansClusters(points, MAX_ITER)

    for scatter in scatter_objects:
        scatter.remove()
    scatter_objects.clear()

    x = []
    y = []
    colors = []

    colorMap = {
        1: 'blue',
        2: 'red',
        3: 'green'
    }

    for pt in points:
        x.append(pt[0])
        y.append(pt[1])
        colors.append(colorMap[pt[2]])

    scatter = ax.scatter(x, y, c=colors)
    scatter_objects.append(scatter)

    centroids = [[points[0][0], points[0][1], 1], [points[1][0], points[1][1], 2], [points[2][0], points[2][1], 3]]

    avg = [[centroids[0][0], centroids[0][1], 1], [centroids[1][0], centroids[1][1], 1],
           [centroids[2][0], centroids[2][1], 1]]

    points_prev = []

    for pt in points:
        avg[pt[2] - 1][0] += pt[0]
        avg[pt[2] - 1][1] += pt[1]
        avg[pt[2] - 1][2] += 1

    cs = [[avg[0][0] / avg[0][2], avg[0][1] / avg[0][2], 1],
          [avg[1][0] / avg[1][2], avg[1][1] / avg[1][2], 2],
          [avg[2][0] / avg[2][2], avg[2][1] / avg[2][2], 3]]

    cent1 = ax.scatter(cs[0][0], cs[0][1], color='black', marker='x')
    scatter_objects.append(cent1)
    cent2 = ax.scatter(cs[1][0], cs[1][1], color='black', marker='x')
    scatter_objects.append(cent2)
    cent3 = ax.scatter(cs[2][0], cs[2][1], color='black', marker='x')
    scatter_objects.append(cent3)


axfreq = fig.add_axes([0.25, 0.01, 0.65, 0.03])
freq_slider = plt.Slider(
    ax=axfreq,
    label='Iterations',
    valmin=1,
    valmax=100,
    valinit=50,
    valstep=1,
)

freq_slider.on_changed(update)

update(50)

plt.show()
plt.show()
