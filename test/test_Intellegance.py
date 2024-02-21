#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pig import Intellegance, User
import unittest


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

    def test_toss_or_hold_return_true(self):
        computer = Intellegance.Intellegance()
        computer.level_choice('low')
        player_1 = User.User("G")
        res = computer.toss_or_hold(player_1)
        self.assertTrue(res)


if __name__ == "__main__":
    unittest.main()
