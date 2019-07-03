#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1028

class TestProblem(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(maior_pilha(1, 1), 1)

    def test_2_2(self):
        self.assertEqual(maior_pilha(2, 2), 2)

    def test_3_3(self):
        self.assertEqual(maior_pilha(3, 3), 3)

    def test_2_1(self):
        self.assertEqual(maior_pilha(2, 1), 1)

    def test_1_2(self):
        self.assertEqual(maior_pilha(1, 2), 1)

    def test_3_2(self):
        self.assertEqual(maior_pilha(3, 2), 1)   

    def test_5_3(self):
        self.assertEqual(maior_pilha(5, 3), 1)   

    def test_4_6(self):
        self.assertEqual(maior_pilha(4, 6), 2)   

if __name__ == "__main__":
    unittest.main()

