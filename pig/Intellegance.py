"""intellegance module."""

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
            result = 0
        else:
            result = a + b
            self.score += result
        return result

    def tossing(self, die):
        """Toss command within the intellagance."""
        self.tosses += 1
        if self.level == 3:
            a, b = die().dice_cheat()
            result = self.calculate_result(a, b)
            return result
        a, b = die().toss()
        result = self.calculate_result(a, b)
        return result

    def toss_or_hold(self, player):
        """Intellegance gameplay."""
        self.tosses = 0
        die = dice.Dice
        result = self.tossing(die)
        self.is_winner()
        while result != 0 \
                and self.tosses < (4 * self.level) \
                and self.score < (self.level * 4 + player.get_user_score()):
            result = self.tossing(die)
            self.is_winner()
        return self.level

    def is_winner(self):
        """Test to see if winner."""
        if self.score >= 100:
            self.computer_win()
            shell.Shell().cmdloop()

    def computer_win(self):
        """If the computer wins."""
        print('Computer has won!')
        self.score = 0
        self.tosses = 10
        return self.tosses

    def __str__(self) -> str:
        """Intellegance to print."""
        return f"Computer:\nCurrent score: {self.score}"
