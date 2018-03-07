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
if __name__ == "__main__":
    unittest.main()
