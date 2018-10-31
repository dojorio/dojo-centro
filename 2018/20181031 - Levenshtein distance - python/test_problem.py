#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.hackerrank.com/contests/cse-830-homework-3/challenges/edit-distance

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_abcde_abde_1(self):
        self.assertEqual(levenshtein("ABCDE", "ABDE"), 1)

    def test_abde_abde_0(self):
        self.assertEqual(levenshtein("ABDE", "ABDE"), 0)

    def test_abcdef_abde_2(self):
        self.assertEqual(levenshtein("ABCDEF", "ABDE"), 2)

if __name__ == "__main__":
    unittest.main()

