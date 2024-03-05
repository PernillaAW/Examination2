"""In thsi class we have the user."""


class User:
    """This class holds all user artibutes."""

    def __init__(self, user_name):
        """Create object user."""
        self.user_name = user_name
        self.highscore = 0
        self.score = 0
        self.game_count = 0
        self.toss_count = 0
        self.round_count = 0

    def change_name(self, new_name):
        """Will update user name."""
        self.user_name = new_name
        return self.user_name

    def update_score(self, score):
        """Update the current users score."""
        if score == 0:
            self.score = 0
        self.score += score
        return self.score

    def update_highscore(self):
        """Update highscore after winning."""
        self.highscore = self.score
        self.score = 0
        return self.highscore

    def update_game_count(self, count):
        """Update the current user game count."""
        self.game_count += count
        return self.game_count

    def update_toss_count(self):
        """Will update toss count."""
        self.toss_count += 1
        return self.toss_count

    def update_round_count(self, score):
        """Will update round count."""
        if score == 0:
            self.round_count = 0
        else:
            self.round_count += score
        return self.round_count

    def get_user_name(self):
        """Will return user name."""
        return self.user_name

    def get_user_score(self):
        """Will return user score."""
        return self.score

    def get_highscore(self):
        """Will return user highscore."""
        return self.highscore

    def get_user_toss_count(self):
        """Will return the number of tosses the user have done for the game."""
        return self.toss_count

    def cheat(self):
        """Cheat to win."""
        self.score = 100
        self.toss_count = 1000
        return self.score
