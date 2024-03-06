"""Roll a pair of dice."""

import random


class Dice:
    """Dice class, rolls two dice."""

    def __init__(self):
        """Specified thresholds for lowest and highest return values."""
        self.dice_low = 1
        self.dice_high = 6

    def toss(self):
        """Toss two dice and return their value."""
        dice_1 = random.randint(self.dice_low, self.dice_high)
        dice_2 = random.randint(self.dice_low, self.dice_high)
        return dice_1, dice_2

    def dice_cheat(self):
        """Adjusting the lower threshold to 2 if user choses to cheat."""
        self.dice_low = 2
        dice_1 = random.randint(self.dice_low, self.dice_high)
        dice_2 = random.randint(self.dice_low, self.dice_high)
        return dice_1, dice_2
