#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import MagicMock, patch
from pig import intellegance


class TestintelleganceClass(unittest.TestCase):
    """Test the class."""

    def test_init_object(self):
        """This test initating inteligance object."""
        res = intellegance.Intellegance()
        self.assertIsInstance(res, intellegance.Intellegance)

    def test_level_choice(self):
        """This test that level method choise works."""
        computer = intellegance.Intellegance()
        res = computer.level_choice("hard")
        exp = 3
        self.assertEqual(res, exp)

    def test_calculate_result_two_one(self):
        """This tests the result calculation method getting two 1."""
        computer = intellegance.Intellegance()
        res = computer.calculate_result(1, 1)
        exp = 0
        self.assertEqual(res, exp)

    def test_calculate_result_to_get_hold(self):
        """This tests the result calculation method getting one 1."""
        computer = intellegance.Intellegance()
        res = computer.calculate_result(1, 3)
        exp = 0
        self.assertEqual(res, exp)

    def test_calculate_result(self):
        """This tests the result calculation method for tossing the dice."""
        computer = intellegance.Intellegance()
        res = computer.calculate_result(6, 3)
        exp = 9
        self.assertEqual(res, exp)

    def test_computer_winner(self):
        """This tests the result calculation method for tossing the dice."""
        computer = intellegance.Intellegance()
        res = computer.computer_win()
        exp = 10
        self.assertEqual(res, exp)

    @patch("pig.user.User")
    def test_toss_or_hold_low(self, mock_get):
        """This test method of toss and hold with level low."""
        computer = intellegance.Intellegance()
        computer.level_choice("low")
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 10
        res = computer.toss_or_hold(mock_user)
        exp = 1
        self.assertEqual(res, exp)

    @patch("pig.user.User")
    def test_toss_or_hold_medium(self, mock_get):
        """This test method of toss and hold with level medium."""
        computer = intellegance.Intellegance()
        computer.level_choice("medium")
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 20
        res = computer.toss_or_hold(mock_user)
        exp = 2
        self.assertEqual(res, exp)

    @patch("pig.user.User.get_user_score")
    def test_toss_or_hold_hard(self, mock_get):
        """This test method of toss and hold with level hard."""
        computer = intellegance.Intellegance()
        computer.level_choice("hard")
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 20
        res = computer.toss_or_hold(mock_user)
        exp = 3
        self.assertEqual(res, exp)

    def test_tossing_level_low(self):
        """This will test the toss method with in the toss and hold method."""
        computer = intellegance.Intellegance()
        computer.level_choice(1)
        mock_dice = MagicMock()
        mock_die = mock_dice.return_value
        mock_die.toss.return_value = (2, 5)
        res = computer.tossing(mock_dice)
        exp = 7
        self.assertEqual(res, exp)

    def test_tossing_level_hard(self):
        """This will test the toss method with in the toss and hold method."""
        computer = intellegance.Intellegance()
        computer.level_choice('hard')
        mock_dice = MagicMock()
        mock_die = mock_dice.return_value
        mock_die.dice_cheat.return_value = (2, 8)
        res = computer.tossing(mock_dice)
        exp = 10
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
