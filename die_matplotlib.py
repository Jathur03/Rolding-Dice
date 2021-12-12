import matplotlib.pyplot as plt
from die import Die

die_1 = Die(8)
die_2 = Die(8)

plt.style.use('seaborn')
fig, ax = plt.subplots()

results = []
for roll_num in range(10000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# set size of tick labels
ax.tick_params(axis = 'both', which = 'major', labelsize = 8)

# creating the hisogram
ax.hist(frequencies, bins=die_1.num_sides+die_2.num_sides)

plt.show()