class User:

    def __init__(self, user_name):
        self.user_name = user_name
        self.highscore = 0
        self.score = 0
        self.game_count = 0
        self.toss_count = 0
        self.round_count = 0

    def change_name(self, new_name):
        self.user_name = new_name
        return self.user_name

    def update_score(self, score):
        """Updete the current users score"""
        if score == 0:
            self.score = 0
        else:
            self.score += score
        return self.score

    def update_game_count(self, count):
        """Update the current user game count"""
        self.game_count += count
        return self.game_count

    def update_toss_count(self):
        self.toss_count += 1
        return self.toss_count

    def update_round_count(self, score):
        if score == 0:
            self.round_count = 0
        else:
            self.round_count += score
        return self.round_count

    def get_user_name(self):
        return self.user_name

    def get_user_score(self):
        return self.score

    def get_highscore(self):
        return self.highscore

    def get_user_toss_count(self):
        return self.toss_count

    def cheat(self):
        self.score = 100
        self.toss_count = 1000
        return self.score

    def __str__(self) -> str:
        return f'{self.user_name}\nTotalscore: {self.highscore}\n \
            Current score: {self.score}'
