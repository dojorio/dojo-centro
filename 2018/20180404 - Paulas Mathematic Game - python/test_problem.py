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

    def test_1A2_3(self):
        self.assertEqual(1, paula_game('1A2'))

    def test_1A3_2(self):
        self.assertEqual(2, paula_game('1A3'))
    
    def test_7A3__4(self):
        self.assertEqual(-4, paula_game('7A3'))

    def test_3A7_4(self):
        self.assertEqual(4, paula_game('3A7'))

    def test_3A10_7(self):
        self.assertEqual(7, paula_game('3A10'))

    def test_3A11_8(self):
        self.assertEqual(8, paula_game('3A11'))

    def test_11A3__8(self):
        self.assertEqual(-8, paula_game('11A3'))

if __name__ == "__main__":
    unittest.main()

