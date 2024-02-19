import user
import highscore

class Gameplay:

    def __init__(self):
        self.computer_score = 0
        self.rounds = 0
        self.file = "saved_games.txt"
        self.player = user.User
    
    #Saves a file if user quits before game has ended
    def read_to_file(self):
        with open(self.file, 'w') as file:
            file.write(self)
        
    #Checks if a current game exists
    def read_from_file(self):
         with open(self.file, 'r') as file:
            for list in file:
                current_game = list