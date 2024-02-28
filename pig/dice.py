""" Roll a pair of dices """
import random
from pig import user

class Dice:
    """Dice class, rolls two dices"""
    def __init__(self):
        """Starts a random module """
        self.dice_low = 1
        self.dice_high = 6
#       self.current_user
        self.toss_count = 0
        random.seed()

    def toss(self):
        """Rolls two dices and returns their value"""
        dice_1 = random.randint(self.dice_low, self.dice_high)
        dice_2 = random.randint(self.dice_low, self.dice_high)
        return dice_1, dice_2

    def toss_count(self, user):
        """Count the number of tosses of the user"""
        if self.current_user.get_user_name == user:
            toss_count =+ 1
            return toss_count
        

