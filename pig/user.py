from pig import highscore

class User:

    def __init__(self, user_name):
        self.user_name = user_name
        self.highscore = 0
        self.score = 0
        self.game_count = 0
        self.toss_count = 0
        self.round_count = 0

    def change_name(self):
        """Change the name of the user"""
        print(f"Current Username: {self.user_name}")
        user_name = input(f"Change {self.user_name} to: ")
        old_name = self.user_name
        self.user_name = user_name
        highscore.Highscore().check_list_add_remove(self, old_name)
        print(f'Your usename has now been changed to {self.user_name}')
    
    def get_user_name(self):
        return self.user_name
    
    def update_highscore(self, score):
        """Updates the highscore"""
        self.highscore += score
        return self.highscore
    
    def get_highscore(self):
        return self.highscore

    def update_score(self, score):
        """Update the current users score"""
        if score == 0:
            self.score = 0
        else:
            self.score += score

    def get_score(self):
        return self.score

    def update_game_count(self, count):
        """Update the current user game count"""
        self.game_count =+ count
        return self.game_count
    
    def update_toss_count(self):
        self.toss_count += 1
        return self.toss_count
    
    def get_toss_count(self):
        """Update users number of tosses"""
        return self.toss_count
    
    def update_round_count(self, score):
        """Updates the score for a round"""
        if score == 0:
            self.round_count = 0
        else:
            self.round_count += score
        return self.round_count
    
    def get_round_count(self):
        """Gets the total score for the round currently playing"""
        return self.round_count


    def cheat(self):
        self.score = 100

    def __str__(self) -> str:
        return f'User name: {self.user_name}\nTotalscore: {self.highscore}'
