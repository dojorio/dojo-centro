#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from problem import *


class TestProblem(unittest.TestCase):
    def test_ampulhetas_de_5_e_7_da_10(self):
        self.assertEqual(10, miojo(5, 7))

    def test_ampulhetas_de_7_e_10_da_10(self):
        self.assertEqual(10, miojo(7, 10))

    def test_ampulhetas_de_6_e_9_da_9(self):
        self.assertEqual(9, miojo(6, 9))

    def test_ampulhetas_de_4_e_6_da_9(self):
        self.assertEqual(9, miojo(6, 9))

if __name__ == "__main__":
    unittest.main()

