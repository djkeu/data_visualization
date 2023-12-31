from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die


# 15.7 Three dice
die_1 = Die()
die_2 = Die()
die_3 = Die()

results = []
for roll_num in range(100_000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides

for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

x_values = list(range(1, max_result+1))
data = Bar(x=x_values, y=frequencies)

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {"title": "Frequency of Result"}

my_layout = Layout(title="Result of rolling three D6's 1000 times",
xaxis=x_axis_config, yaxis=y_axis_config)

offline.plot({'data': data, 'layout': my_layout}, filename='html/three_dice.html')

