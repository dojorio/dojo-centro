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

if __name__ == "__main__":
    unittest.main()

