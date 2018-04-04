#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/en/problems/view/1192

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1a1_1(self):
        self.assertEqual(1, paula_game('1a1'))

    def test_2a2_4(self):
        self.assertEqual(4, paula_game('2a2'))

    def test_1a2_3(self):
        self.assertEqual(3, paula_game('1a2'))


if __name__ == "__main__":
    unittest.main()

