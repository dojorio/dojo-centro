#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/en/problems/view/1169

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        self.assertEqual(board_to_grain(0), 0)
    def test_2(self):
        self.assertEqual(board_to_grain(1), 1)
    def test_3(self):
        self.assertEqual(board_to_grain(2), 3)
    def test_4(self):
        self.assertEqual(board_to_grain(12), 4095)
    def test_5(self):
        self.assertEqual(board_to_g(4), 1)
    def test_6(self):
        self.assertEqual(board_to_g(3), 0)
    def test_7(self):
        self.assertEqual(board_to_g(5), 2)
    def test_8(self):
        self.assertEqual(board_to_kg(12), 0)
    def test_9(self):
        self.assertEqual(board_to_kg(14), 1)
    def test_10(self):
        self.assertEqual(board_to_kg(19), 43)
    def test_11(self):
        self.assertEqual(board_to_kg(0), 0)
    def test_12(self):
        self.assertEqual(board_to_kg(7), 0)
if __name__ == "__main__":
    unittest.main()
