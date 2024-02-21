import Dice
import User
import Intellegance


def main():
    player = User.User("G")
    computer = Intellegance.Intellegance()
    computer.level_choice("hard")
    player.update_score(50)
    computer.toss_or_hold(player)
    player.cheat()
    print(computer)
    print(player)


if __name__ == "__main__":
    main()
