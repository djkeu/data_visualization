from random import randint

class Die:
    """Class representng singel die."""

    def __init__(self, num_sides=6) -> None:
        """Initialize six-sided die."""
        self.num_sides = num_sides

    def roll(self):
        """Return random value between 1 and number of sides."""
        return randint(1, self.num_sides)
