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

    def test_3(self):
        self.assertEqual(letter_range('b'), ['b:b'])

    def test_4(self):
        self.assertEqual(letter_range('ab'), ['a:b'])

    def test_5(self):
        self.assertEqual(letter_range('aa'), ['a:a'])

    def test_6(self):
        self.assertEqual(letter_range('bc'), ['b:c'])
 
    def test_7(self):
        self.assertEqual(letter_range('cd'), ['c:d'])

    def test_8(self):
        self.assertEqual(letter_range('ba'), ['a:b'])

    def test_9(self):
        self.assertEqual(letter_range('bd'), ['b:b', 'd:d'])

    def test_10(self):
        self.assertEqual(letter_range(' '), [])

if __name__ == "__main__":
    unittest.main()
