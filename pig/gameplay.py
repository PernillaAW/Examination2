"""Importing class modules and libraries."""

import pickle
from pig import user, dice, highscore, Intellegance


class Gameplay:
    """A class that handles the gameplay."""
    def __init__(self):
        """Initial class variables"""
        self.computer_score = 0
        self.rounds = 0
        self.round_score = 0
        self.highscore = highscore.Highscore()
        self.user_1 = user.User
        self.user_2 = user.User
        self.users_turn = 1
        self.dice = dice.Dice()
        self.intelligence = Intellegance.Intellegance()

    # Saves a file if user quits before game has ended
    def read_to_file(self,user_to_save_1, user_to_save_2):
        """This saves the game that is being played."""
        to_save = (user_to_save_1, user_to_save_2)
        success = False
        with open("saved_game.pickle", "wb") as file:
            pickle.dump(to_save, file)
            success = True
        return success

    # Checks if a current game exists
    def read_from_file(self):
        """It loads a saved game."""
        try:
            with open("saved_game.pickle", "rb") as file:
                user_to_load = ()
                user_to_load = pickle.load(file)
                return user_to_load
        except FileNotFoundError:
            return None, None
        except EOFError:
            return None, None

    def add_two_players(self):
        """This method asks the player their."""
        user_name_1 = input("Enter Player 1 name: ")
        user_name_2 = input("Enter Player 2 name: ")
        users = [user_name_1, user_name_2]
        return users

    def check_if_user_exists(self, users):
        """Check if the user exists."""
        self.highscore.read_from_file()
        user_name_1 = users[0]
        user_name_2 = users[1]
        self.user_1 = self.highscore.check_list(user_name_1)
        self.user_1.game_count += 1

        self.user_2 = self.highscore.check_list(user_name_2)
        self.user_2.game_count += 2

        users[0] = self.user_1
        users[1] = self.user_2
        return users

    def check_saved_game(self, users):
        """Check to see if there is a game saved."""
        user_name_1 = users[0].get_user_name()
        user_name_2 = users[1].get_user_name()
        try:
            user_to_load = self.read_from_file()
            if user_to_load[0] and user_to_load[1] is not None:
                if (
                    user_to_load[0].get_user_name() == user_name_1
                    or user_to_load[0].get_user_name() == user_name_2
                ):
                    self.user_1 = user_to_load[0]
                if (
                    user_to_load[1].get_user_name() == user_name_1
                    or user_to_load[1].get_user_name() == user_name_2
                ):
                    self.user_2 = user_to_load[1]
        except FileNotFoundError:
            pass
        return users

    def computer_intelligence(self, choice):
        """Choose computer intelligence."""
        self.intelligence.level_choice(choice)

    def toss(self):
        """Where dices gets tossed, added up and saved."""
        dice_1, dice_2 = self.dice.toss()
        dices = (dice_1, dice_2)
        return dices

    def update_user_score(self, dices):
        """Updates the score for user, also handles if user toss one or two one's."""
        dice_1 = dices[0]
        dice_2 = dices[1]
        if self.users_turn == 1:
            self.user_1.update_toss_count()
            if dice_1 == 1 and dice_2 == 1:
                self.user_1.update_score(0)
            if dice_1 == 1 or dice_2 == 1:
                self.user_1.update_round_count(0)
                self.hold()
            else:
                total_dices = dice_1 + dice_2
                self.user_1.update_round_count(total_dices)
                self.user_1.update_score(total_dices)
            return self.user_1
        if self.users_turn == 2:
            if self.user_1 is not None:
                self.user_1.update_toss_count()
            self.user_2.update_toss_count()
            if dice_1 == 1 and dice_2 == 1:
                self.user_2.update_score(0)
            if dice_1 == 1 or dice_2 == 1:
                self.user_2.update_round_count(0)
                self.hold()
            else:
                total_dices = dice_1 + dice_2
                self.user_2.update_round_count(total_dices)
                self.user_2.update_score(total_dices)
            return self.user_2

    def update_user_score_one_player(self, dices, one_player_user):
        """Updates the score for user, also handles if user toss one or two one's."""
        dice_1 = dices[0]
        dice_2 = dices[1]
        self.user_1 = one_player_user
        self.user_1.update_toss_count()
        if dice_1 == 1 and dice_2 == 1:
            self.user_1.update_score(0)
        if dice_1 == 1 or dice_2 == 1:
            self.user_1.update_round_count(0)
            return self.user_1
        else:
            total_dices = dice_1 + dice_2
            self.user_1.update_round_count(total_dices)
            self.user_1.update_score(total_dices)
        return self.user_1

    def hold(self):
        """Saves the users and changes turn."""
        if self.users_turn == 1:
            self.users_turn = 2
            self.read_to_file(self.user_1, self.user_2)
            return self.user_2
        if self.users_turn == 2:
            self.users_turn = 1
            self.read_to_file(self.user_1, self.user_2)
            return self.user_1

    def hold_one_player(self):
        """Saves the users and changes turn."""
        self.user_2 = user.User("computer")
        self.read_to_file(self.user_1, self.user_2)
        self.intelligence.toss_or_hold(self.user_1)
        self.user_2.update_score(self.intelligence.score)
        print(self.intelligence)
        return self.user_1

    def winner(self, user_to_save):
        """When there is a winner their highscor shall be saved."""
        self.read_to_file(None, None)
        if user_to_save.get_user_toss_count != 0:
            user_to_save.update_highscore()
            old_user_score = self.highscore.check_list(user_to_save)
            self.highscore.check_highscore(user_to_save, old_user_score)
            self.highscore.read_to_file()
        return True
