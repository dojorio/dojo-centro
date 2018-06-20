#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://www.urionlinejudge.com.br/judge/pt/problems/view/1520

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_nao_acha(self):
        finder = ScrewFinder([(1, 1)])
        self.assertEqual([], finder.find(2))

    def test_acha(self):
        finder = ScrewFinder([(1, 1)])
        self.assertEqual([0, 0], finder.find(1))

    def test_nao_acha_1(self):
        finder = ScrewFinder([(2, 2)])
        self.assertEqual([], finder.find(1))
    
    def test_acha_1_1(self):
        finder = ScrewFinder([(1, 2)])
        self.assertEqual([1,1], finder.find(2))

if __name__ == "__main__":
    unittest.main()
