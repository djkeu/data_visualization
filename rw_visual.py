import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Keep making new walks, as long as the program is active
while True:
    # Make a random walk
    rw =RandomWalk()
    rw.fill_walk()

    # Plot the points in the walk
    plt.style.use('seaborn-v0_8')  # 'classic' doesn't close with 'q'

    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, s=15)

    plt.show()

    keep_running = input("\nNog een eindje lopen? \n('n' om te stoppen): ")
    if keep_running == 'n':
        break
