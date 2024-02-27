import unittest
from unittest.mock import Mock, patch
from pig import Dice


class TestDiceClass(unittest.TestCase):

    @patch('pig.dice.random')
    def test_toss(self, mock_random):
        mock_random.randint.side_effect[2, 5]
        dice = Dice()
        result = dice.toss()

        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertTrue(1 <= result[0] <= 6)
        self.assertTrue(1 <= result[1] <= 6)
        res = [2, 5]
        exp = [2, 5]


if __name__ == "__main__":
    unittest.main()
