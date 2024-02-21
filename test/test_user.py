from pig import User, Highscore
import unittest


class TestUserClass(unittest.TestCase):

    def test_init_object(self):
        user = User.User('G')
        self.assertIsInstance(user, User)

    def test_change_name(self):
        highscore = Highscore.Highscore()
        user = highscore.new_player('g')
        res = user.change_name('T')
        self.assertTrue(res)

