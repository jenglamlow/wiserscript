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

    def test_scenario_pending_rescue(self):
        self._game.process('r1w3')
        self._game.process('r1w3')
        self._game.process('r1w2')
        self._game.process('r1w2')
        self._game.process('w4r1')
        self._game.process('w4r1')
        self._game.process('w4r1')
        self._game.process('r6r7')
        self._game.process('w4r2')

        self.assertTrue(self._game.is_contesting('w2'))

    def test_scenario_pending_rescue_2(self):
        self._game.process('r2w3')
        self._game.process('r2w3')
        self._game.process('r2w2')
        self._game.process('r2w1')
        self._game.process('r1w4')
        self._game.process('r1w4')
        self._game.process('r1w2')
        self._game.process('r1w1')
        self._game.process('w6r1')
        self._game.process('w6r1')
        self._game.process('w6r1')
        self._game.process('w6r2')
        self._game.process('w6r2')
        self._game.process('w6r2')
        self._game.process('w6r3')

        self.assertTrue(self._game.is_first_lock('w1'))

        self._game.process('w6r3')

        self.assertTrue(self._game.is_contesting('w1'))

    def test_scenario_miss_hit_rescue(self):
        self._game.process('r2w1')
        self._game.process('r2r3')
        self._game.process('w7r6')
        self._game.process('r4w3')

if __name__ == '__main__':
    unittest.main()
