from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# Create a D6 dice
die_1 = Die(8)
die_2 = Die(8)

# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)


print(results)

# Analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
x_values = list(range(1, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

# Plot 
x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling one 2 D8 dice 1000 times', xaxis=x_axis_config, yaxis = y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename= '2_d8.html')