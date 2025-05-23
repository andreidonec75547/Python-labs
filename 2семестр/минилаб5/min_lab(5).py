import random as rnd
import warnings
from itertools import cycle, islice

import matplotlib.pyplot as plt
import numpy as np
from sklearn import cluster, datasets, mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler

# Генерируем 3 числа
rnd.seed("1(191911919119191991")
for _ in range(3):
    print(rnd.randint(1, 11))

sample_number = 500
random_seed = 30

# Создаем различные типы кластеров для тестирования
circle_data = datasets.make_circles(
    n_samples=sample_number, factor=0.5, noise=0.05, random_state=random_seed
)
moon_data = datasets.make_moons(n_samples=sample_number, noise=0.05, random_state=random_seed)
blob_data = datasets.make_blobs(n_samples=sample_number, random_state=random_seed)

rng = np.random.RandomState(random_seed)
random_points = rng.rand(sample_number, 2), None

X_blobs, y_blobs = datasets.make_blobs(n_samples=sample_number, random_state=random_seed)
transformation_matrix = [[0.6, -0.6], [-0.4, 0.8]]
X_aniso = np.dot(X_blobs, transformation_matrix)
aniso_data = (X_aniso, y_blobs)

varied_blobs = datasets.make_blobs(
    n_samples=sample_number, cluster_std=[1.0, 2.5, 0.5], random_state=random_seed
)

plt.figure(figsize=(9 * 2 + 3, 13))
plt.subplots_adjust(
    left=0.02, right=0.98, bottom=0.02, top=0.95, wspace=0.05, hspace=0.01
)

plot_counter = 1

base_params = {
    "quantile": 0.3,
    "eps": 0.3,
    "damping": 0.9,
    "preference": -200,
    "n_neighbors": 3,
    "n_clusters": 3,
    "min_samples": 7,
    "xi": 0.05,
    "min_cluster_size": 0.1,
    "allow_single_cluster": True,
    "hdbscan_min_cluster_size": 15,
    "hdbscan_min_samples": 3,
    "random_state": 42,
}

dataset_collection = [
    (circle_data, {"damping": 0.77, "preference": -240, "quantile": 0.2,
                   "n_clusters": 2, "min_samples": 7, "xi": 0.08}),
    (moon_data, {"damping": 0.75, "preference": -220, "n_clusters": 2,
                 "min_samples": 7, "xi": 0.1}),
    (varied_blobs, {"eps": 0.18, "n_neighbors": 2, "min_samples": 7,
                    "xi": 0.01, "min_cluster_size": 0.2}),
    (aniso_data, {"eps": 0.15, "n_neighbors": 2, "min_samples": 7,
                  "xi": 0.1, "min_cluster_size": 0.2}),
    (blob_data, {"min_samples": 7, "xi": 0.1, "min_cluster_size": 0.2}),
    (random_points, {}),
]

for dataset_idx, (current_dataset, algorithm_params) in enumerate(dataset_collection):
    params = base_params.copy()
    params.update(algorithm_params)

    features, true_labels = current_dataset

    features = StandardScaler().fit_transform(features)

    bandwidth = cluster.estimate_bandwidth(features, quantile=params["quantile"])

    connectivity = kneighbors_graph(
        features, n_neighbors=params["n_neighbors"], include_self=False
    )
    connectivity = 0.5 * (connectivity + connectivity.T)


    hdbscan_clusterer = cluster.HDBSCAN(
        min_samples=params["hdbscan_min_samples"],
        min_cluster_size=params["hdbscan_min_cluster_size"],
        allow_single_cluster=params["allow_single_cluster"],
    )

    optics_clusterer = cluster.OPTICS(
        min_samples=params["min_samples"],
        xi=params["xi"],
        min_cluster_size=params["min_cluster_size"],
    )

    affinity_clusterer = cluster.AffinityPropagation(
        damping=params["damping"],
        preference=params["preference"],
        random_state=params["random_state"],
    )

    algorithms_to_test = (
        ("Affinity Propagation", affinity_clusterer),
        ("HDBSCAN", hdbscan_clusterer),
        ("OPTICS", optics_clusterer),
    )

    for algorithm_name, clustering_algorithm in algorithms_to_test:
        with warnings.catch_warnings():
            warnings.filterwarnings(
                "ignore",
                message="the number of connected components of the "
                        + "connectivity matrix is [0-9]{1,2}"
                        + " > 1. Completing it to avoid stopping the tree early.",
                category=UserWarning,
            )
            warnings.filterwarnings(
                "ignore",
                message="Graph is not fully connected, spectral embedding"
                        + " may not work as expected.",
                category=UserWarning,
            )
            clustering_algorithm.fit(features)

        # Получаем предсказанные метки
        if hasattr(clustering_algorithm, "labels_"):
            predicted_labels = clustering_algorithm.labels_.astype(int)
        else:
            predicted_labels = clustering_algorithm.predict(features)

        # Визуализация результатов
        plt.subplot(len(dataset_collection), len(algorithms_to_test), plot_counter)
        if dataset_idx == 0:
            plt.title(algorithm_name, size=18)

        # Цветовая схема для кластеров
        color_palette = np.array(
            list(
                islice(
                    cycle([
                        "#377eb8", "#ff7f00", "#4daf4a", "#f781bf",
                        "#a65628", "#984ea3", "#999999", "#e41a1c",
                        "#dede00"
                    ]),
                    int(max(predicted_labels) + 1),
                )
            )
        )
        # Черный цвет для выбросов
        color_palette = np.append(color_palette, ["#000000"])

        plt.scatter(features[:, 0], features[:, 1], s=10, color=color_palette[predicted_labels])

        plt.xlim(-2.5, 2.5)
        plt.ylim(-2.5, 2.5)
        plt.xticks(())
        plt.yticks(())
        plot_counter += 1

plt.show()
