"""Highscore module."""

import pickle
import user


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

    def check_list(self, user):
        """Chackes highscore list for user."""
        for player in self.playerlist:
            if player == user:
                return player
            elif player.get_user_name() == user:
                return player
        return self.new_player(user)

    def check_highscore(self, user, player):
        """Compare current score with previous score in highscore."""
        if player.get_user_score() < user.get_user_score():
            self.update_highscore_list(player, user)
            return user
        return player

    def update_highscore_list(self, player, user):
        """Will update the user in the list."""
        self.playerlist.remove(player)
        self.playerlist.append(user)
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
            key=lambda x: ([x.highscore], [x.toss_count]), reverse=False
        )

    def display(self):
        """Display every player on the list."""
        print(f'{"Name":15s} {"Highscore":<20s} {"Tosses":<15s}')
        for x in self.playerlist:
            print(f'{x.user_name:15s} {x.score:<20.0f}'
                  f'{x.toss_count:<15.0f}')
