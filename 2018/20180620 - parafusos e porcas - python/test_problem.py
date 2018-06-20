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
        self.assertEqual([1, 1], finder.find(2))

    def test_acha_1_1_com_3(self):
        finder = ScrewFinder([(1, 3)])
        self.assertEqual([1, 1], finder.find(2))

    def test_acha_2_caixas(self):
        finder = ScrewFinder([(1, 3), (4,4)])
        self.assertEqual([3, 3], finder.find(4))

    def test_acha_3_caixas(self):
        finder = ScrewFinder([(1, 3), (4, 4), (5, 6)])
        self.assertEqual([4, 4], finder.find(5))

    def test_acha_2_caixas_repetindo(self):
        finder = ScrewFinder([(1, 3), (3, 4)])
        self.assertEqual([2, 3], finder.find(3))

    def test_acha_2_caixas_repetindo_maior(self):
        finder = ScrewFinder([(1, 3), (2, 4)])
        self.assertEqual([3, 4], finder.find(3))

    def test_acha_2_caixas_repetindo_maior_big(self):
        finder = ScrewFinder([(1, 100)] * 100)
        self.assertEqual([4100, 4199], finder.find(42))

if __name__ == "__main__":
    unittest.main()
