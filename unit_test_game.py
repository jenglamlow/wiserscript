import unittest
import itertools
from game import Game


class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        red_list = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']
        white_list = ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7']
        cls._combo = map(''.join, itertools.chain(itertools.product(
            red_list, white_list), itertools.product(white_list, red_list)))

    def setUp(self):
        self.game = Game('game_test_1')

    def tearDown(self):
        pass

    def test_first_locked(self):
        self.game.process('r1w2')

        self.assertFalse(self.game.is_contesting('w2'))
        self.assertTrue(self.game.is_first_lock('w2'))
        self.assertFalse(self.game.is_second_lock('w2'))
        self.assertFalse(self.game.is_eliminated('w2'))

    def test_second_locked(self):
        self.game.process('r1w2')
        self.assertFalse(self.game.is_contesting('w2'))
        self.assertTrue(self.game.is_first_lock('w2'))
        self.assertFalse(self.game.is_second_lock('w2'))
        self.assertFalse(self.game.is_eliminated('w2'))


if __name__ == '__main__':
    unittest.main()
