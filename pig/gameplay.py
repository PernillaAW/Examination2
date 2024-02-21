import user
import dice
import highscore
#import pickle


class Gameplay:

    def __init__(self):
        self.computer_score = 0
        self.rounds = 0
        self.file = "pig\saved_games.txt"
        self.highscore = highscore.Highscore
        self.user_1 = None
        self.user_2 = None
        self.users_turn = 1
        self.dice = dice.Dice

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
    

    def add_two_players(self):
        self.saved_game = self.read_from_file()
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

        new_game = "Yes"
        for saved in self.saved_game:
            if self.user_name_1 == saved[0] or self.user_name_2 == saved[0]:
                new_game = "No"
        return new_game

    def toss(self):
            dice_1, dice_2 = self.dice().toss()
            dices = [dice_1, dice_2]
            total_dice = dice_1 + dice_2
            if self.users_turn == 1:
                if dice_1 == 1 or dice_2 == 1:
                    self.hold()
                    return self.user_1, dices
                else:
                    print(f"{self.user_1.get_user_name()}'s turn:")
                    self.user_1.update_score(total_dice)
                    self.user_1.update_toss_count()
                    return self.user_1, dices
            elif self.users_turn == 2:
                if dice_1 == 1 or dice_2 == 1:
                    self.hold()
                    return self.user_2, dices
                else:
                    print(f"{self.user_2.user_name}'s turn")
                    self.user_2.update_score(total_dice)
                    self.user_2.update_toss_count()
                    return self.user_2, dices
    
    def hold(self):
        if self.users_turn == 1:
            self.users_turn = 2
            return self.users_turn
        if self.users_turn == 2:
            self.users_turn = 1
        return self.users_turn