from pig import User
import unittest


class TestUserClass(unittest.TestCase):

    def test_init_object(self):
        user = User.User('G')
        self.assertIsInstance(user, User.User)

    def test_change_name(self):
        user = User.User('G')
        res = user.change_name('T')
        exp = 'T'
        self.assertEqual(res, exp)

    def test_update_score(self):
        user = User.User('G')
        res = user.update_score(50)
        exp = 50
        self.assertEqual(res, exp)

    def test_update_game_count(self):
        user = User.User('G')
        res = user.update_game_count(50)
        exp = 50
        self.assertEqual(res, exp)

    def test_get_user_name(self):
        user = User.User('G')
        res = user.get_user_name()
        exp = 'G'
        self.assertEqual(res, exp)

    def test_get_score(self):
        user = User.User('G')
        res = user.get_user_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_cheat(self):
        user = User.User('G')
        res = user.cheat()
        exp = 100
        self.assertEqual(res, exp)

    def test_get_highscore(self):
        user = User.User('G')
        res = user.get_highscore()
        exp = 0
        self.assertEqual(res, exp)

    def test_get_toss_count(self):
        user = User.User('G')
        res = user.get_highscore()
        exp = 0
        self.assertEqual(res, exp)

    def test_update_toss_count(self):
        user = User.User('G')
        res = user.update_toss_count(1)
        exp = 1
        self.assertEqual(res, exp)
