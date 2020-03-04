#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(miojo(1,1), 3)

    def test_2_5(self):
        self.assertEqual(miojo(2,5), 5)

    def test_2_7(self):
        self.assertEqual(miojo(2,7), 7)

    def test_2_9(self):
        self.assertEqual(miojo(2,9), 9)

    def test_2_4(self):
        self.assertEqual(miojo(2,4), 'ampulhetas inválidas')

    def test_2_6(self):
        self.assertEqual(miojo(2,6), 'ampulhetas inválidas')

    def test_6_4(self):
        self.assertEqual(miojo(6,4), 'ampulhetas inválidas')

    def test_8_10(self):
        self.assertEqual(miojo(8,10), 'ampulhetas inválidas')    

if __name__ == "__main__":
    unittest.main()

