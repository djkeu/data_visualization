# ToDo: 15.1 Cubes
# A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.

import matplotlib.pyplot as plt

# x_values = range(1, 6)
x_values = range(1, 5001)
y_values = [x **3 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(x_values, y_values)

plt.show()
