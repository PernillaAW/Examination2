import user
import dice
import highscore
import pickle


class Gameplay:

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
    def read_to_file(self, user):
        atributes_to_save = {
            "username": user.get_user_name(),
            "highscore": user.get_highscore(),
            "score": user.get_round_count(),
            "game_count": user.game_count,
            "toss_count": user.get_toss_count(),
            "round_cont": user.get_round_count() }
        serialized_data = pickle.dumps(atributes_to_save)
        with open(self.file, 'wb') as file:
            file.write(serialized_data)
        
    #Checks if a current game exists
    def read_from_file(self):
        self.saved_game = []
        try:
            with open(self.file, 'rb') as file:
                user_1, user_2 = pickle.load(file)
                return user_1, user_2
        except FileNotFoundError:
            return None, None
        except EOFError:
            return None, None
    
    def add_two_players(self):
        self.user_name_1 = input("Enter Player 1 name: ")
        self.user_name_2 = input("Enter Player 2 name: ")
        self.user_1 = self.highscore().check_list_current_user(self.user_name_1)
        if self.user_1 is not None:
            self.user_1.game_count += 1
        else:
            self.user_1 = user.User(self.user_name_1)
            self.user_1.game_count += 1

        self.user_2 =  self.highscore().check_list_current_user(self.user_name_2)
        if self.user_2 is not None:
            self.user_2.game_count += 2
        else:
            self.user_2 = user.User(self.user_name_2)
            self.user_2.game_count += 1
        try:
            user_1, user_2 = self.read_from_file()
            if user_1 == self.user_name_1 or user_1 == self.user_name_2:
                self.user_1 = user_1
            elif user_2 == self.user_name_1 or user_2 == self.user_name_2:
                self.user_2 = user_2
        except FileNotFoundError:
            pass



        new_game = "Yes"
        #Checks if there is a current game going. 
        

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
            self.read_to_file(self.user_1)
            return self.user_1
        elif self.users_turn == 2:
            self.users_turn = 1
            self.read_to_file(self.user_2)
            return self.user_2
    
    def winner(self, user):
        self.highscore.read_to_file(user)
        return