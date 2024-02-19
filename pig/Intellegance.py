import dice
import user


class Intellegance:

    def __init__(self):
        self.level = 0
        self.score = 0

    def level_choice(self, choise):
        levels = {"low": 1, "medium": 2, "hard": 3}
        self.level = levels.get(choise)
        return self.level

    def toss_or_hold(self, _):
        tosses = 0
        die = dice.Dice
        if self.level == 1:
            a, b = die().toss()
            result = a + b
            while result != 0 or tosses < 5:
                tosses += 1
                self.score += result
                a, b = die().toss()
                result = a + b
            if result == 0:
                self.score = 0

        elif self.level == 2:
            a, b = die().toss()
            result = a + b
            while result != 0 or self.score < _ or tosses < 12:
                tosses += 1
                self.score += result
                a, b = die().toss()
                result = a + b
            if result == 0:
                self.score = 0

        elif self.level == 3:
            die().dice_cheat()
            a, b = die().toss()
            result = a + b
            while self.score < _ or tosses < 5:
                tosses += 1
                self.score += result
                result = die().toss()
                result = a + b
