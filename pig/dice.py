"""Roll a pair of dice."""

import random


class Dice:
    """Dice class, rolls two dices."""

    def __init__(self):
        """Start a random module."""
        self.dice_low = 1
        self.dice_high = 6

    def toss(self):
        """Toss two dice and returns their value."""
        dice_1 = random.randint(self.dice_low, self.dice_high)
        dice_2 = random.randint(self.dice_low, self.dice_high)
        return dice_1, dice_2

    def dice_cheat(self):
        """If cheat is chosen the lowest returnis set to 2."""
        self.dice_low = 2
        dice_1 = random.randint(self.dice_low, self.dice_high)
        dice_2 = random.randint(self.dice_low, self.dice_high)
        return dice_1, dice_2
