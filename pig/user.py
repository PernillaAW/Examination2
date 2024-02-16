#import Highscore

class User:
    
    def __init__(self, user_name):
        self.user_name = user_name
        #self.highscore = Highscore
        self.score = 0
    
    def change_name(self):
        """Change the name of the user"""
        print(f"Current Username: {self.user_name}" )
        user_name = input(f"Change {self.user_name} to: ")
        self.user_name = user_name
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