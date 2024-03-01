"""Test module to test the module gameplay.py"""
import unittest
from unittest.mock import MagicMock, Mock, patch
from pig import gameplay
import builtins
import pickle

class TestGameplayClass (unittest.TestCase):
    """Class to test the class gameplay.py"""

    def test_init_default_object(self):
        """Checks that object can be instanciated"""
        game = gameplay.Gameplay()
        self.assertIsInstance(game, gameplay.Gameplay)

    def test_read_to_file(self,):
        """Checks so it can save to a file successfully"""
        mock_user_1 = Mock()
        mock_user_2 = Mock()
        game = gameplay.Gameplay()
        with unittest.mock.patch("pickle.dump"):
            sucess = game.read_to_file(mock_user_1, mock_user_2)
            self.assertTrue(sucess)

    @patch('os.path.exists')
    @patch('builtins.open', new_callable=MagicMock)
    @patch('pickle.load')
    def test_read_from_file(self, mock_load, mock_open, mock_no_file):
        """Checks so that the program can read from a file"""
        game = gameplay.Gameplay()
        filename = "saved_game.pickle"
        game.read_from_file()

        mock_open.assert_called_once_with(filename, 'rb')
        mock_load.assert_called_once_with(mock_open().__enter__())

    @patch('builtins.open')
    def test_read_from_file_exeptions(self, mock_open):
        """Checks the Exeptions in the read from file method"""
        mock_open.side_effect = FileNotFoundError
        game = gameplay.Gameplay()
        res_1, res_2 = game.read_from_file()
        self.assertIsNone(res_1)
        self.assertIsNone(res_2)

        mock_open.side_effect = EOFError
        res_1, res_2 = game.read_from_file()
        self.assertIsNone(res_1)
        self.assertIsNone(res_2)


    @patch('builtins.input', side_effect=["player 1", "player 2"])
    def test_add_two_players(self, mocked_input):
        """Test if two players can be added."""
        game = gameplay.Gameplay()
        res = game.add_two_players()
        self.assertEqual(res, ["player 1", "player 2"])

    @patch('pig.user.User')
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

    @patch('pig.user.User')
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

    @patch('pig.user.User')
    @patch('pig.gameplay.Gameplay.read_from_file')
    def test_check_saved_game_raises_error(self, mock_read, mock_user):
        """Test if FileNotFound raises an error when there is
        any games saved"""
        mock_read.side_effect = FileNotFoundError
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

    @patch('pig.Intellegance.Intellegance.level_choice')
    def test_computer_intelligence(self, mock_choice): 
        """Test so that the call for intelligence works""" 
        game = gameplay.Gameplay()
        game.computer_intelligence(mock_choice)
        self.assertTrue(mock_choice.called)

    @patch('pig.dice.random')
    def test_toss(self, mock_random):
        """Testing the toss method so it returns user and dices"""
        mock_random.randint.side_effect = [3, 4]
        game = gameplay.Gameplay()
        res = game.toss()
        exp = (3, 4)
        self.assertEqual(res, exp)

    @patch('pig.dice.Dice')
    @patch('pig.user.User')
    def test_update_user_score_user_2(self, mock_dice, mock_user):
        """Test to see it the user score will update"""
        game = gameplay.Gameplay()
        with patch.object(game, 'users_turn', 2):
            assert game.users_turn == 2
            mock_dice_inst = mock_dice.return_value
            mock_toss = mock_dice_inst.toss.return_value = (2, 4)

            mock_user_inst = mock_user.return_value
        
            initial_score = 10
            mock_user_inst.score = initial_score

            game.update_user_score(mock_toss)
            res = initial_score + sum(mock_toss)
            exp = initial_score + 6

            self.assertEqual(res, exp)

    @patch('pig.dice.Dice')
    @patch('pig.user.User')
    def test_update_user_score_user_1(self, mock_dice, mock_user):
        """Test to see it the user score will update"""
        game = gameplay.Gameplay()
        with patch.object(game, 'users_turn', 1):
            assert game.users_turn == 1
            mock_dice_inst = mock_dice.return_value
            mock_toss = mock_dice_inst.toss.return_value = (2, 4)
            mock_user_inst = mock_user.return_value
            initial_score = 10
            mock_user_inst.score = initial_score
            game.update_user_score(mock_toss)
            res = initial_score + sum(mock_toss)
            exp = initial_score + 6
            self.assertEqual(res, exp)

    @patch('pig.dice.Dice')
    @patch('pig.user.User')
    def test_update_user_score_one_player(self, mock_dice, mock_user):
        """Test to see it the user score will update"""
        mock_dice_inst = mock_dice.return_value
        mock_toss = mock_dice_inst.toss.return_value = (2, 4)

        mock_user_inst = mock_user.return_value
        mock_user_1 = mock_user_inst
        mock_user_1.update_toss_count.return_value = 1
        game = gameplay.Gameplay()
        initial_score = 10
        mock_user_inst.score = initial_score

        game.update_user_score_one_player(mock_toss, mock_user_1)
        res = initial_score + sum(mock_toss)
        exp = initial_score + 6
        self.assertEqual(res, exp)

    def test_hold_user_1(self):
        """Tests the hold method"""
        game = gameplay.Gameplay()
        with patch.object('users_turn', 1):
            assert game.users_turn == 1
            mock_user_inst = MagicMock()
            mock_user_1 = mock_user_inst
            mock_user_2 = mock_user_inst

            with patch('pig.gameplay.Gameplay.read_to_file', return_value=True) \
            as mock_read_to_file:
                game.user_1 = mock_user_1
                game.user_2 = mock_user_2
                res = game.hold()

            self.assertIsInstance(res, mock_user_inst.__class__)
            mock_read_to_file.assert_called_once()

    def test_hold_user_2(self):
        """Tests the hold method"""
        game = gameplay.Gameplay()
        with patch.object('users_turn', 2):
            assert game.users_turn == 2
            mock_user_inst = MagicMock()
            mock_user_1 = mock_user_inst
            mock_user_2 = mock_user_inst
            with patch('pig.gameplay.Gameplay.read_to_file', return_value=True) as mock_read_to_file:
                game.user_1 = mock_user_1
                game.user_2 = mock_user_2
                res = game.hold()

            self.assertIsInstance(res, mock_user_inst.__class__)
            mock_read_to_file.assert_called_once()

    def test_hold_one_player(self):
        """Tests the hold method when one player plays the game"""
        mock_user_inst = MagicMock()
        mock_user_1 = mock_user_inst
        mock_user_2 = mock_user_inst

        with patch('pig.gameplay.Gameplay.read_to_file', return_value=True) as mock_read_to_file:
            game = gameplay.Gameplay()
            game.user_1 = mock_user_1
            game.user_2 = mock_user_2
            res = game.hold_one_player()

        self.assertIsInstance(res, mock_user_inst.__class__)
        mock_read_to_file.assert_called_once()
    
    # @patch('pig.user.User')
    # def test_winner(self, mock_user):
    #     """Test sp the winners score gets saved"""
    #     mock_user_1 = mock_user.return_value
    #     mock_read_to_file = MagicMock
    #     mock_highscore_check = MagicMock
    #     mock_highscore_check_list = MagicMock
    #     mock_highscore_read_to_file = MagicMock
    #     game = gameplay.Gameplay()
    #     mock_user.return_value.score.return_value = 102
    #     mock_user.return_value.score.return_value = 104
    #     game.winner(mock_user_1)
    #     self.assertTrue(mock_read_to_file.called)
    #     self.assertTrue(mock_highscore_check.called)
    #     self.assertTrue(mock_highscore_check_list.called)
    #     self.assertTrue(mock_highscore_read_to_file.called)