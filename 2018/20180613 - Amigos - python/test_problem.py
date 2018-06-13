#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/repository/UOJ_1726.html

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_single_set(self):
        self.assertEqual('{ABC}', my_party('{ABC}'))

    def test_union_of_two_unitary_sets(self):
        self.assertEqual('{AB}', my_party('{A}+{B}'))

    def test_union_of_two_unitary_sets2(self):
        self.assertEqual('{AC}', my_party('{A}+{C}'))

    def test_union_of_two_sets(self):
        self.assertEqual('{AC}', my_party('{A}+{AC}'))

    def test_difference(self):
        self.assertEqual('{A}', my_party('{A}-{B}'))

    def test_difference_2(self):
        self.assertEqual('{B}', my_party('{B}-{A}'))

    def test_difference_3(self):
        self.assertEqual('{}', my_party('{A}-{A}'))
    
    def test_difference_2(self):
        self.assertEqual('{B}', my_party('{B}-{AC}'))



if __name__ == "__main__":
    unittest.main()
