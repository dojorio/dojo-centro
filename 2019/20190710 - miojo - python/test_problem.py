#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *

class TestProblem(unittest.TestCase):
    def test_1_1(self):
        self.assertEqual(miojo(1, 1), 3)

    def test_2_5(self):
        self.assertEqual(miojo(2, 5), 5)

    def test_5_2(self):
        self.assertEqual(miojo(5, 2), 5)

    def test_2_2(self):
        self.assertEqual(miojo(2, 2), None)

    def test_3_2(self):
        self.assertEqual(miojo(3, 2), 3)

    def test_4_2(self):
        self.assertEqual(miojo(4, 2), None)

    def test_8_5(self):
        self.assertEqual(miojo(8, 5), 8)

    def test_15_12(self):
        self.assertEqual(miojo(15, 12), 15)

    def test_0_3(self):
        self.assertEqual(miojo(0, 3), 3)

    def test_6_3(self):
        self.assertEqual(miojo(6, 3), 3)

    def test_5_7(self):
        self.assertEqual(miojo(5, 7), 10)

if __name__ == "__main__":
    unittest.main()