# ToDo: 15.1 Cubes
# A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.

import matplotlib.pyplot as plt

x_values = range(1, 6)
y_values = [x **3 for x in x_values]
for value in y_values:
    print(value)

