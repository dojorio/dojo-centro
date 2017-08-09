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
        moves = ['6b', '6d', '5a', '5e', '3a', '3e', '2b', '2d']
        self.assertEqual(moves, knight_moves(knight))

if __name__ == "__main__":
    unittest.main()
