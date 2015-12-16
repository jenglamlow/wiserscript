import unittest
import itertools
from game import Game


class TestGame(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._game = Game('game_test')
        red_list = ['r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7']
        white_list = ['w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7']
        cls._rw_combo = list(map(''.join, itertools.chain(itertools.product(
            red_list, white_list), itertools.product(white_list, red_list))))

    def setUp(self):
        self._game.reset()

    def tearDown(self):
        pass

    def test_first_locked(self):
        for action in self._rw_combo:
            target = action[2:]
            self._game.process(action)

            self.assertFalse(self._game.is_contesting(target))
            self.assertTrue(self._game.is_first_lock(target))
            self.assertFalse(self._game.is_second_lock(target))
            self.assertFalse(self._game.is_eliminated(target))

            self._game.reset()

    def test_second_locked(self):
        self._game.process('r1w2')
        self.assertFalse(self._game.is_contesting('w2'))
        self.assertTrue(self._game.is_first_lock('w2'))
        self.assertFalse(self._game.is_second_lock('w2'))
        self.assertFalse(self._game.is_eliminated('w2'))


if __name__ == '__main__':
    unittest.main()
