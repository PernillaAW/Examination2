"""Intellegance module."""

from pig import dice, shell


class Intellegance:
    """Class intellegence is the computer intellegance."""

    def __init__(self):
        """Create intellegance."""
        self.level = 0
        self.score = 0
        self.tosses = 0

    def level_choice(self, choise):
        """Choose difficulty level."""
        levels = {"low": 1, "medium": 2, "hard": 3}
        self.level = levels.get(choise)
        return self.level

    def calculate_result(self, a, b):
        """Calculate the result of the dice toss."""
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

    def tossing(self, die):
        """Toss command within the intellagance."""
        self.tosses += 1
        a, b = die().toss()
        result = self.calculate_result(a, b)
        return result

    def toss_or_hold(self, player):
        """Intellegance gameplay."""
        self.tosses = 0
        die = dice.Dice
        if self.level == 1:
            result = self.tossing(die)
            self.computer_win(result)
            while result != 0 and self.tosses < 5 and result != 1:
                result = self.tossing(die)
                self.computer_win(result)
            return 1

        elif self.level == 2:
            result = self.tossing(die)
            while (
                result != 1
                and result != 0
                and self.tosses < 8
                or self.score < 10 + player.get_user_score()
                    ):
                result = self.tossing(die)
                self.computer_win(result)
            return 2

        elif self.level == 3:
            die().dice_cheat()
            result = self.tossing(die)
            while self.score < 6 + player.get_user_score() or self.tosses < 5:
                result = self.tossing(die)
                self.computer_win(result)

            return 3
        
    def computer_win(self, result):
        if result >= 100:
            print('Computer has won!')
            self.score = 0
            return True


    def __str__(self) -> str:
        """Intellegance to print."""
        return f"Computer:\nCurrent score: {self.score}"
