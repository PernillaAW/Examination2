"""Test module to test the module gameplay.py"""
import tempfile
import unittest
import pickle
from unittest.mock import Mock, patch, MagicMock
from pig import gameplay

class TestGameplayClass (unittest.TestCase):
    """Class to test the class gameplay.py"""
    
    def test_init_default_object(self):
        """Checks that object can be instanciated"""
        game = gameplay.Gameplay()
        self.assertIsInstance(game, gameplay.Gameplay)

    @patch('pig.user.User')
    def test_read_to_file(self,_):
        """Checks so it can save to a file successfully"""
        mock_user_1 = Mock()
        mock_user_2 = Mock()
        game = gameplay.Gameplay()
        with unittest.mock.patch("pickle.dump"):
            sucess = game.read_to_file(mock_user_1, mock_user_2)
            self.assertTrue(sucess)

    def test_read_from_file(self):
        """Checks so that the program can read from a file"""
        game = gameplay.Gameplay()
        user_1 = {"user_name": "Pernilla", "score": 20}
        test_file = "test_saved_game.pickle"
        with open(test_file, "wb") as f:
            pickle.dump(user_1, f)
        with unittest.mock.patch("builtins.open", 
                                 unittest.mock.mock_open(read_data=pickle.dumps(user_1))):
            user_to_load = game.read_from_file()
            self.assertEqual(user_to_load, user_1)

    def test_add_two_players(self):
        """Test if two players can be added.s"""
        game = gameplay.Gameplay()

        res = game.add_two_players()
        exp = ["player 1", "player 2"]
        self.assertEqual(res, exp)

    def test_check_if_user_exists(self):
        """Test if check against highscore list"""
        game = gameplay.Gameplay()
        users = ["player 1", "player 2"]
        res = game.check_if_user_exists(users)
        exp = ["player 1", "player 2"]
        self.assertEqual(res, exp)

    @patch('pig.dice.random')
    def test_toss(self, mock_random):
        """Testing the toss method so it returns user and dices"""
        mock_random.randint.side_effect = [3,4]
        game = gameplay.Gameplay()
        res = game.toss()
        exp = (3, 4)
        self.assertEqual(res, exp)


"""
    @patch('pig.user.User')
    def test_add_two_players(self):
        """#Test so that the game can add two players
"""
        game = gameplay.Gameplay()

        res = game.add_two_players()
        exp = "Yes"
        self.assertEqual(res, exp)

    @patch('pig.user.User')
    def test_toss(self, mock_user_1):
        """#Test so the tossing of the dices works and score-tracking
"""
        game = gameplay.Gameplay()
        mock_user_1 = Mock()
        mock_user_1.get_user_name.return_value = "p"
        game.user_1 = mock_user_1

        res = game.toss()
        exp = 1
        self.assertEqual(res, exp)


    def test_hold(self):
        """#Test to check if it works to save and next player's turn
"""
        game = gameplay.Gameplay()
        res = game.hold()
        exp = 2
        self.assertEqual(res, exp)

"""