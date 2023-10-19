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
    ax.scatter(rw.x_values, rw.y_values, s=15)

    plt.show()

    keep_running = input("Nog een eindje lopen? (j/n): ")
    if keep_running == 'n':
        break
    