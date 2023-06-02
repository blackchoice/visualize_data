import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()

    plt.style.use('classic')
    fig = plt.subplots(figsize=(15, 9))
    ax = plt.axes(projection="3d")
    point_numbers = range(rw.num_points)
    ax.scatter3D(rw.x_values, rw.y_values, rw.z_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=100)

    ax.scatter3D(0, 0, 0, c='green', edgecolors='none', s=100)
    ax.scatter3D(rw.x_values[-1], rw.y_values[-1], rw.z_values[-1], c='red', cmap=plt.cm.Blues, edgecolors='none',
                 s=100)

    # ax.get_xaxis().set_visible(False)
    # ax.get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk? (y/n)")
    if keep_running == 'n':
        break
