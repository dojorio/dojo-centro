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

    def test_2x2_cells_half_dead(self):
        board = [
            [1, 1],
            [0, 0]
        ]
        future_board = [
            [0, 0],
            [0, 0]
        ]
        self.assertEqual(future_board, game_of_life(board))

    def test_2x2_everyone_alive_after(self):
        board = [
            [1, 1],
            [1, 0]
        ]
        future_board = [
            [1, 1],
            [1, 1]
        ]
        self.assertEqual(future_board, game_of_life(board))

    def test_3x3_one_alive(self):
        board = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        future_board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.assertEqual(future_board, game_of_life(board))

    def test_3x3_three_alive(self):
        board = [
            [0, 0, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        future_board = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 1, 0]
        ]
        self.assertEqual(future_board, game_of_life(board))

    def test_3x3_four_alive(self):
        board = [
            [0, 1, 0],
            [1, 1, 1],
            [0, 0, 0]
        ]
        future_board = [
            [1, 1, 1],
            [1, 1, 1],
            [0, 1, 0]
        ]
        self.assertEqual(future_board, game_of_life(board))

    # def test_3x3_four_alive_other_places(self):
    #     board = [
    #         [1, 0, 0],
    #         [1, 1, 1],
    #         [0, 0, 0]
    #     ]
    #     future_board = [
    #         [1, 0, 0],
    #         [1, 1, 0],
    #         [0, 1, 0]
    #     ]
    #     self.assertEqual(future_board, game_of_life(board))


class TestForwardCell(unittest.TestCase):

    def test_one_cell_dead(self):
        board = [
            [0],
        ]
        future_cell = 0
        self.assertEqual(forward_cell(board, x=0, y=0), future_cell)

    def test_2x2_one_dead(self):
        board = [
            [0, 1],
            [1, 1]
        ]
        future_cell = 1
        self.assertEqual(forward_cell(board, x=0, y=0), future_cell)

    def test_2x2_half_dead(self):
        board = [
            [0, 0],
            [1, 1]
        ]
        future_cell = 0
        self.assertEqual(forward_cell(board, x=0, y=0), future_cell)

    def test_2x2_half_dead_transpose(self):
        board = [
            [0, 1],
            [0, 1]
        ]
        future_cell = 0
        self.assertEqual(forward_cell(board, x=0, y=0), future_cell)

    def test_2x2_half_dead_transpose(self):
        board = [
            [0, 0],
            [1, 1]
        ]
        future_cell = 0
        self.assertEqual(forward_cell(board, x=1, y=0), future_cell)


if __name__ == "__main__":
    unittest.main()
