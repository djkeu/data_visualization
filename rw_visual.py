import matplotlib.pyplot as plt

from random_walk import RandomWalk


# Make a random walk
rw =RandomWalk()
rw.fill_walk()

# Plot the points in the walk
plt.style.use('seaborn-v0_8')  # 'classic' doesn't close with 'q'

fig, ax = plt.subplots()
ax.scatter(rw.x_values, rw.y_values, s=15)

plt.show()
