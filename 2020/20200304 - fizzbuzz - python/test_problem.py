#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1(self):
        self.assertEqual(fizzbuzz(1), 1)

    def test_2(self):
        self.assertEqual(fizzbuzz(2), 2)

    def test_3(self):
        self.assertEqual(fizzbuzz(3), 'fizz')

    def test_4(self):
        self.assertEqual(fizzbuzz(4), 4)

    def test_5(self):
        self.assertEqual(fizzbuzz(5), 5)    
if __name__ == "__main__":
    unittest.main()

