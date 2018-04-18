#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/en/problems/view/1069

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_without_diamond(self):
        self.assertEqual(count_diamonds(''), 0)

    def test_with_diamond(self):
        self.assertEqual(count_diamonds('<>'), 1)

    def test_with_sand_and_diamond(self):
        self.assertEqual(count_diamonds('<.>'), 1)

    def test_with_sand_and_diamond_and_piece(self):
        self.assertEqual(count_diamonds('<.<.>'), 1)

    def test_with_sand_and_diamond_and_piece_and_diamonds(self):
        self.assertEqual(count_diamonds('><.<.>'), 1)

    def test_with_sand_and_diamond_and_piece_and_diamonds_and_diamonds(self):
        self.assertEqual(count_diamonds('<<.>>'), 2)

if __name__ == "__main__":
    unittest.main()

