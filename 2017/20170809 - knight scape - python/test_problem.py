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

    def test_no_pawns_side(self):
        knight = '2d'
        pawns = []
        self.assertEqual(8, knight_scape(knight, pawns))

if __name__ == "__main__":
    unittest.main()
