from pig import User
import pickle


class Highscore:

    def __init__(self):
        self.file = "highscore.pickle"
        self.playerlist = []

    def new_player(self, user_name):
        """Creats and adds new player"""
        new_user = User.User(user_name)
        self.playerlist.append(new_user)
        return new_user
    
    def check_list(self, user):
        for player in self.playerlist:
            if player == user:
                return player

    def check_highscore(self, user, player):
        """Checks if player exist in high score list"""
        if player.get_user_score() < user.get_user_score():
            self.update_highscore_name_change(player, user)
            return user
        return player

    def update_highscore_list(self, player, user):
        self.playerlist.remove(player)
        self.playerlist.append(user)
        return True

    def read_to_file(self):
        try:
            with open(self.file, 'wb') as f:
                pickle.dump(self.playerlist, f)
        except IOError:
            print(f'Could not read file {self.file}')

    def read_from_file(self):
        try:
            with open(self.file, 'rb') as file:
                self.playerlist = pickle.load(file)
        except IOError:
            print(f'Could not read file {self.file}')

    def sort_player_highscore(self):
        self.playerlist.sort(key=lambda x: ([x.highscore], [x.toss_count]),
                             reverse=True)

    def display(self):
        """Displays every player on the list"""
        for x in self.playerlist:
            print(x)
