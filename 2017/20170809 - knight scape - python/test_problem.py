#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/en/problems/view/1147

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_no_pawns(self):
        knight = '4d'
        pawns = []
        self.assertEqual(8, knight_scape(knight, pawns))

    def test_no_pawns_down(self):
        knight = '2d'
        pawns = []
        self.assertEqual(6, knight_scape(knight, pawns))

class TestKnight(unittest.TestCase):
    def test_middle_board(self):
        knight = '4c'
        moves = set(['6b', '6d', '5a', '5e', '3a', '3e', '2b', '2d'])
        self.assertEqual(moves, knight_moves(knight))

    def test_middle_board_shifted(self):
        knight = '4d'
        moves = set(['6c', '6e', '5b', '5f', '3b', '3f', '2c', '2e'])
        self.assertEqual(moves, knight_moves(knight))

    def test_knight_2d(self):
        knight = '2d'
        moves = set(['4c', '4e', '3b', '3f', '1b', '1f'])
        self.assertEqual(moves, knight_moves(knight))

    def test_knight_2e(self):
        knight = '2e'
        moves = set(['4d', '4f', '3c', '3g', '1c', '1g'])
        self.assertEqual(moves, knight_moves(knight))

    def test_knight_1e(self):
        knight = '1e'
        moves = set(['3d', '3f', '2c', '2g'])
        self.assertEqual(moves, knight_moves(knight))

    def test_knight_4b(self):
        knight = '4b'
        moves = set(['6a', '6c', '5d','3d', '2c', '2a'])
        self.assertEqual(moves, knight_moves(knight))

    def test_knight_5b(self):
        knight = '5b'
        moves = set(['7a', '7c', '6d','4d', '3c', '3a'])
        self.assertEqual(moves, knight_moves(knight))

if __name__ == "__main__":
    unittest.main()
