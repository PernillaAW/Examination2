import cmd
# import gameplay

class Shell(cmd.Cmd):
    """The introduction to a command driven game of dice"""
    intro = 'This is a game of Pig \n'
    prompt = '(pig)'

    def __init__(self):
        """Instansiate the object"""
        super().__init__()

    def do_start():
        """Start a game of pig."""
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
            # Calls add second player
        else: 
            print(error_message)
    
    def do_quit(self, arg):
        """Quits the game"""
        return True
    
    def do_cheat(self, arg):
        """A cheat to directly win the game (for testing purposes only)"""
        print("Cheater.. cheater..")


