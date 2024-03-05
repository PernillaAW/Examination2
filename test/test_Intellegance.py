#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import MagicMock, patch
from pig import Intellegance


class TestIntelleganceClass(unittest.TestCase):
    """Test the class."""

    def test_init_object(self):
        """This test initating inteligance object."""
        res = Intellegance.Intellegance()
        self.assertIsInstance(res, Intellegance.Intellegance)

    def test_level_choice(self):
        """This test that level method choise works."""
        computer = Intellegance.Intellegance()
        res = computer.level_choice("low")
        exp = 1
        self.assertEqual(res, exp)

    def test_calculate_result_two_one(self):
        """This tests the result calculation method getting two 1."""
        computer = Intellegance.Intellegance()
        res = computer.calculate_result(1, 1)
        exp = 0
        self.assertEqual(res, exp)

    def test_calculate_result_to_get_hold(self):
        """This tests the result calculation method getting one 1."""
        computer = Intellegance.Intellegance()
        res = computer.calculate_result(1, 3)
        exp = 1
        self.assertEqual(res, exp)

    def test_calculate_result(self):
        """This tests the result calculation method for tossing the dice."""
        computer = Intellegance.Intellegance()
        res = computer.calculate_result(6, 3)
        exp = 9
        self.assertEqual(res, exp)

    def test_computer_winner(self):
        """This tests the result calculation method for tossing the dice."""
        computer = Intellegance.Intellegance()
        with patch.object(computer, 'score', 100):
            assert computer.score == 100
            res = computer.computer_win()
            exp = True
            self.assertEqual(res, exp)

    @patch("pig.user.User")
    def test_toss_or_hold_low_score_over_100(self, mock_get):
        """This test method of toss and hold with low and score 100."""
        computer = Intellegance.Intellegance()
        computer.level_choice('low')
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 20
        # with patch.object(computer, 'score', 100):
        #     assert computer.score == 100
        #     with patch.object(computer, "computer_win", return_value=True) as mock_return:
        #         computer.toss_or_hold(mock_user)
        #         mock_return.assert_called_once()
            
    @patch("pig.user.User")
    def test_toss_or_hold_low(self, mock_get):
        """This test method of toss and hold with level low."""
        computer = Intellegance.Intellegance()
        computer.level_choice("low")
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 10
        res = computer.toss_or_hold(mock_user)
        exp = 1
        self.assertEqual(res, exp)

    @patch("pig.user.User")
    def test_toss_or_hold_medium_score_over_100(self, mock_get):
        """This test method of toss and hold with medium and score 100."""
        computer = Intellegance.Intellegance()
        computer.level_choice('medium')
        # with patch.object(computer, 'score', 100):
        #     assert computer.score == 100
        #     mock_user = mock_get.return_value
        #     mock_user.get_user_score.return_value = 20
        #     with patch.object(computer, "computer_win", return_value=True) as mock_return:
        #         computer.toss_or_hold(mock_user)
        #         mock_return.assert_called_once()

    @patch("pig.user.User")
    def test_toss_or_hold_medium(self, mock_get):
        """This test method of toss and hold with level medium."""
        computer = Intellegance.Intellegance()
        computer.level_choice("medium")
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 20
        res = computer.toss_or_hold(mock_user)
        exp = 2
        self.assertEqual(res, exp)


    @patch("pig.user.User.get_user_score")
    def test_toss_or_hold_hard_score_over_100(self, mock_get):
        """This test method of toss and hold with hard and score 100."""
        computer = Intellegance.Intellegance()
        computer.level_choice('hard')
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 20
        # with patch.object(computer, 'score', 100):
        #     assert computer.score == 100
        #     with patch.object(computer, "computer_win", return_value=True) as mock_return:
        #         computer.toss_or_hold(mock_user)
        #         mock_return.assert_called_once()

    @patch("pig.user.User.get_user_score")
    def test_toss_or_hold_hard(self, mock_get):
        """This test method of toss and hold with level hard."""
        computer = Intellegance.Intellegance()
        computer.level_choice("hard")
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 20
        res = computer.toss_or_hold(mock_user)
        exp = 3
        self.assertEqual(res, exp)

    def test_tossing(self):
        """This will test the toss method with in the toss and hold method."""
        computer = Intellegance.Intellegance()
        mock_dice = MagicMock()
        mock_die = mock_dice.return_value
        mock_die.toss.return_value = (2, 5)
        res = computer.tossing(mock_dice)
        exp = 7
        self.assertEqual(res, exp)


        

if __name__ == "__main__":
    unittest.main()
