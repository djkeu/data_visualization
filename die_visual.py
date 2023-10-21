from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6 (six-sided die)
die = Die()

# Make rolls, store the results
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

