import matplotlib.pyplot as plt

from die import Die

die = Die()

input_values = range(1, die.num_sides+1)

rolls = []
throws = 101
for roll in range(1, throws):
    side = die.roll()
    rolls.append(side)

results = []
max_result = die.num_sides
for roll in range(1, max_result+1):
    result = rolls.count(roll)
    results.append(result)

print(results)

plt.style.use('seaborn-v0_8')
fix, ax = plt.subplots()
fmt = 'bo'
ax.plot(input_values, results, fmt)

ax.set_title(f"Resultaten van {throws} keer gooien met een dobbelsteen:")
ax.set_xlabel("Kanten van de dobbelsteen")
ax.set_ylabel("Aantal keer gegooid")

plt.show()
