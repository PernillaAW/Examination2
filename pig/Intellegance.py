from pig import dice


class Intellegance:
    """This class is used when you play against the computer. It has its own 
    intellegance for playing thegame."""

    def __init__(self):
        self.level = 0
        self.score = 0
        self.tosses = 0

    def level_choice(self, choise):
        """This medthod is for chosing the right level on the intelegance if
          you chose to play agaisnt the computer."""
        levels = {"low": 1, "medium": 2, "hard": 3}
        self.level = levels.get(choise)
        return self.level

    def calculate_result(self, a, b):
        """This method will calculate the result of the dice toss"""
        if a == 1 and b == 1:
            result = 0
            self.score = 0
        elif a == 1 or b == 1:
            result = 1
            self.score += 0
        else:
            result = a + b
            self.score += result
        return result

    def toss(self, die):
        """This is the toss comand with in the intellagance"""
        self.tosses += 1
        a, b = die().toss()
        result = self.calculate_result(a, b)
        return result

    def toss_or_hold(self, player):
        """This is the gameplay for intelagance. it hold all the methods and
          calculations for playing"""
        self.tosses = 0
        die = dice.Dice
        if self.level == 1:
            result = self.toss(die)
            while result != 0 and self.tosses < 5 and result != 1:
                result = self.toss(die)
            return 1

        elif self.level == 2:
            result = self.toss(die)
            while result != 1 and result != 0 and self.tosses < 8 or \
                    self.score < 10 + player.get_user_score():
                result = self.toss(die)
            return 2

        elif self.level == 3:
            die().dice_cheat()
            result = self.toss(die)
            while self.score < 6 + player.get_user_score() or \
                    self.tosses < 5:
                result = self.toss(die)
            return 3

    def __str__(self) -> str:
        return f'Computer:\nCurrent score: {self.score}'
