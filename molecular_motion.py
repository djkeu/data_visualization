import matplotlib.pyplot as plt

from molecular_walk import RandomWalk


# Make a random walk
rw =RandomWalk(5_000)
rw.fill_walk()

# Plot the points in the walk
plt.style.use('seaborn-v0_8')  # 'classic' doesn't close with 'q'

fig, ax = plt.subplots(figsize=(13,7))
point_numbers = range(rw.num_points)
ax.plot(rw.x_values, rw.y_values, linewidth='0.7')

# Emphasize the first and last points
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

# Remove the axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()
