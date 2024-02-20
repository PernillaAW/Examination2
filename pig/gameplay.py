#import user
#import highscore

class Gameplay:

    def __init__(self):
        self.computer_score = 0
        self.rounds = 0
        self.file = "pig\saved_games.txt"
        #self.player = user.User
    
    #Saves a file if user quits before game has ended
    def read_to_file(self):
        with open(self.file, 'w') as file:
            file.write(self)
        
    #Checks if a current game exists
    def read_from_file(self):
         saved_game = []
         with open(self.file, 'r') as file:
            for l in file:
                record = l.split(' ')
                saved_game_row = (record[0], int(record[1]), int(record[2]))
                saved_game.append(saved_game_row)
            return saved_game
    
    def start_two_players(self):
        self.saved_game = self.read_from_file()
        player_1 = input("Enter Player 1 name: ")
        player_2 = input("Enter Player 2 name: ")
        
            