import unittest
from pig import Dice


class TestDiceClass(unittest.TestCase):

    def test_toss(self):
        dice = Dice()
        result = dice.toss()

        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 2)
        self.assertTrue(1 <= result[0] <= 6)
        self.assertTrue(1 <= result[1] <= 6)

    def test_toss_count(self):
        dice = Dice()
        user_name = "a name"
        dice.current_user = user_name
        initial_count = dice.toss_count
        dice.toss_count(user_name)
        updated_count = dice.toss_count

        self.assertEqual(updated_count, initial_count + 1)


if __name__ == "__main__":
    unittest.main()
