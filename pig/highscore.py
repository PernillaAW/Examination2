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

    def check_list_current_user(self, user_name):
        """Checks if player exist in high score list"""
        for player in self.playerlist:
            if player().get_user_name() == user_name:
                return player
        return self.new_player(user_name)
    
    def check_list_add_remove(self, user, old_name):
        for player in self.playerlist:
            if player().get_user_name() == old_name:
                self.playerlist.remove(player)
                self.playerlist.append(user)
                return True
        return False

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
