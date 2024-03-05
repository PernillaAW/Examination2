"""Highscore module."""

import pickle
from pig import user


class Highscore:
    """All users are saved to the highscore list."""

    def __init__(self):
        """Create object highscore."""
        self.file = "highscore.pickle."
        self.playerlist = []

    def new_player(self, user_name):
        """Create and adds new player."""
        new_user = user.User(user_name)
        self.playerlist.append(new_user)
        return new_user

    def check_list(self, current_user):
        """Chackes highscore list for user."""
        for player in self.playerlist:
            if player == current_user:
                return player
            elif player.get_user_name() == current_user:
                return player
        return self.new_player(current_user)

    def check_highscore(self, current_user, player):
        """Compare current score with previous score in highscore."""
        if player.get_highscore() < current_user.get_highscore():
            if player.get_user_toss_count() > current_user:
                self.update_highscore_list(player, current_user)
                return current_user
        return player

    def update_highscore_list(self, player, current_user):
        """Will update the user in the list."""
        self.playerlist.remove(player)
        self.playerlist.append(current_user)
        return True

    def read_to_file(self):
        """Read list to the binary file."""
        try:
            with open(self.file, "wb") as f:
                pickle.dump(self.playerlist, f)
        except IOError:
            print(f"Could not read file {self.file}")

    def read_from_file(self):
        """Read list from the binary file."""
        try:
            with open(self.file, "rb") as file:
                self.playerlist = pickle.load(file)
        except IOError:
            print(f"Could not read file {self.file}")

    def sort_player_highscore(self):
        """Will sort the highscore list after highscore and tosses."""
        self.playerlist.sort(
            key=lambda x: (x.highscore, -x.toss_count), reverse=(True)
        )

    def display(self):
        """Display every player on the list."""
        self.sort_player_highscore()
        for x in self.playerlist:
            print(f'{x.get_user_name()}\n{x.get_highscore()}\n{x.get_user_toss_count()}')
