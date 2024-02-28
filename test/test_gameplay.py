"""Test module to test the module gameplay.py"""

import unittest
import pickle
from unittest.mock import MagicMock, Mock, patch
import gameplay


class TestGameplayClass(unittest.TestCase):
    """Class to test the class gameplay.py"""

    def test_init_default_object(self):
        """Checks that object can be instanciated"""
        game = gameplay.Gameplay()
        self.assertIsInstance(game, gameplay.Gameplay)

    @patch("pig.user.User")
    def test_read_to_file(self, _):
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
        with unittest.mock.patch(
            "builtins.open", unittest.mock.mock_open(read_data=pickle.dumps(user_1))
        ):
            user_to_load = game.read_from_file()
            self.assertEqual(user_to_load, user_1)

    def test_add_two_players(self):
        """Test if two players can be added.s"""
        game = gameplay.Gameplay()

        res = game.add_two_players()
        exp = ["player 1", "player 2"]
        self.assertEqual(res, exp)

    @patch("pig.user.User")
    def test_check_if_user_exists(self, mock_user_User):
        """Test if check against highscore list"""
        game = gameplay.Gameplay()
        users = ["player 1", "player 2"]

        user_objects = [mock_user_User.return_value(user_name) for user_name in users]

        mock_user_1 = user_objects[0]
        mock_user_1.get_user_name.return_value = "player 1"
        mock_user_2 = user_objects[1]
        mock_user_2.get_user_name.return_value = "player 2"

        res = game.check_if_user_exists(user_objects)

        exp = user_objects
        self.assertEqual(res, exp)

    @patch("pig.user.User")
    def test_check_saved_game(self, mock_user):
        """Test if there is any games saved"""
        game = gameplay.Gameplay()
        users = ["player 1", "player 2"]

        user_objects = [mock_user.return_value(user_name) for user_name in users]

        mock_user_1 = user_objects[0]
        mock_user_1.get_user_name.return_value = "player 1"
        mock_user_2 = user_objects[1]
        mock_user_2.get_user_name.return_value = "player 2"

        res = game.check_saved_game(user_objects)

        exp = user_objects
        self.assertEqual(res, exp)

    @patch("pig.dice.random")
    def test_toss(self, mock_random):
        """Testing the toss method so it returns user and dices"""
        mock_random.randint.side_effect = [3, 4]
        game = gameplay.Gameplay()
        res = game.toss()
        exp = (3, 4)
        self.assertEqual(res, exp)

    @patch("pig.dice.Dice")
    @patch("pig.user.User")
    def test_update_user_score(self, mock_dice, mock_user):
        """Test to see it the user score will update"""
        mock_dice_inst = mock_dice.return_value
        mock_toss = mock_dice_inst.toss.return_value = (2, 4)

        mock_user_inst = mock_user.return_value
        game = gameplay.Gameplay()
        initial_score = 10
        mock_user_inst.score = initial_score

        game.update_user_score(mock_toss)
        res = initial_score + sum(mock_toss)
        exp = initial_score + 6

        self.assertEqual(res, exp)

    def test_hold(self):
        """Tests the hold method"""
        mock_user_inst = MagicMock()
        mock_user_1 = mock_user_inst
        mock_user_2 = mock_user_inst

        with patch(
            "pig.gameplay.Gameplay.read_to_file", return_value=True
        ) as mock_read_to_file:
            game = gameplay.Gameplay()
            game.user_1 = mock_user_1
            game.user_2 = mock_user_2
            res = game.hold()

        self.assertIsInstance(res, mock_user_inst.__class__)
        mock_read_to_file.assert_called_once()
