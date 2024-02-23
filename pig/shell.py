import cmd
import dice
import gameplay

class Shell(cmd.Cmd):
    """The introduction to a command driven game of dice"""
    intro = 'This is a game of Pig \n'
    prompt = '(PIG)'

    def __init__(self):
        """Instansiate the object"""
        super().__init__()
        self.dice = dice.Dice()
        self.game = gameplay.Gameplay()
        self.new_game = "No"

    #def do_start(self, _):
        """Start a game of pig."""
        #self.game.

        # Calls a class.method that starts the game
        
    
    def do_players(self, arg):
        """
        User decides to play against computer or another player 
        'players 1' - Play against the computer
        'players 2' - Play against a friend 
        """
        error_message ="Invalid choice. Write 'players 1' or 'players 2'"
        if (arg == '1'):
            # Calls the computer intelligence
            print('You have choosen to play against the computer')
        elif (arg == '2'):
            print('You have choosen to play against another player.')
            user_1, user_2 = self.game.add_two_players()
            print(f"Welcome {user_1.get_user_name()} and \
                  {user_2.get_user_name()}! {user_1.get_user_name()} starts. Write toss to \
                    start the game.")
            self.new_game = "Yes"
        else: 
            print(error_message)
        return
    
    def do_toss(self, _):
        """Toss the dices for you"""
        error_message ="Please choose 'players 1' or 'players 2' first."
        if self.new_game == "Yes":
            user, dices = self.game.toss()
            print(f'Dices rolled: {dices[0]}, {dices[1]}')
            if dices[0] == 1 or dices[1] == 1:
                print(f"\nBad luck, you rolled a 1. {user.get_user_name()} no points this round. \n")
            elif dices[0] == 1 and dices[1] == 1:
                print(f"\nNo, two ones, all {user.get_user_name()} points disapear. \n")
            else:
                if user.get_score() >= 100:
                    print(f"{user.get_user_name()} has won the game! Congratulations.")
                    self.game.winner(user)
                    return
                else:
                    print(f'\n{user.get_user_name()} has {user.get_round_count()} points this round, Toss or Hold?.\n')
        else:
            print(error_message)
    
    def do_hold(self, _):
        """Holds the game and start tallys the score and saves it """
        user = self.game.hold()
        print(f"\n{user.get_user_name()}'s turn to play. Your total score is " 
              f"{user.get_score()} and you have tossed {user.get_toss_count()} times.\n")


    
    def do_quit(self, _):
        """Quits the game"""
        return True
    
    def do_exit(self, _):
        """Exits the game"""
        return True  
    
    def do_cheat(self, _):
        """A cheat to directly win the game (for testing purposes only)"""
        print("Cheater.. cheater..")


