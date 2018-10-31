#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/pt/problems/view/2235

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_1_1_S(self):
        self.assertEqual(viagem([1, 1, 1]), "S")

    def test_100_30_40_N(self):
        self.assertEqual(viagem([100, 30, 40]), "N")

    def test_110_30_40_N(self):
        self.assertEqual(viagem([110, 30, 40]), "N")

    def test_90_40_30_N(self):
        self.assertEqual(viagem([90, 40, 30]), "N")

    def test_90_30_10_N(self):
        self.assertEqual(viagem([90, 30, 10]), "N")

    def test_100_30_30_S(self):
        self.assertEqual(viagem([100, 30, 30]), "S")

if __name__ == "__main__":
    unittest.main()

