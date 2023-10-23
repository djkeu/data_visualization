import matplotlib.pyplot as plt
from random import randint

from die import Die

rolls = []

for roll in range(1, 100):
    side = randint(1, 6)
    rolls.append(side)

