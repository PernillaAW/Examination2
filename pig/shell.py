import cmd
import user
import dice
import Intellegance
import highscore


class Shell(cmd.Cmd):
    """The introduction to a command driven game of dice"""
    intro = 'This is a game of Pig \n'
    prompt = '(PIG)'

    def __init__(self):
        """Instansiate the object"""
        super().__init__()
        self.dice = dice.Dice()

    def do_start(self, _):
        """Start a game of pig."""
        playerlist = highscore.Highscore()
        playerlist.read_from_file()
        player_1 = input("What is you name? ")
        player_1 = playerlist.check_list(player_1, 1)
        dice_1, dice_2 = self.dice.toss()
        print(f"{dice_1}, {dice_2}")

        # Calls a class.method that starts the game

    def do_players(self, arg):
        """
        User decides to play against computer or another player 
        'players 1' - Play against the computer
        'players 2' - Play against a friend 
        """
        error_message = "Invalid choice. Write 'players 1' or 'players 2'"
        if (arg == '1'):
            # Calls the computer intelligence
            computer = Intellegance.Intellegance
            print('You have choosen to play against the computer')
            choise = input('Now chose game level low, medium, hard')
            computer = computer().level_choice(choise)
        elif (arg == '2'):
            print('You have choosen to play against another player.')
            # Calls add second player
        else: 
            print(error_message)

    def do_quit(self, _):
        """Quits the game"""
        highscore.Highscore().read_to_file()
        return True

    def do_exit(self, _):
        """Exits the game"""
        highscore.Highscore().read_to_file()
        return True

    def do_cheat(self, _):
        """A cheat to directly win the game (for testing purposes only)"""
        print("Cheater.. cheater..")
        _.cheat()

    def do_high_score_display(self):
        """Display the high score list"""
        highscore.Highscore().read_from_file().display()
    
