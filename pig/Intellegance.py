from pig import Dice


class Intellegance:

    def __init__(self):
        self.level = 0
        self.score = 0

    def level_choice(self, choise):
        levels = {"low": 1, "medium": 2, "hard": 3}
        self.level = levels.get(choise)
        return self.level

    def calculate_result(self, a, b):
        if a == 1 and b == 1:
            result = 0
        elif a == 1 or b == 1:
            result = 1
        else:
            result = a + b
        return result

    def toss_or_hold(self, player):
        tosses = 0
        die = Dice.Dice
        if self.level == 1:
            a, b, c = die().toss()
            result = self.calculate_result(a, b)
            while result != 0 and tosses < 5 and result != 1:
                tosses += 1
                self.score += result
                a, b, c = die().toss()
                result = self.calculate_result(a, b)
            if result == 0:
                self.score = 0
            return True

        elif self.level == 2:
            a, b, c = die().toss()
            result = self.calculate_result(a, b)
            while result != 0 and tosses < 8 or \
                    self.score < 10 + player.get_user_score():
                tosses += 1
                self.score += result
                a, b, c = die().toss()
                result = self.calculate_result(a, b)
            if result == 0:
                self.score = 0
            return True

        elif self.level == 3:
            die().dice_cheat()
            a, b, c = die().toss()
            result = self.calculate_result(a, b)
            while self.score < 6 + player.get_user_score() or tosses < 5:
                tosses += 1
                self.score += result
                a, b, c = die().toss()
                result = self.calculate_result(a, b)
            return True

    def __str__(self) -> str:
        return f'Computer:\nCurrent score: {self.score}'
