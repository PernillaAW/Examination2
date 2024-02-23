"""Importing class modules and libraries"""
import pickle
import user
import dice
import highscore


class Gameplay:
    """A class that handles the gameplay"""
    def __init__(self):
        self.computer_score = 0
        self.rounds = 0
        self.file = "saved_game.pickle"
        self.highscore = highscore.Highscore
        self.user_1 = None
        self.user_2 = None
        self.users_turn = 1
        self.dice = dice.Dice
        self.round_score = 0

    #Saves a file if user quits before game has ended
    def read_to_file(self, user_to_save_1, user_to_save_2):
        to_save = (user_to_save_1, user_to_save_2)
        with open(self.file, 'wb') as file:
            pickle.dump(to_save, file)
       
    #Checks if a current game exists
    def read_from_file(self):
        """Loads a saved pickle file"""
        try:
            with open(self.file, 'rb') as file:
                user_to_load = ()
                user_to_load = pickle.load(file)
                return user_to_load
        except FileNotFoundError:
            return None, None
        except EOFError:
            return None, None
    
    def add_two_players(self):
        user_name_1 = input("Enter Player 1 name: ")
        user_name_2 = input("Enter Player 2 name: ")
        self.user_1 = self.highscore().check_list_current_user(user_name_1)
        if self.user_1 is not None:
            self.user_1.game_count += 1
        else:
            self.user_1 = user.User(user_name_1)
            self.user_1.game_count += 1

        self.user_2 =  self.highscore().check_list_current_user(user_name_2)
        if self.user_2 is not None:
            self.user_2.game_count += 2
        else:
            self.user_2 = user.User(user_name_2)
            self.user_2.game_count += 1
        try:
            user_to_load = self.read_from_file()
            if user_to_load[0] and user_to_load[1] is not None:
                if user_to_load[0].get_user_name() == user_name_1 or \
                   user_to_load[0].get_user_name() == user_name_2:
                    self.user_1 = user_to_load[0]
                if user_to_load[1].get_user_name() == user_name_1 or \
                     user_to_load[1].get_user_name() == user_name_2:
                    self.user_2 = user_to_load[1]
        except FileNotFoundError:
            pass
        return

    def toss(self):
        dice_1, dice_2 = self.dice().toss()
        dices = [dice_1, dice_2]
        if self.users_turn == 1:
            self.user_1.update_toss_count()
            if dice_1 == 1 and dice_2 ==1:
                self.user_1.update_score(0)
            if dice_1 == 1 or dice_2 == 1:
                self.user_1.update_round_count(0)
                self.hold()
            else:
                total_dices = dice_1 + dice_2
                self.user_1.update_round_count(total_dices)
                self.user_1.update_score(total_dices)
            return self.user_1, dices
        if self.users_turn == 2:
            self.user_2.update_toss_count()
            if dice_1 == 1 and dice_2 ==1:
                self.user_2.update_score(0)
            if dice_1 == 1 or dice_2 == 1:
                self.user_2.update_round_count(0)
                self.hold()
            else:
                total_dices = dice_1 + dice_2
                self.user_2.update_round_count(total_dices)
                self.user_2.update_score(total_dices)
            return self.user_2, dices
             
    def hold(self):
        if self.users_turn == 1:
            self.users_turn = 2
            self.read_to_file(self.user_1, self.user_2)
            return self.user_2
        elif self.users_turn == 2:
            self.users_turn = 1
            self.read_to_file(self.user_1, self.user_2)
            return self.user_1
    
    def winner(self, user_to_save):
        self.read_to_file(None, None)
        self.highscore.read_to_file(user_to_save)
        return