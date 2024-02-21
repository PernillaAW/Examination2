import unittest
from unittest.mock import *
from pig import gameplay, user

class TestGameplayClass (unittest.TestCase):

    def test_init_default_object(self):
        """Checks that object can be instanciated"""
        game = gameplay.Gameplay()
        self.assertIsInstance(game, gameplay.Gameplay)
   
    def test_read_from_file(self):
        game = gameplay.Gameplay()

        res = game.read_from_file()
        exp = [("Pernilla", 25, 4), ("Valdemar", 28, 4)]
        self.assertEqual(res, exp)

    def test_add_two_players(self):
        game = gameplay.Gameplay()

        res = game.add_two_players()
        exp = "Yes"
        self.assertEqual(res, exp)

    @patch('pig.user.User')
    def test_toss(self, mock_user):
        self.game = gameplay.Gameplay()
        mock_user_1 = Mock()
        mock_user_1.get_user_name.return_value = "p"
        self.game.user_1 = mock_user_1

        res = self.game.toss()
        exp = 1
        self.assertEqual(res, exp)


    def test_hold(self):
        game = gameplay.Gameplay()
        res = game.hold()
        exp = 2
        self.assertEqual(res, exp)