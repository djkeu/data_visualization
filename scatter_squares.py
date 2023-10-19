import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = []

for value in x_values:
    y_values.append(value ** 2)

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(2, 4, s=200)

# Set chart title and label axes
ax.set_title("Square numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()
