import user
import pickle


class Highscore:

    def __init__(self):
        self.file = "highscore.pickle"
        self.playerlist = []

    def new_player(self, user_name):
        """Creats and adds new player"""
        user.User(user_name)
        self.playerlist.append(user)

    def check_list(self, user, user_name, num):
        """Checks if player exist in high score list"""
        for player in self.playerlist:
            if player().get_user_name() == user_name:
                if num == 1:
                    return player
                else:
                    self.playerlist.remove(player)
                    self.playerlist.append(user)
                    return None
        return self.new_player(user_name)

    def read_to_file(self):
        with open(self.file, 'wb') as f:
            pickle.dump(self.playerlist, f)

    def read_from_file(self):
        with open(self.file, 'rb') as file:
            self.playerlist = pickle.load(file)

    def display(self):
        """Displays every player on the list"""
        for x in self.playerlist:
            print(x)
