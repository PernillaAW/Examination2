import Highscore


class main:

    def main():
        highscore = Highscore.Highscore()
        user = highscore.new_player('g')
        res = user.change_name('T')


if __name__ == '__main__':
    main()
