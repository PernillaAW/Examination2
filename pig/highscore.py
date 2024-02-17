import user

class Highscore:

    def __init__(self):
        self.file = "highscore.txt"


    def read_to_file(self, player):
        with open(self.file, 'w') as f:
            f.write(player)
    
    def read_from_file(self, player):
         with open(self.file, 'r') as file:
            for list in file:
                highscore_list = list.split(' ')