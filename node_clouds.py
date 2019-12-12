import numpy as np
import matplotlib.pyplot as plt


def print_cloud(points, Lx, Ly, delta):
    plt.figure()
    plt.scatter(points[:, 0], points[:, 1], s=Lx, alpha=1)

    x_lines = (0, delta * Lx, (1 - delta) * Lx, Lx)
    y_lines = (0, delta * Ly, (1 - delta) * Ly, Ly)

    plt.plot((0, 0), (0, Ly), 'k-', color='r')
    plt.plot((0, Lx), (0, 0), 'k-', color='r')
    plt.plot((0, Lx), (Ly, Ly), 'k-', color='r')
    plt.plot((Lx, Lx), (0, Ly), 'k-', color='r')

    delta_x = Lx * delta
    delta_y = Ly * delta
    plt.plot((delta_x, delta_x), (0, Ly), 'k-', color='r')
    plt.plot((0, Lx), (delta_y, delta_y), 'k-', color='r')
    plt.plot((0, Lx), (Ly - delta_y, Ly - delta_y), 'k-', color='r')
    plt.plot((Lx - delta_x, Lx - delta_x), (0, Ly), 'k-', color='r')

    plt.show()

def uniform_node_clouds(Lx, Ly, delta, Npoints, line_share):
    xy_min = [0, 0]
    xy_max = [Lx, Ly]

    xline_qty = int(np.sqrt(Npoints) / Ly)
    yline_qty = int(np.sqrt(Npoints) / Lx)

    points = np.random.uniform(low=xy_min, high=xy_max, size=(Npoints, 2))
    xline_points = np.linspace(0, Lx, xline_qty)
    yline_points = np.linspace(0, Ly, yline_qty)

    x_lines = (0, delta * Lx, (1 - delta) * Lx, Lx)
    y_lines = (0, delta * Ly, (1 - delta) * Ly, Ly)

    for i in range(0, 4):
        xline = np.concatenate((xline_points[:, np.newaxis], np.repeat(x_lines[i], xline_qty)[:, np.newaxis]), axis=1)
        yline = np.concatenate((np.repeat(y_lines[i], yline_qty)[:, np.newaxis], yline_points[:, np.newaxis]), axis=1)

        points = np.concatenate((points, xline))
        points = np.concatenate((points, yline))
    return points