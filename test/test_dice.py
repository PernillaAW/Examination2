"""Unittest for dice class."""

import unittest
from unittest.mock import Mock, patch
from pig import dice


class TestDiceClass(unittest.TestCase):

    def test_init_object(self):
        res = dice.Dice()
        self.assertIsInstance(res, dice.Dice)

    @patch("pig.dice.random")
    def test_toss(self, mock_random):
        mock_random.randint.side_effect = [2, 5]
        die = dice.Dice()
        result = die.toss()

        self.assertTrue(1 <= result[0] <= 6)
        self.assertTrue(1 <= result[1] <= 6)
        exp = 2, 5

        self.assertEqual(result, exp)

    @patch("pig.dice.random")
    def test_dice_cheat(self, mock_random):
        mock_random.randint.side_effect = (3, 5)
        die = dice.Dice()
        result = die.dice_cheat()

        self.assertTrue(2 <= result[0] <= 6)
        self.assertTrue(2 <= result[1] <= 6)
        exp = 3, 5
        self.assertEqual(result, exp)


if __name__ == "__main__":
    unittest.main()
