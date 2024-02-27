""" Roll a pair of dices """
import random


class Dice:
    """Dice class, rolls two dices"""
    def __init__(self):
        """Starts a random module """
        self.dice_low = 1
        self.dice_high = 6

    def toss(self):
        """Rolls two dices and returns their value"""
        dice_1 = random.randint(self.dice_low, self.dice_high)
        dice_2 = random.randint(self.dice_low, self.dice_high)
        return dice_1, dice_2

    def dice_cheat(self):
        self.dice_low = 2
