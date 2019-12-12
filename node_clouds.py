import numpy as np
import matplotlib.pyplot as plt


def print_cloud(points, l_x, l_y, delta):
    plt.figure()
    plt.scatter(points[:, 0], points[:, 1], s=l_x, alpha=1)

    plt.plot((0, 0), (0, l_y), 'k-', color='r')
    plt.plot((0, l_x), (0, 0), 'k-', color='r')
    plt.plot((0, l_x), (l_y, l_y), 'k-', color='r')
    plt.plot((l_x, l_x), (0, l_y), 'k-', color='r')

    delta_x = l_x * delta
    delta_y = l_y * delta
    plt.plot((delta_x, delta_x), (0, l_y), 'k-', color='r')
    plt.plot((0, l_x), (delta_y, delta_y), 'k-', color='r')
    plt.plot((0, l_x), (l_y - delta_y, l_y - delta_y), 'k-', color='r')
    plt.plot((l_x - delta_x, l_x - delta_x), (0, l_y), 'k-', color='r')

    plt.show()


def uniform_node_clouds(l_x, l_y, delta, n_points):
    xy_min = [0, 0]
    xy_max = [l_x, l_y]

    dot_dist = np.sqrt(l_x * l_y / n_points)

    x_line_qty = int(l_x/dot_dist)
    y_line_qty = int(l_y/dot_dist)

    points = np.random.uniform(low=xy_min, high=xy_max, size=(n_points, 2))
    x_line_points = np.linspace(0, l_x, x_line_qty)
    y_line_points = np.linspace(0, l_y, y_line_qty)

    x_lines = (0, delta * l_x, (1 - delta) * l_x, l_x)
    y_lines = (0, delta * l_y, (1 - delta) * l_y, l_y)

    for i in range(0, 4):
        x_line = np.concatenate((x_line_points[:, np.newaxis], np.repeat(x_lines[i], x_line_qty)[:, np.newaxis]), axis=1)
        y_line = np.concatenate((np.repeat(y_lines[i], y_line_qty)[:, np.newaxis], y_line_points[:, np.newaxis]), axis=1)

        points = np.concatenate((points, x_line))
        points = np.concatenate((points, y_line))

    return points

