"""Shell this is what the user see"""

import cmd
from pig import dice, gameplay, intellegance, user, highscore, rules


class Shell(cmd.Cmd):
    """The introduction to a command driven game of dice."""

    intro = "This is a game of Pig \n\
     ___________________________________ \n\
    |                Menu               |\n\
    | players 1 - start 1 player game   |\n\
    | players 2 - start 2 player game   |\n\
    | hold - pause current game         |\n\
    | display - highscore list          |\n\
    | change_name                       |\n\
    | cheat - to win game               |\n\
    | rules                             |\n\
    | ? - help                          |\n\
    | exit                              |\n\
    |___________________________________|\n"
    prompt = "(PIG)"

    def __init__(self):
        """Instansiate the object."""
        super().__init__()
        self.dice = dice.Dice()
        self.game = gameplay.Gameplay()
        self.two_player = ""
        self.intelligence = intellegance.Intellegance()
        self.user_comp_1 = user.User
        self.computer = user.User
        self.highscore = highscore.Highscore()

    def do_players(self, arg):
        """
        User decides to play against computer or another player.
        'players 1' - Play against the computer
        'players 2' - Play against a friend
        """
        error_message = "Invalid choice. Write 'players 1' or 'players 2'"
        if arg == "1":
            # Calls the computer intelligence
            print("You have choosen to play against the computer")
            level = input("At what level do you want to start?")
            self.game.computer_intelligence(level)
            user_name = input("What is your name?: ")
            self.user_comp_1 = user.User(user_name)
            self.computer = user.User("Computer")
            self.user_comp_1 = self.game.check_if_user_exists_one_player(
                self.user_comp_1
            )
            self.user_comp_1 = self.game.check_saved_game_one_player(self.user_comp_1)
            self.two_player = "No"
        elif arg == "2":
            print("You have choosen to play against another player.")
            users = self.game.add_two_players()
            users = self.game.check_if_user_exists(users)
            users = self.game.check_saved_game(users)
            user_1 = users[0]
            user_2 = users[1]
            print(
                f"Welcome \n{user_1.get_user_name()} and "
                f"\n{user_2.get_user_name()} \n{user_1.get_user_name()} starts."
                f"\nWrite toss to start the game."
            )
            self.two_player = "Yes"
        else:
            print(error_message)

    def do_toss(self, _):
        """Toss the dices for you."""
        error_msg = "Please enter 'player 1' or 'player 2'."
        dices = self.game.toss()
        if self.two_player == "Yes":
            user_1 = self.game.update_user_score(dices)
            print(f"Dices rolled: {dices[0]}, {dices[1]}")
            if dices[0] == 1 or dices[1] == 1:
                print(
                    f"\nBad luck, you rolled a 1. {user_1.get_user_name()} "
                    f"no points this round. \n"
                )
            elif dices[0] == 1 and dices[1] == 1:
                print(
                    f"\nNo, two ones, all of  {user_1.get_user_name()}'s points disapear. \n"
                )
            if user_1.get_user_score() >= 100:
                print(
                    f"{user_1.get_user_name()} has won the game! Congratulations.\n\n "
                )
                user_1.update_highscore()
                self.game.winner(user_1)
                return self.cmdloop()
            print(
                f"\n{user_1.get_user_name()} has {user_1.get_user_score()}"
                f"and {user_1.score} points this round, Toss or Hold?.\n"
            )
        # Plays against computer
        elif self.two_player == "No":
            self.user_comp_1 = self.game.update_user_score_one_player(
                dices, self.user_comp_1
            )
            print(f"Dices rolled: {dices[0]}, {dices[1]}")
            if dices[0] == 1 or dices[1] == 1:
                print(
                    f"\nBad luck, you rolled a 1. {self.user_comp_1.get_user_name()}"
                    f" no points this round. \n"
                )
                self.game.hold_one_player()
            elif dices[0] == 1 and dices[1] == 1:
                print(
                    f"\nNo, two ones, all {self.user_comp_1.get_user_name()} points disapear. \n"
                )
                self.game.hold_one_player()

            if self.user_comp_1.get_user_score() >= 100:
                print(
                    f"{self.user_comp_1.get_user_name()} has won the game! Congratulations.\n\n"
                )
                self.user_comp_1.update_highscore()
                self.game.winner(self.user_comp_1)
                return self.cmdloop()
            print(
                f"\n{self.user_comp_1.get_user_name()} has "
                f"{self.user_comp_1.get_user_score()}"
                f" points this round, Toss or Hold?.\n"
            )
        else:
            print(error_msg)

    def do_hold(self, _):
        """Hold the game and start tallys the score and saves it."""
        if self.two_player == "Yes":
            user_1 = self.game.hold()
            print(
                f"\n{user_1.get_user_name()}'s turn to play. Your total score is "
                f"{user_1.get_user_score()} and you have tossed {user_1.get_user_toss_count()}"
                f" times.\n"
            )
        elif self.two_player == "No":
            self.game.hold_one_player()

    def do_change_name(self, _):
        """Change user name."""
        player_name = input("What is your user name: ")
        self.highscore.read_from_file()
        player = self.highscore.check_list(player_name)
        old_name = player
        new_name = input("Whats your new user name: ")
        player.change_name(new_name)
        self.highscore.update_highscore_list(old_name, player)

    def do_display(self, _):
        """Will display the highscore list."""
        print("High score list")
        self.highscore.read_from_file()
        self.highscore.display()

    def do_exit(self, _):
        """Exit the game."""
        return True

    def do_cheat(self, _):
        """Cheat to win the game (for testing purposes only)."""
        print("Cheater.. cheater..")
        self.game.cheater()

    def do_rules(self, _):
        """The rules of the game."""
        print(rules.Rules.__doc__)
