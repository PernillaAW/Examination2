import highscore


class User:
    
    def __init__(self, user_name):
        self.user_name = user_name
        self.highscore = 0
        self.score = 0

    def change_name(self):
        """Change the name of the user"""
        print(f"Current Username: {self.user_name}")
        user_name = input(f"Change {self.user_name} to: ")
        old_name = self.user_name
        self.user_name = user_name
        highscore.Highscore().check_list(self, old_name, 2)
        print(f'Your usename has now been changed to {self.user_name}')

    def update_score(self, score):
        """Updete the current users score"""
        self.score += score
        return self.score

    def update_game_count(self, count):
        """Update the current user game count"""
        self.game_count =+ count
        return self.game_count

    def get_user_name(self):
        return self.user_name

    def cheat(self):
        self.score = 100

    def __str__(self) -> str:
        return f'User name: {self.user_name}\nTotalscore: {self.highscore}'
