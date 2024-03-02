"""Unittest."""

import unittest
from pig import user


class TestUserClass(unittest.TestCase):
    """Will do unittest to user class."""

    def test_init_object(self):
        """Will test user object."""
        player = user.User("G")
        self.assertIsInstance(player, user.User)

    def test_change_name(self):
        """Test change name method."""
        player = user.User("G")
        res = player.change_name("T")
        exp = "T"
        self.assertEqual(res, exp)

    def test_update_score(self):
        """Test update score in user."""
        player = user.User("G")
        res = player.update_score(50)
        exp = 50
        self.assertEqual(res, exp)

    def test_update_score_loss_round(self):
        """Tests update score if you loss the round."""
        player = user.User("G")
        res = player.update_score(0)
        exp = 0
        self.assertEqual(res, exp)

    def test_update_game_count(self):
        """Test update game count."""
        player = user.User("G")
        res = player.update_game_count(50)
        exp = 50
        self.assertEqual(res, exp)

    def test_update_round_count(self):
        """Test update round count."""
        player = user.User("G")
        res = player.update_round_count(20)
        exp = 20
        self.assertEqual(res, exp)

    def test_update_highscore(self):
        """Test update user hihscore."""
        player = user.User('G')
        player.update_score(100)
        res = player.update_highscore()
        exp = 100
        self.assertEqual(res, exp)

    def test_get_user_name(self):
        """Test if get user name returns user name."""
        player = user.User("G")
        res = player.get_user_name()
        exp = "G"
        self.assertEqual(res, exp)

    def test_get_score(self):
        """Test that get score returns user score."""
        player = user.User("G")
        res = player.get_user_score()
        exp = 0
        self.assertEqual(res, exp)

    def test_cheat_score(self):
        """Test if cheat works."""
        player = user.User("G")
        res = player.cheat()
        exp = 100
        self.assertEqual(res, exp)

    def test_get_highscore(self):
        """Test if get highscore returns highscore."""
        player = user.User("G")
        res = player.get_highscore()
        exp = 0
        self.assertEqual(res, exp)

    def test_get_toss_count(self):
        """Test if get toss count returns toss count"""
        player = user.User("G")
        res = player.get_user_toss_count()
        exp = 0
        self.assertEqual(res, exp)

    def test_update_toss_count(self):
        """Test update toss count"""
        player = user.User("G")
        res = player.update_toss_count()
        exp = 1
        self.assertEqual(res, exp)
