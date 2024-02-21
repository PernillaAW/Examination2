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
        self.new_game = "Yes"

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
            self.new_game = self.game.add_two_players()
        else: 
            print(error_message)
        return
    
    def do_toss(self, _):
        """Toss the dices for you"""
        error_message ="Please choose 'players 1' or 'players 2' first."
        if self.new_game == "Yes":
            user, dices = self.game.toss()
            print(f'Dices rolled: {dices[0]}, {dices[1]}')
            if dices[0] == 1 or dices[1]:
                print(f"Oh no, you rolled a 1!")
            else:
                print(f'{user.get_user_name()} has {user.get_score()} points saved.')
        else:
            print(error_message)
    
    def do_hold(self, _):
        """Holds the game and start tallys the score and saves it """
        error_message ="Please choose 'players 1' or 'players 2' first."
        if self.new_game == "Yes":
            self.game.hold()
        else:
            print(error_message)

    
    def do_quit(self, _):
        """Quits the game"""
        return True
    
    def do_exit(self, _):
        """Exits the game"""
        return True  
    
    def do_cheat(self, _):
        """A cheat to directly win the game (for testing purposes only)"""
        print("Cheater.. cheater..")


