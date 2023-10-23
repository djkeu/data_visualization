import plotly.express as px

from random_walk import RandomWalk

pw = RandomWalk(50_000)
pw.fill_walk()

fig = px.scatter(pw.x_values, pw.y_values)
fig.update_traces(marker_size = 1)
fig.show()
