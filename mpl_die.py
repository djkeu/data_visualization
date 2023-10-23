import matplotlib.pyplot as plt
from random import randint

fnum_sides = 6

input_values = range(1, num_sides+1)

rolls = []
throws = 101
for throw in range(1, throws):
    roll = randint(1, num_sides+1)
    rolls.append(roll)

results = []
max_result = num_sides
for roll in range(1, max_result+1):
    result = rolls.count(roll)
    results.append(result)

print(results)

plt.style.use('seaborn-v0_8')
fix, ax = plt.subplots()
fmt = 'bo'
ax.plot(input_values, results, fmt)

ax.set_title(f"Resultaten van {throws - 1} x gooien met een dobbelsteen:")
ax.set_xlabel("Kanten van de dobbelsteen")
ax.set_ylabel("Aantal keer gegooid")

plt.show()
