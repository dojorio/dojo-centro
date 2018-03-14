#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://www.urionlinejudge.com.br/judge/en/problems/view/1276

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        self.assertEqual(letter_range(''), [])

    def test_2(self):
        self.assertEqual(letter_range('a'), ['a:a'])

if __name__ == "__main__":
    unittest.main()
