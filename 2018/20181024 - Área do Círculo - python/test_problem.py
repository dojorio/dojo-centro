#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/1002


import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_circulo_2(self):
        self.assertEqual(area(2.00), 'A=12.5664')

    def test_circulo_100_64(self):
        self.assertEqual(area(100.64), 'A=31819.3103')

    def test_circulo_150_00(self):
        self.assertEqual(area(150.00), ' A=70685.7750')

if __name__ == "__main__":
    unittest.main()

