import unittest
from game_of_life import game_of_life

class TestGameOfLife(unittest.TestCase):
    def test_1x1_alive(self):
        board = [[1]]
        self.assertEqual(game_of_life(board), [[0]])

    def test_2x1_alive_dead(self):
        board = [[1, 0]]
        self.assertEqual(game_of_life(board), [[0, 0]])

    def test_3x1_alive_dead(self):
        board = [[1, 1, 1]]
        expected = [[0, 1, 0]]
        self.assertEqual(game_of_life(board), expected)

unittest.main()
