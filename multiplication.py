from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die_1 = Die()
die_2 = Die()

results = []

results = [die_1.roll() * die_2.roll() for _ in range(1, 1000)]

frequencies = []
maximum_result = die_1.num_sides * die_2.num_sides

frequencies = [results.count(value) for value in range(1, maximum_result + 1)]

x_values = list(range(1, maximum_result+1))
data = Bar(x=x_values, y=frequencies)

x_axis_config = {'title': 'Result','dtick': 1 }
y_axis_config = {'title': 'Frequency of Result', 'dtick': 10}

my_layout = Layout(title="Results of multiplying the outcomes of two dices rolling 1000 times", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='html/multiplication.html')
