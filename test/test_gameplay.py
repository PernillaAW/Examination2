import unittest
from pig import gameplay

class TestGameplayClass (unittest.TestCase):
    def test_init_default_object(self):
        """Checks that object can be instanciated"""
        game = gameplay.Gameplay()
        self.assertIsInstance(game, gameplay.Gameplay)
   
    def test_read_from_file(self):
        game = gameplay.Gameplay()

        res = game.read_from_file()
        exp = [("Pernilla", 25, 4), ("Valdemar", 28, 4)]
        self.assertEqual(res, exp)
