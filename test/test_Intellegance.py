#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
from unittest.mock import Mock, patch
from pig import Intellegance


class TestIntelleganceClass(unittest.TestCase):
    """Test the class."""

    def test_init_object(self):
        res = Intellegance.Intellegance()
        self.assertIsInstance(res, Intellegance.Intellegance)

    def test_level_choice(self):
        computer = Intellegance.Intellegance()
        res = computer.level_choice("low")
        exp = 1
        self.assertEqual(res, exp)

    def test_calculate_result(self):
        computer = Intellegance.Intellegance()
        res = computer.calculate_result(1, 1)
        exp = 0
        self.assertEqual(res, exp)

    @patch('pig.user.User')
    def test_toss_or_hold_low(self, mock_get):
        computer = Intellegance.Intellegance()
        computer.level_choice('low')
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 10
        res = computer.toss_or_hold(mock_user)
        exp = 1
        self.assertEqual(res, exp)

    @patch('pig.user.User')
    def test_toss_or_hold_medium(self, mock_get):
        computer = Intellegance.Intellegance()
        computer.level_choice('medium')
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 20
        res = computer.toss_or_hold(mock_user)
        exp = 2
        self.assertEqual(res, exp)

    @patch('pig.user.User.get_user_score')
    def test_toss_or_hold_hard(self, mock_get):
        computer = Intellegance.Intellegance()
        computer.level_choice('hard')
        mock_user = mock_get.return_value
        mock_user.get_user_score.return_value = 20
        res = computer.toss_or_hold(mock_user)
        exp = 3
        self.assertEqual(res, exp)

    @patch('pig.dice.Dice')
    def test_toss(self, mock_get):
        computer = Intellegance.Intellegance()
        mock_dice = mock_get.return_value
        mock_dice.toss.return_value = [3, 4]
        res = computer.toss(mock_dice)
        exp = 7
        self.assertEqual(res, exp)


if __name__ == "__main__":
    unittest.main()
