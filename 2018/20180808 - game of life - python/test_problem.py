#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestGameOfLife(unittest.TestCase):
    def test_one_cell_dead(self):
        board = [
            [0],
        ]
        future_board = [
            [0],
        ]
        self.assertEqual(future_board, game_of_life(board))

    def test_one_cell_alive(self):
        board = [
            [1],
        ]
        future_board = [
            [0],
        ]
        self.assertEqual(future_board, game_of_life(board))

    def test_2x2_cells_all_dead(self):
        board = [
            [0, 0],
            [0, 0]
        ]
        future_board = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(future_board, game_of_life(board))

    def test_2x2_cells_one_alive(self):
        board = [
            [1, 0],
            [0, 0]
        ]
        future_board = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(future_board, game_of_life(board))

    def test_2x2_cells_all_alive(self):
        board = [
            [1, 1],
            [1, 1]
        ]
        future_board = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(future_board, game_of_life(board))

if __name__ == "__main__":
    unittest.main()
