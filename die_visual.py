from die import Die

# Create a D6 (six-sided die)
die = Die()

# Make rolls, store the results
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

