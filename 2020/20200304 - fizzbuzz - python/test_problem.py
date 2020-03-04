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
        self.assertEqual(fizzbuzz(5), 'buzz')

    def test_6(self):
        self.assertEqual(fizzbuzz(6), 'fizz')

    def test_7(self):
        self.assertEqual(fizzbuzz(7), 7)

    def test_8(self):
        self.assertEqual(fizzbuzz(8), 8)

    def test_9(self):
        self.assertEqual(fizzbuzz(9), 'fizz')

    def test_10(self):
        self.assertEqual(fizzbuzz(10), 'buzz')    

    def test_11(self):
        self.assertEqual(fizzbuzz(11), 11)
    
    def test_15(self):
        self.assertEqual(fizzbuzz(15), 'fizzbuzz')

if __name__ == "__main__":
    unittest.main()

