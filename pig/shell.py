import cmd
import Dice
import Intellegance
import Highscore


class Shell(cmd.Cmd):
    """The introduction to a command driven game of dice"""
    intro = 'This is a game of Pig \n'
    prompt = '(PIG)'

    def __init__(self):
        """Instansiate the object"""
        super().__init__()
        self.dice = Dice.Dice()

    def do_start(self, _):
        """Start a game of pig."""
        dice = Dice.Dice()
        dice.toss()
        playerlist = Highscore.Highscore()
        playerlist.read_from_file()
        player_1 = input("What is you name? ")
        player_1 = playerlist.check_list_current_user(player_1)
        # Calls a class.method that starts the game

    def do_name_change(self, player):
        """Change the name of the user"""
        old_username = player.get_user_name()
        new_name = input(f"Current Username: {old_username} \
                         \nChange {old_username} to: ")
        player.change_name(player, new_name)
        Highscore.Highscore().check_list_add_remove(player, old_username)
        print(f'Your usename has now been changed to {player.get_user_name}')

    def do_players(self, arg):
        """
        User decides to play against computer or another player
        'players 1' - Play against the computer
        'players 2' - Play against a friend
        """
        error_message = "Invalid choice. Write 'players 1' or 'players 2'"
        if (arg == '1'):
            computer = Intellegance.Intellegance
            print('You have choosen to play against the computer')
            choise = input('Now chose game level low, medium, hard: ')
            computer = computer().level_choice(choise)
        elif (arg == '2'):
            print('You have choosen to play against another player.')
            playerlist = Highscore.Highscore()
            playerlist.read_from_file()
            player_2 = input("What is you name? ")
            player_2 = playerlist.check_list_current_user(player_2)
        else:
            print(error_message)

    def do_quit(self, _):
        """Quits the game"""
        Highscore.Highscore().read_to_file()
        return True

    def do_exit(self, _):
        """Exits the game"""
        Highscore.Highscore().read_to_file()
        return True

    def do_cheat(self, _):
        """A cheat to directly win the game (for testing purposes only)"""
        print("Cheater.. cheater..")
        _.cheat()

    def do_high_score_display(self):
        """Display the high score list"""
        Highscore.Highscore().read_from_file().display()
