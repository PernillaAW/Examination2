class User:

    def __init__(self, user_name):
        self.user_name = user_name
        self.highscore = 0
        self.score = 0
        self.game_count = 0

    def change_name(self, new_name):
        self.user_name = new_name
        return self.user_name

    def update_score(self, score):
        """Updete the current users score"""
        self.score += score
        return self.score

    def update_game_count(self, count):
        """Update the current user game count"""
        self.game_count += count
        return self.game_count

    def get_user_name(self):
        return self.user_name

    def get_user_score(self):
        return self.score

    def cheat(self):
        self.score = 100
        return self.score

    def __str__(self) -> str:
        return f'{self.user_name}\nTotalscore: {self.highscore}\n \
            Current score: {self.score}'
