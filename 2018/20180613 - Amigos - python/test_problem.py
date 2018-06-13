#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/repository/UOJ_1726.html

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_single_set(self):
        self.assertEqual('{ABC}', my_party('{ABC}'))

    def test_union_of_two_sets(self):
        self.assertEqual('{AB}', my_party('{A}+{B}'))

if __name__ == "__main__":
    unittest.main()
