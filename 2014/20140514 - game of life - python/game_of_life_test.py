import unittest

from game_of_life import game_of_life, neighbors


class TestGameOfLife(unittest.TestCase):
    def test_1x1_alive(self):
        board = [[1]]
        self.assertEqual(game_of_life(board), [[0]])

    def test_2x1_alive_dead(self):
        board = [[1, 0]]
        self.assertEqual(game_of_life(board), [[0, 0]])

    def test_3x1_one_stay_alive(self):
        board = [[1, 1, 1]]
        expected = [[0, 1, 0]]
        self.assertEqual(game_of_life(board), expected)

    def test_3x1_all_dead(self):
        board = [[1, 0, 1]]
        expected = [[0, 0, 0]]
        self.assertEqual(game_of_life(board), expected)

    def test_3x1_all_dead(self):
        board = [[1, 0, 1]]
        expected = [[0, 0, 0]]
        self.assertEqual(game_of_life(board), expected)

class TestLittleV(unittest.TestCase):
    def test_with_no_neighbors(self):
        board = [[1]]
        self.assertEqual(neighbors(board, 0, 0), 0)

    def test_with_no_neighbors_dois(self):
        board = [[1, 1]]
        self.assertEqual(neighbors(board, 0, 0), 1)

unittest.main()
